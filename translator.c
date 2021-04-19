#include <stdio.h>
#include <string.h>


void assembly ( char cmd, int value ) {
  if ( cmd == '>' )
    printf ( "add x19, x19, %d\n", value );
  else if ( cmd == '<' )
    printf ( "sub x19, x19, %d\n", value );
  else if ( cmd == '+' )
    printf ( "add w20, w20, %d\n"
             "strb w20, [x19]\n", value );
  else if ( cmd == '-' )
    printf ( "sub w20, w20, %d\n"
             "strb w20, [x19]\n", value );
  else if ( cmd == ',' )
    printf ( "mov x8, 63\nmov x0, 0\n"
             "mov x1, x19\nmov x2, 1\nsvc 0\n" );
  else if ( cmd == '.' )
    printf ( "mov x8, 64\nmov x0, 1\n"
             "mov x1, x19\nmov x2, 1\nsvc 0\n" );
  else if ( cmd == '[' )
    printf ( "cmp w20, 0\nbeq END_%d\n"
             "START_%d:\n", value, value );
  else if ( cmd == ']' )
    printf ( "cmp w20, 0\nbne START_%d\n"
             "END_%d:\n", value, value );
}


char file [ 65536 ];


int main ( int argc, char **argv ) {

  FILE *prog;
  if ( ! ( prog = fopen ( argv [ 1 ], "r" ))) {
    fprintf ( stderr, "can't open the file \"%s\".\n", argv [ 1 ]);
    return 2;
  }
  fread ( file, 65536, 1, prog );
  fclose ( prog );
  printf ( "// C brainfuck translator //\n"
           ".data\n"
           ".bss\n"
           ".lcomm ARRAY, 65536\n"
           ".text\n"
           ".global _start\n"
           "_start:\n"
           "ldr x19, =ARRAY\n" );

  char cond [ ] = { 0, 0, 0, 0 };
  char cmds [ ] = "<>+-";
  int loops = 0;
  char loops_ [ 256 ] = { 0 };
  int loaded = 0;

  char current_char;
  char end = '#';
  strncat ( file, &end, 1 );
  for ( int i = 0; file [ i ] != 0; i ++ ) {
    current_char = file [ i ];
    int j = 0;
    for ( int i = 0; i < 4; i ++ )
      if ( cond [ i ]) {
        j = 1;
        break;
      }
    if ( j ) {
      int index;
      int value;
      char cmd;
      for ( int k = 0; k < 4; k ++ )
        if ( cond [ k ]) {
          index = k;
          value = cond [ k ];
          cmd = cmds [ k ];
          break;
        }
      if ( ( current_char != cmd ) &&
           strchr ( "<>+-.,[]", current_char )) {
        if ( ( ! loaded ) && strchr ( "+-", cmd )) {
          printf ( "ldrb w20, [x19]\n" );
          loaded = 1;
        }
        assembly ( cmd, value );
        cond [ index ] = 0;
      }
    }

    if ( strchr ( "[]", current_char )) {
      if ( ! loaded ) {
        printf ( "ldrb w20, [x19]\n" );
        loaded = 1;
      }
    } else if ( strchr ( "<>,", current_char ))
      loaded = 0;

    if ( strchr ( cmds, current_char )) {
      for ( int k = 0; k < 4; k ++ )
        if ( cmds [ k ] == current_char ) {
          cond [ k ] ++;
          break;
        }
    } else if ( strchr ( ",.", current_char ))
      assembly ( current_char, 0 );
    else if ( current_char == '[' ) {
      loops ++;
      int j;
      for ( int k = 0; k < 256; k ++ ) {
        j = k;
        if ( ! loops_ [ k ]) break;
      }
      loops_ [ j ] = loops;
      assembly ( current_char, loops );
    } else if ( current_char == ']' ) {
      int j;
      for ( int k = 0; k < 256; k ++ ) {
        if ( ! loops_ [ k ]) break;
        j = k;
      }
      assembly ( current_char, loops_ [ j ]);
      loops_ [ j ] = 0;
    }
  }
  printf ( "mov x8, 93\nmov x0, 0\n"
           "svc 0\n" );
}
