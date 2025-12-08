import sys
from antlr4 import *
from CleanCodeLexer import CleanCodeLexer
from CleanCodeParser import CleanCodeParser
from CleanCodeVisitor import CleanCodeVisitor

# 1. KITA BUAT ANALYZER (VISITOR) SENDIRI
class CleanCodeAnalyzer(CleanCodeVisitor):
    
    def __init__(self):
        self.errors = [] # Menampung daftar kesalahan

    # Helper: Melaporkan error
    def reportError(self, entitas, nama, pesan):
        error_msg = f"[ERROR] {entitas} '{nama}': {pesan}"
        print(error_msg)
        self.errors.append(error_msg)

    #  LOGIKA PENGECEKAN CLASS 
    def visitClassDef(self, ctx):
        # Ambil nama class (Text dari token ID)
        nama_class = ctx.ID().getText()
        
        # Hitung jumlah function
        # ctx.function() mengembalikan list semua function dalam class itu
        jumlah_fungsi = len(ctx.function())
        
        print(f"Menganalisis Class: {nama_class} (Jumlah Fungsi: {jumlah_fungsi})")

        # ATURAN: Class tidak boleh lebih dari 10 function
        if jumlah_fungsi > 10:
            self.reportError("Class", nama_class, f"Terlalu banyak fungsi! ({jumlah_fungsi} > 10)")

        # Lanjutkan kunjungan ke anak-anaknya (masuk ke dalam function)
        return self.visitChildren(ctx)

    # --- LOGIKA PENGECEKAN FUNCTION ---
    def visitFunction(self, ctx):
        nama_fungsi = ctx.ID().getText()
        
        # 1. Hitung Parameter
        # Cek apakah ada paramList?
        param_list = ctx.paramList()
        if param_list:
            # Ambil semua param di dalam list tersebut
            jumlah_param = len(param_list.param())
        else:
            jumlah_param = 0

        # 2. Hitung Line of Code (LoC)
        # ctx.lineOfCode() mengembalikan list semua baris kode
        jumlah_baris = len(ctx.lineOfCode())

        # print(f" -> Cek Fungsi '{nama_fungsi}': Params={jumlah_param}, LoC={jumlah_baris}")

        # ATURAN: Function max 5 parameter
        if jumlah_param > 5:
            self.reportError("Function", nama_fungsi, f"Terlalu banyak parameter ({jumlah_param} > 5). Maksimal 5.")

        # ATURAN: Function max 20 baris
        if jumlah_baris > 20:
            self.reportError("Function", nama_fungsi, f"Terlalu panjang ({jumlah_baris} baris). Maksimal 20.")

        return self.visitChildren(ctx)

# 2. BAGIAN UTAMA (MAIN)
def main():
    # Nama file input
    input_file = "contoh.txt" 
    
    print(f"--- Memulai Analisis Clean Code pada '{input_file}' ---\n")

    # Langkah standar ANTLR untuk membaca file
    input_stream = FileStream(input_file)
    lexer = CleanCodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CleanCodeParser(stream)
    
    # Mulai parsing dari rule awal 'file'
    tree = parser.file_()

    # Jalankan Visitor yang sudah kita buat di atas
    visitor = CleanCodeAnalyzer()
    visitor.visit(tree)

    print("\n--- Analisis Selesai ---")
    if not visitor.errors:
        print("Hasil: CLEAN CODE! Tidak ada pelanggaran ditemukan.")
    else:
        print(f"Hasil: Ditemukan {len(visitor.errors)} pelanggaran.")

if __name__ == '__main__':
    main()