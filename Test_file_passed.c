#include <stdio.h>
#include <string.h>

typedef struct {
    char nama[50];
    int nilai_tugas;
    int nilai_uts;
    int nilai_uas;
    int absensi;
} Mahasiswa;

float hitung_rata_rata(int a, int b, int c) {
    return (a + b + c) / 3.0;
}

void cetak_status(float nilai_akhir) {

    if (nilai_akhir >= 60.0) {
        printf("Status: LULUS\n");
    } else {
        printf("Status: TIDAK LULUS\n");
    }
}

void proses_nilai(Mahasiswa m) {
    float rata_rata = hitung_rata_rata(m.nilai_tugas, m.nilai_uts, m.nilai_uas);
    
    printf("---------------------------\n");
    printf("Nama: %s\n", m.nama);
    printf("Nilai Akhir: %.2f\n", rata_rata);
    
    if (m.absensi < 75) {
        printf("Peringatan: Absensi Kurang!\n");
        printf("Status: DITAHAN (Absensi)\n");
    } else {
        cetak_status(rata_rata);
    }
}

int main() {
    Mahasiswa m1;
    strcpy(m1.nama, "Budi Santoso");
    m1.nilai_tugas = 80;
    m1.nilai_uts = 75;
    m1.nilai_uas = 85;
    m1.absensi = 90;

    printf("=== SISTEM AKADEMIK STRICT-C ===\n");
    proses_nilai(m1);
    
    return 0;
}