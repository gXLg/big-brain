# Big Brain

This repository contains:
* simple C interpreter
* Python3 translator to arm64 asm
* C translator to arm64 asm
* a 'hello world' example

# Example

The file `example/hello.bf` contains brainfuck code.
```bf
++++++++++
[
  >+++++++
  >++++++++++
  >+++
  >+
  <<<<-
]
>++.
>+.
+++++++..
+++.
>++.
<<+++++++++++++++.
>.
+++.
------.
--------.
>+.
>.
```
This is code for printing `Hello World!\n`.

It can be interpreted:
1) Change the constant `f` in `bf.c` to the byte-size of your programm, or just set it to be high enough.
2) Compile `bf.c`.
3) Run.

```
 $ gcc bf.c -o bf
 $ ./bf hello.bf
Hello World!
 $
```

It can be compiled on arm64/aarch64:
1) Translate brainfuck to asm and pipe the result to an output file.
2) Compile the output file to mashine code.
3) Run the result.

Python3 (a bit slower):
```
 $ python3 translator.py hello.bf > hello.s
 $ as hello.s -o hello.o
 $ ld hello.o -o hello
 $ ./hello
Hello World!
 $
```
or

C (faster and compiled):
```
 $ gcc tranlator.c -o translator
 $ ./translator hello.bf > hello.s
 $ as hello.s -o hello.o
 $ ld hello.o -o hello
 $ ./hello
Hello World!
 $
```
