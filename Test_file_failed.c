#include <stdio.h>

int hitung_fisika_rumit(int massa, int percepatan, int waktu, int gesekan, int gravitasi, int koreksi_angin) {
    return (massa * percepatan) - (gesekan * waktu) + gravitasi - koreksi_angin;
}

void fitur_masa_depan() {
}

void simulasi_server() {
    int status = 0;
    int memori = 1024;
    int cpu = 50;
    
    printf("Memulai simulasi server...\n");
    printf("Cek memori...\n");
    status += 1;
    memori -= 10;

    if (memori < 100)
        printf("Warning: Low Memory\n");
        
    printf("Loading kernel...\n");
    cpu += 20;
    status += 2;
 
    printf("Loading driver A...\n");
    printf("Loading driver B...\n");
    printf("Loading driver C...\n");
    printf("Loading driver D...\n");
    printf("Loading driver E...\n");
    printf("Loading driver F...\n");
    printf("Loading driver G...\n");
    printf("Loading driver H...\n");
    printf("Loading driver I...\n");
    printf("Loading driver J...\n"); 

    if (status > 10) goto CRITICAL_ERROR;

    printf("Server Siap.\n");
    return;

    CRITICAL_ERROR:
    printf("Server Meledak!\n");
}

int main() {
    printf("Menjalankan Test Fail...\n");
    simulasi_server();
    return 0;
}