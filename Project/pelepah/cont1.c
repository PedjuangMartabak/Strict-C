#include <stdio.h>

/* BENAR: Parameter Sedikit
   Hanya 2 parameter. Lolos aturan (Max 5).
*/
int tambah(int a, int b) {
    return a + b;
}

/* BENAR: Fungsi Pendek & Padat
   Hanya sekitar 4 baris kode. Lolos aturan (Max 20).
   Fungsi panjang sebaiknya dipecah menjadi fungsi-fungsi kecil.
*/
void hitungCepat() {
    int x = 10;
    int y = 20;
    int hasil = tambah(x, y);
    printf("Hasil: %d", hasil);
}

/* BENAR: Fungsi Tidak Kosong
   Minimal ada satu statement (return atau print).
*/
void fungsiValid() {
    return; 
}