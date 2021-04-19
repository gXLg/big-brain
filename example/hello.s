// python brainfuck translator //

.data
.bss
.lcomm ARRAY, 65536
.text
.global _start
_start:
ldr x19, =ARRAY
ldrb w20, [x19]
add w20, w20, 10
strb w20, [x19]
cmp w20, 0
beq END_1
START_1:
add x19, x19, 1
ldrb w20, [x19]
add w20, w20, 7
strb w20, [x19]
add x19, x19, 1
ldrb w20, [x19]
add w20, w20, 10
strb w20, [x19]
add x19, x19, 1
ldrb w20, [x19]
add w20, w20, 3
strb w20, [x19]
add x19, x19, 1
ldrb w20, [x19]
add w20, w20, 1
strb w20, [x19]
sub x19, x19, 4
ldrb w20, [x19]
sub w20, w20, 1
strb w20, [x19]
cmp w20, 0
bne START_1
END_1:
add x19, x19, 1
ldrb w20, [x19]
add w20, w20, 2
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
add x19, x19, 1
ldrb w20, [x19]
add w20, w20, 1
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
add w20, w20, 7
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
add w20, w20, 3
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
add x19, x19, 1
ldrb w20, [x19]
add w20, w20, 2
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
sub x19, x19, 2
ldrb w20, [x19]
add w20, w20, 15
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
add x19, x19, 1
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
ldrb w20, [x19]
add w20, w20, 3
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
sub w20, w20, 6
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
sub w20, w20, 8
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
add x19, x19, 1
ldrb w20, [x19]
add w20, w20, 1
strb w20, [x19]
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
add x19, x19, 1
mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0

mov x8, 93
mov x0, 0
svc 0
