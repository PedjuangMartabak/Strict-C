import glob
import os
import sys
import subprocess  # Library untuk menjalankan perintah terminal (GCC)
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CLexer import CLexer
from CParser import CParser
from CVisitor import CVisitor

# --- Custom Error Listener (Menangkap Pelanggaran Grammar) ---
class StrictCErrorListener(ErrorListener):
    def __init__(self):
        super(StrictCErrorListener, self).__init__()
        self.violations = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Mengubah pesan error teknis menjadi pesan aturan StrictC
        violation = f"Baris {line}:{column} -> "
        
        if "goto" in str(msg) or (offendingSymbol and "goto" in offendingSymbol.text):
            violation += "Penggunaan 'goto' DILARANG keras di StrictC."
        elif "mismatched input" in msg and "{" in msg:
            violation += "Control flow (if/while/for) WAJIB menggunakan kurung kurawal '{}'."
        elif "extraneous input" in msg and "}" in msg:
            violation += "Fungsi atau Blok tidak boleh kosong."
        elif "parameterList" in str(recognizer) or "mismatched input ','" in msg:
             violation += "Jumlah parameter melebihi batas maksimal (Max 5)."
        else:
            # Fallback untuk error lain
            violation += f"Syntax Error: {msg}"
            
        self.violations.append(violation)

# --- Visitor (Menangkap Pelanggaran Logika/Semantik) ---
class DetailedCAnalyzer(CVisitor):
    def __init__(self):
        self.logic_violations = []
        self.function_count = 0

    def get_function_name(self, ctx):
        # Helper untuk mengambil nama fungsi dari parse tree
        decl = ctx.declarator()
        curr = decl.directDeclarator()
        while curr:
            if curr.Identifier():
                return curr.Identifier().getText()
            if curr.declarator():
                curr = curr.declarator().directDeclarator()
            elif curr.directDeclarator():
                curr = curr.directDeclarator()
            else:
                break
        return "UnknownFunction"

    def visitFunctionDefinition(self, ctx):
        self.function_count += 1
        func_name = self.get_function_name(ctx)
        
        # Aturan: Fungsi Maksimal 20 Baris Statement
        body = ctx.compoundStatement()
        line_count = 0
        if body.blockItemList():
            line_count = len(body.blockItemList().blockItem())

        if line_count > 20:
            self.logic_violations.append(
                f"Baris {ctx.start.line}: Fungsi '{func_name}' terlalu panjang ({line_count} baris). Maksimal 20 baris."
            )
        
        return self.visitChildren(ctx)

# --- 3. Fungsi Utama Analisis & Eksekusi ---
def analyze_single_file(file_path):
    print(f"\n>>> Scanning: {file_path}")
    
    try:
        input_stream = FileStream(file_path)
        lexer = CLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CParser(stream)
        
        # A. Pasang Error Listener Khusus StrictC
        parser.removeErrorListeners() # Hapus listener bawaan console
        strict_listener = StrictCErrorListener()
        parser.addErrorListener(strict_listener)
        
        # B. Lakukan Parsing
        tree = None
        try:
            tree = parser.compilationUnit()
        except Exception:
            pass # Error akan ditangkap listener

        # C. Jalankan Visitor (jika parsing menghasilkan tree)
        analyzer = DetailedCAnalyzer()
        if tree:
            analyzer.visit(tree)
        
        # D. Gabungkan Semua Pelanggaran
        all_violations = strict_listener.violations + analyzer.logic_violations
        
        if all_violations:
            # --- JIKA ADA PELANGGARAN ---
            for v in all_violations:
                print(f"    [PELANGGARAN] {v}")
            print(f"\n!!! KOMPILASI DIBATALKAN: Kode tidak memenuhi standar StrictC !!!")
            return False 
        else:
            # --- JIKA BERSIH -> EKSEKUSI ---
            print(f"    [BERSIH] Kode Valid & Aman.")
            
            print(f">>> StrictC mengizinkan eksekusi. Memanggil GCC...")
            
            # Tentukan nama output file executable
            output_name = os.path.splitext(file_path)[0]
            if os.name == 'nt': 
                output_name += ".exe" # Tambah .exe jika di Windows
            
            # 1. Compile menggunakan GCC
            compile_cmd = ["gcc", file_path, "-o", output_name]
            compile_process = subprocess.run(compile_cmd, capture_output=True, text=True)
            
            if compile_process.returncode == 0:
                print(f">>> Kompilasi Sukses! Menjalankan program...\n")
                print("-" * 40)
                
                # 2. Jalankan Program
                run_cmd = f"./{output_name}"
                if os.name == 'nt':
                    run_cmd = output_name
                
                subprocess.run([run_cmd])
                print("\n" + "-" * 40)
            else:
                print(f"Error Internal GCC:\n{compile_process.stderr}")
            
            return True

    except Exception as e:
        print(f"    [SYSTEM ERROR] Gagal memproses file: {e}")
        return False

# --- 4. User Interface ---
def main():
    while True:
        print(f"\n=== StrictC Compiler & Executor ===")
        print("Ketik nama file .c untuk di-scan dan dijalankan.")
        target = input(f"Input File > ")
        
        if target.lower() in ['exit', 'quit', 'b', 'q']:
            print("Sampai jumpa!")
            break
            
        if not os.path.exists(target):
            print(f"File '{target}' tidak ditemukan.")
            continue
            
        analyze_single_file(target)

if __name__ == '__main__':
    main()