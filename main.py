import os
import sys
import subprocess  # Library untuk menjalankan perintah terminal (GCC)
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from ANTLR.CLexer import CLexer
from ANTLR.CParser import CParser
from ANTLR.CVisitor import CVisitor

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
        elif "missing '{'" in msg:
            violation += "Blok kode (if/while/for/fungsi) WAJIB menggunakan kurung kurawal '{}'."
        elif "missing ';'" in msg and "'{'" in msg:
            violation += "Kurang titik koma ';' sebelum blok kode, atau format header fungsi salah."
        elif "extraneous input" in msg and "}" in msg:
            violation += "Fungsi atau Blok tidak boleh kosong."
        elif "parameterList" in str(recognizer) or "mismatched input ','" in msg:
             violation += "Jumlah parameter melebihi batas maksimal (Max 5)."
        elif offendingSymbol and offendingSymbol.text == "<EOF>":
             violation += "Akhir file tidak terduga. Kemungkinan ada kurung kurawal '}' yang kurang atau error sintaks sebelumnya merusak struktur parsing."
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
        
        # Aturan: Fungsi Maksimal 50 Baris Statement
        body = ctx.compoundStatement()
        line_count = 0
        if body.blockItemList():
            line_count = len(body.blockItemList().blockItem())

        if line_count > 50:
            self.logic_violations.append(
                f"Baris {ctx.start.line}: Fungsi '{func_name}' terlalu panjang ({line_count} baris). Maksimal 50 baris."
            )
        
        return self.visitChildren(ctx)

# --- 3. Fungsi Utama Analisis & Eksekusi ---
def analyze_file(file_path):
    print(f"\n>>> Scanning: {file_path}")
    
    try:
        input_stream = FileStream(file_path)
        lexer = CLexer(input_stream)
        lexer.removeErrorListeners() # Hapus listener bawaan Lexer (menghilangkan noise token error)
        
        stream = CommonTokenStream(lexer)
        parser = CParser(stream)
        
        # A. Pasang Error Listener Khusus StrictC
        parser.removeErrorListeners()
        strict_listener = StrictCErrorListener()
        
        parser.addErrorListener(strict_listener)
        lexer.addErrorListener(strict_listener)
        
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
            return False 
        else:
            # --- JIKA BERSIH ---
            print(f"    [BERSIH] Kode Valid & Aman.")
            return True

    except Exception as e:
        print(f"    [SYSTEM ERROR] Gagal memproses file: {e}")
        return False

def compile_and_run(source_files):
    print(f"\n>>> StrictC mengizinkan eksekusi. Memanggil GCC...")
    
    # Tentukan nama output file executable (menggunakan nama file pertama)
    output_name = os.path.splitext(source_files[0])[0]
    if os.name == 'nt': 
        output_name += ".exe" # Tambah .exe jika di Windows
    
    # 1. Compile menggunakan GCC (support multiple source files)
    compile_cmd = ["gcc"] + source_files + ["-o", output_name]
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

# --- 4. User Interface ---
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_or_directory> ...")
        sys.exit(1)

    targets = sys.argv[1:]
    files_to_process = []
    all_valid = True

    # 1. Kumpulkan semua file target (support direktori rekursif)
    for target in targets:
        if os.path.isdir(target):
            for root, _, files in os.walk(target):
                for file in files:
                    if file.endswith(".c") or file.endswith(".h"):
                        files_to_process.append(os.path.join(root, file))
        elif os.path.isfile(target):
            files_to_process.append(target)
        else:
            print(f"Target '{target}' tidak ditemukan.")
            all_valid = False

    if not all_valid:
        sys.exit(1)

    if not files_to_process:
        print("Tidak ada file .c atau .h yang ditemukan.")
        return

    source_files = []

    # 2. Proses setiap file yang ditemukan
    for file_path in files_to_process:
        # Kumpulkan file .c untuk kompilasi
        if file_path.endswith(".c"):
            source_files.append(file_path)
            
        # Analisis setiap file (baik .c maupun .h)
        if not analyze_file(file_path):
            all_valid = False

    if all_valid:
        if source_files:
            compile_and_run(source_files)
        else:
            print(f"\n>>> Analisis Selesai. Tidak ada file source (.c) untuk dijalankan.")
    else:
        print(f"\n!!! KOMPILASI DIBATALKAN: Kode tidak memenuhi standar StrictC !!!")

if __name__ == '__main__':
    main()
