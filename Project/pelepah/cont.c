#include <stdio.h>

/* PELANGGARAN 1: Parameter Terlalu Banyak
   Aturan: Maksimal 5 parameter.
   Di sini ada 7 parameter (a, b, c, d, e, f, g).
*/
void fungsiRibet(int a, int b, int c, int d, int e, int f, int g) {
    printf("Fungsi ini parameternya kebanyakan!");
}

/* PELANGGARAN 2: Fungsi Terlalu Panjang
   Aturan: Maksimal 20 baris statement.
   Di sini saya buat > 20 baris assignment.
*/
void fungsiPanjang() {
    int total = 0;
    
    // Baris 1-25 (Melanggar batas 20)
    total += 1;
    total += 2;
    total += 3;
    total += 4;
    total += 5;
    total += 6;
    total += 7;
    total += 8;
    total += 9;
    total += 10;
    total += 11;
    total += 12;
    total += 13;
    total += 14;
    total += 15;
    total += 16;
    total += 17;
    total += 18;
    total += 19;
    total += 20;
    total += 21; // <-- Mulai dari sini sudah Violation
    total += 22;
    
    printf("Total: %d", total);
}

/* PELANGGARAN 3: Fungsi Kosong
   Aturan: Fungsi harus punya isi (body).
*/
void fungsiHantu() {
    // Tidak ada kode apa-apa di sini
}