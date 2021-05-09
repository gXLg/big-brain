import sys

try : file = open ( sys.argv [ 1 ], "r" ).read ( )
except : exit ( "Error opening file" )

file = "".join ([ i for i in file if i in "+-<>[].," ])

x = 0
while len ( file ) != x :
  x = len ( file )
  file = file.replace ( "+-", ""
  ).replace ( "-+", ""
  ).replace ( "<>", ""
  ).replace ( "><", ""
  ).replace ( "+,", ","
  ).replace ( "-,", "" )


def assembly ( cmd, value ) :
  if cmd == ">" :
    return """add x19, x19, %d
""" % value
  elif cmd == "<" :
    return """sub x19, x19, %d
""" % value
  elif cmd == "+" :
    return """add w20, w20, %d
strb w20, [x19]
""" % value
  elif cmd == "-" :
    return """sub w20, w20, %d
strb w20, [x19]
""" % value
  elif cmd == "," :
    return """mov x8, 63
mov x0, 0
mov x1, x19
mov x2, 1
svc 0
"""
  elif cmd == "." :
    return """mov x8, 64
mov x0, 1
mov x1, x19
mov x2, 1
svc 0
"""
  elif cmd == "[" :
    return """cmp w20, 0
beq END_%d
START_%d:
""" % ( value, value )
  elif cmd == "]" :
    return """cmp w20, 0
bne START_%d
END_%d:
""" % ( value, value )

# incptr, decptr, incval, decval
cmds = "><+-"
cond = 0
cmd = ""

loops = 0
loops_ = [ ]
ldr = False
programm = ""
file += "#"

for pos, char in enumerate ( file, 1 ) :

  if cond :
    if char != cmd :
      if not ldr and cmd in "+-" :
        programm += "ldrb w20, [x19]\n"
        ldr = True
      programm += assembly ( cmd, cond )
      cond = 0

  if char in "[]" :
    if not ldr :
      programm += "ldrb w20, [x19]\n"
      ldr = True
  elif char in "<>," :
    ldr = False

  if char in cmds :
    cond += 1
    cmd = char
  elif char in ",." : programm += assembly ( char, 0 )
  elif char == "[" :
    loops += 1
    loops_.append ( loops )
    programm += assembly ( char, loops )
  elif char == "]" :
    programm += assembly ( char, loops_.pop ( ))

init = """
// python brainfuck translator //

.data
.bss
.lcomm ARRAY, 65536
.text
.global _start
_start:
ldr x19, =ARRAY
"""

close = """
mov x8, 93
mov x0, 0
svc 0
"""

print ( init + programm + close )
