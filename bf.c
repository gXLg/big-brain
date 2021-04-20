#include <stdio.h>                                                                                                                                      const size_t f = 65536;                                                                                                                                 unsigned char game [ 2048 ] = { 0 };                                        unsigned char *ptr = game;
char file [ f ];

int main ( int argc, char **argv ) {
  FILE *prog;
  if ( ! ( prog = fopen ( argv [ 1 ], "r" ))) {
    fprintf ( stderr, "can't open the file \"%s\".\n", argv [ 1 ]);
    return 2;
  }
  fread ( file, f, 1, prog );
  fclose ( prog );

  char current_char;
  size_t i;
  size_t loop;

  for ( i = 0; file [ i ] != 0; i ++ ) {
    current_char = file [ i ];
    if ( current_char == '>' ) ++ ptr;
    else if ( current_char == '<' ) -- ptr;
    else if ( current_char == '+' ) ++ *ptr;
    else if ( current_char == '-' ) -- *ptr;
    else if ( current_char == '.' ) putchar ( *ptr );
    else if ( current_char == ',' ) *ptr = getchar ( );
    else if ( current_char == '[' && ! *ptr ) {
      loop = 1;
      while ( loop > 0 ) {
        current_char = file [ ++ i ];
        if ( current_char == ']' ) loop --;
        else if ( current_char == '[' ) loop ++;
      }
    } else if ( current_char == ']' && *ptr ) {
      loop = 1;
      while ( loop > 0 ) {
        current_char = file [ -- i ];
        if ( current_char == '[' ) loop --;
        else if ( current_char == ']' ) loop ++;
      }
    }
  }
}
