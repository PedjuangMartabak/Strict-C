import glob
import os
import sys
from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from CVisitor import CVisitor

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class DetailedCAnalyzer(CVisitor):
    def __init__(self):
        self.violations = []
        self.function_count = 0
        self.clean_functions = 0

    def add_violation(self, line, col, func_name, message, actual_val, limit_val):
        report = {
            "line": line,
            "col": col,
            "function": func_name,
            "message": message,
            "detail": f"Actual: {actual_val} | Limit: {limit_val}"
        }
        self.violations.append(report)

    def get_function_name(self, ctx):
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

    def count_parameters(self, ctx):
        decl = ctx.declarator()
        curr = decl.directDeclarator()
        while curr:
            if curr.parameterTypeList():
                param_list_ctx = curr.parameterTypeList().parameterList()
                return len(param_list_ctx.parameterDeclaration())
            if curr.directDeclarator():
                curr = curr.directDeclarator()
            else:
                break
        return 0

    def visitFunctionDefinition(self, ctx):
        self.function_count += 1
        start_line = ctx.start.line
        start_col = ctx.start.column
        func_name = self.get_function_name(ctx)
        param_count = self.count_parameters(ctx)
        
        body = ctx.compoundStatement()
        line_count = 0
        if body.blockItemList():
            line_count = len(body.blockItemList().blockItem())

        is_clean = True
        
        if line_count > 20:
            self.add_violation(start_line, start_col, func_name, "Fungsi terlalu panjang", line_count, 20)
            is_clean = False
        if param_count > 5:
            self.add_violation(start_line, start_col, func_name, "Terlalu banyak parameter", param_count, 5)
            is_clean = False
        if line_count == 0:
            self.add_violation(start_line, start_col, func_name, "Fungsi kosong", 0, "> 0")
            is_clean = False

        if is_clean:
            self.clean_functions += 1
        
        return self.visitChildren(ctx)

# --- FUNGSI UTILITY ---

def analyze_single_file(file_path):
    """Menganalisis satu file dan mengembalikan statistik"""
    print(f"\n{Colors.HEADER}>>> Scanning: {file_path}{Colors.ENDC}")
    
    try:
        input_stream = FileStream(file_path)
        lexer = CLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CParser(stream)
        tree = parser.compilationUnit()
        
        analyzer = DetailedCAnalyzer()
        analyzer.visit(tree)
        
        # Tampilkan hasil per file
        if analyzer.violations:
            for v in analyzer.violations:
                print(f"    {Colors.FAIL}[x]{Colors.ENDC} Line {v['line']}: {v['function']} -> {v['message']} ({v['detail']})")
        else:
            print(f"    {Colors.OKGREEN}[v] File Bersih!{Colors.ENDC}")
            
        return analyzer

    except Exception as e:
        print(f"    {Colors.FAIL}[ERROR] Gagal membaca file: {e}{Colors.ENDC}")
        return None

# --- USER INTERFACE (MENU DINAMIS) ---

def print_banner():
    print(f"\n{Colors.OKCYAN}{'='*50}")
    print(f"   CLEAN CODE ANALYZER (INTERACTIVE MODE)")
    print(f"{'='*50}{Colors.ENDC}")

def menu_scan_file():
    while True:
        target = input(f"\n{Colors.BOLD}Masukkan nama file (cth: test.c) atau 'b' untuk kembali: {Colors.ENDC}")
        if target.lower() == 'b':
            break
        
        if not os.path.exists(target):
            print(f"{Colors.FAIL}File '{target}' tidak ditemukan! Coba lagi.{Colors.ENDC}")
            continue
            
        analyzer = analyze_single_file(target)
        if analyzer:
            # Tampilkan Score Singkat
            total = analyzer.function_count
            clean = analyzer.clean_functions
            if total > 0:
                print(f"    --> Health Score: {int((clean/total)*100)}%")

def menu_scan_folder():
    folder = input(f"\n{Colors.BOLD}Masukkan path folder (Enter untuk folder ini): {Colors.ENDC}")
    if folder.strip() == "":
        folder = "."
    
    print(f"Mencari file .c di '{folder}'...")
    list_files = glob.glob(os.path.join(folder, "*.c"))
    
    if not list_files:
        print(f"{Colors.WARNING}Tidak ada file .c di folder tersebut.{Colors.ENDC}")
        return

    total_funcs = 0
    clean_funcs = 0
    
    for f in list_files:
        res = analyze_single_file(f)
        if res:
            total_funcs += res.function_count
            clean_funcs += res.clean_functions
            
    print(f"\n{Colors.HEADER}--- RINGKASAN FOLDER ---{Colors.ENDC}")
    print(f"Total File: {len(list_files)} | Total Fungsi: {total_funcs}")
    if total_funcs > 0:
        score = (clean_funcs/total_funcs)*100
        print(f"Project Health: {score:.2f}%")

def main():
    while True:
        print_banner()
        print("1. Scan File Spesifik")
        print("2. Scan Semua File di Folder")
        print("3. Keluar")
        
        pilihan = input(f"\n{Colors.BOLD}Pilihan Anda (1-3): {Colors.ENDC}")
        
        if pilihan == '1':
            menu_scan_file()
        elif pilihan == '2':
            menu_scan_folder()
        elif pilihan == '3':
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()