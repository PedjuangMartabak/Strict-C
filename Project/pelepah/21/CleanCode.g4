grammar CleanCode;

//Parsing Rules (Struktur)

// Root: File berisi sekumpulan Class
file: classDef* EOF;

// Class: Punya nama dan berisi banyak fungsi
classDef: 'class' ID '{' function* '}';

// Function: Punya nama, parameter, dan baris kode
function: 'def' ID '(' paramList? ')' '{' lineOfCode* '}';

// Parameter List: param1, param2, dst
paramList: param (',' param)*;
param: type ID;

// LineOfCode: Kita anggap setiap perintah yang diakhiri titik koma (;)
lineOfCode: statement ';';

// Statement sederhana (Assignment atau Function Call)
statement: ID '=' expr        # assignment
         | ID '(' args? ')'   # funcCall
         | 'return' expr?     # returnStmt
         ;

// Lexical Rules (Kata-kata dasar)
type : 'int' | 'string' | 'void' | ID ;
args : expr (',' expr)* ;
expr : ID | INT | STRING ;

ID   : [a-zA-Z_][a-zA-Z0-9_]* ;  // Nama variable/class
INT  : [0-9]+ ;                  // Angka
STRING : '"' .*? '"' ;           // Teks
WS   : [ \t\r\n]+ -> skip ;      // Abaikan spasi/enter