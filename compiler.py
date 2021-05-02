import sys

try : file = open ( sys.argv [ 1 ], "r" ).read ( )
except : exit ( "Error opening file" )

file = "".join ([ i for i in file if i in "+-<>[].," ])

x = 0
while len ( file ) != x :
  x = len ( file )
  file = file.replace ( "+-", "" )

x = 0
while len ( file ) != x :
  x = len ( file )
  file = file.replace ( "-+", "" )

x = 0
while len ( file ) != x :
  x = len ( file )
  file = file.replace ( "<>", "" )

x = 0
while len ( file ) != x :
  x = len ( file )
  file = file.replace ( "><", "" )

x = 0
while len ( file ) != x :
  x = len ( file )
  file = file.replace ( "+,", "," )

x = 0
while len ( file ) != x :
  x = len ( file )
  file = file.replace ( "-,", "" )


def assembly ( cmd, value ) :
  if cmd == ">" :
    hex_ = 0x91000000
    bin_ = "1001110011"
    val = bin ( value ).split ( "b" ) [ 1 ] + bin_
    val = int ( val, 2 ) + hex_
    val = hex ( val ).split ( "x" ) [ 1 ]
    val = " ".join ( [ val [ i : i + 2 ] for i in [ 6, 4, 2, 0 ]])
    return [ val, 0 ]
  elif cmd == "<" :
    hex_ = 0xd1000000
    bin_ = "1001110011"
    val = bin ( value ).split ( "b" ) [ 1 ] + bin_
    val = int ( val, 2 ) + hex_
    val = hex ( val ).split ( "x" ) [ 1 ]
    val = " ".join ( [ val [ i : i + 2 ] for i in [ 6, 4, 2, 0 ]])
    return [ val, 0 ]
  elif cmd == "+" :
    hex_ = 0x11000000
    bin_ = "1010010100"
    val = bin ( value ).split ( "b" ) [ 1 ] + bin_
    val = int ( val, 2 ) + hex_
    val = hex ( val ).split ( "x" ) [ 1 ]
    val = " ".join ( [ val [ i : i + 2 ] for i in [ 6, 4, 2, 0 ]])
    return [ val + " 74 02 00 39", 0 ]
  elif cmd == "-" :
    hex_ = 0x51000000
    bin_ = "1010010100"
    val = bin ( value ).split ( "b" ) [ 1 ] + bin_
    val = int ( val, 2 ) + hex_
    val = hex ( val ).split ( "x" ) [ 1 ]
    val = " ".join ( [ val [ i : i + 2 ] for i in [ 6, 4, 2, 0 ]])
    return [ val + " 74 02 00 39", 0 ]
  elif cmd == "," :
    return [ """
e8 07 80 d2
00 00 80 d2
e1 03 13 aa
22 00 80 d2
01 00 00 d4
""", 0 ]
  elif cmd == "." :
    return [ """
08 08 80 d2
20 00 80 d2
e1 03 13 aa
22 00 80 d2
01 00 00 d4
""", 0 ]
  elif cmd == "[" :
    return [ "9f 02 00 71", "(" ]
  elif cmd == "]" :
    return [ "9f 02 00 71", ")" ]

# incptr, decptr, incval, decval
cmds = "><+-"
cond = 0
cmd = ""

loops = 0
loops_ = [ ]
ldr = False
programm = [ ]
file += "#"

for pos, char in enumerate ( file, 1 ) :

  if cond :
    if char != cmd :
      if not ldr and cmd in "+-" :
        programm.append ( [ "74 02 40 39", 0 ])
        ldr = True
      programm.append ( assembly ( cmd, cond ))
      cond = 0

  if char in "[]" :
    if not ldr :
      programm.append ( [ "74 02 40 39", 0 ])
      ldr = True
  elif char in "<>," :
    ldr = False

  if char in cmds :
    cond += 1
    cmd = char
  elif char in ",." : programm.append ( assembly ( char, 0 ))
  elif char == "[" :
    loops += 1
    loops_.append ( loops )
    programm.append ( assembly ( char, loops ))
  elif char == "]" :
    programm.append ( assembly ( char, loops_.pop ( )))

binary = ""
for ii, i in enumerate ( programm ) :
  if i [ 1 ] == 0 : binary += i [ 0 ].replace ( "\n", "" ).replace ( " ", "" )
  elif i [ 1 ] == "(" :
    jump_len = 2
    loop = 0
    for j in range ( ii + 1, len ( programm )) :
      if programm [ j ] [ 1 ] == 0 : jump_len += \
        len ( programm [ j ] [ 0 ].replace ( "\n", "" ).replace ( " ", "" )) // 8
      elif programm [ j ] [ 1 ] == "(" :
        jump_len += 2
        loop += 1
      elif programm [ j ] [ 1 ] == ")" :
        if loop :
          jump_len += 2
          loop -= 1
        else :
          jump_len += 1
          hex_ = 0x54000000
          bin_ = "00000"
          val = bin ( jump_len ).split ( "b" ) [ 1 ] + bin_
          val = int ( val, 2 ) + hex_
          val = hex ( val ).split ( "x" ) [ 1 ]
          val = "".join ( [ val [ k : k + 2 ] for k in [ 6, 4, 2, 0 ]])
          binary += i [ 0 ].replace ( "\n", "" ).replace ( " ", "" )
          binary += val

          hex_ = 0x54000000
          bin_ = "00001"
          val = bin ( 0b10000000000000000010 - jump_len ).split ( "b" ) [ 1 ] + bin_
          val = int ( val, 2 ) + hex_
          val = hex ( val ).split ( "x" ) [ 1 ]
          val = "".join ( [ val [ k : k + 2 ] for k in [ 6, 4, 2, 0 ]])
          programm [ j ] [ 1 ] = val
          break
  else :
    binary += i [ 0 ].replace ( "\n", "" ).replace ( " ", "" )
    binary += i [ 1 ]


close = "a8 0b 80 d2 00 00 80 d2 01 00 00 d4".replace ( "\n", "" ).replace ( " ", "" )

binary += close

if not ( ( len ( binary ) // 8 ) % 2 ) :
  binary += "00000000"
code_len = len ( binary ) // 2 - 4

print ( binary )


header = """
7f 45 4c 46
02 01
01 00 00 00
00 00 00 00 00 00
02 00
b7 00
01 00 00 00
b0 00 40 00
00 00 00 00
40 00 00 00
00 00 00 00
"""

hex_ = 0x1000000d8
val = code_len + hex_
val = hex ( val ).split ( "x1" ) [ 1 ]
header += "".join ( [ val [ i : i + 2 ] for i in [ 6, 4, 2, 0 ]])

hex_ = 0x100d8 - 24
val = code_len + hex_
val = hex ( val ).split ( "x1" ) [ 1 ]
section = "".join ( [ val [ i : i + 2 ] for i in [ 2, 0 ]])


header += """
00 00 00 00

00 00 00 00


40 00

38 00
02 00

40 00
04 00

03 00

01 00 00 00 05 00 00 00
00 00 00 00 00 00 00 00
00 00 40 00 00 00 00 00
00 00 40 00 00 00 00 00
"""

header += section

header += "00 00 00 00 00 00"

header += section

header += """
00 00 00 00 00 00 00
00 01 00 00 00 00 00 01
00 00 00 06 00 00 00
"""

header += section

header += "00 00 00 00 00 00"

header += section

header += "41 00 00 00 00 00"

header += section

header += """
41 00 00 00 00 00 00 00 00
00 00 00 00 00 30 75 00
00 00 00 00 00 00 00 01
00 00 00 00 00
"""


# number of octets
hex_ = 0x58000000
bin_ = "10011"
val = bin ( code_len // 4 + 2 ).split ( "b" ) [ 1 ] + bin_
val = int ( val, 2 ) + hex_
val = hex ( val ).split ( "x" ) [ 1 ]
val = " ".join ( [ val [ i : i + 2 ] for i in [ 6, 4, 2, 0 ]])
header += val
# code

binary = header + binary

binary += section

binary += """
41 00 00 00 00 00 00
2e 73 68 73 74 72 74 61 62 00
2e 74 65 78 74 00
2e 62 73 73 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 0b 00 00 00
01 00 00 00 06 00 00 00 00 00 00 00 b0 00
40 00 00 00 00 00 b0 00 00 00 00 00 00 00
"""

hex_ = 0x10010
val = code_len + hex_
val = hex ( val ).split ( "x1" ) [ 1 ]
binary += "".join ( [ val [ i : i + 2 ] for i in [ 2, 0 ]])
print(code_len)

binary += """
00 00 00 00 00 00 00 00 00 00 00 00
00 00 08 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 11 00 00 00 08 00 00 00 03 00
00 00 00 00 00 00
"""

binary += section

binary += "41 00 00 00 00 00"

binary += section

binary += """
00 00 00 00 00 00 30 75 00 00 00 00 00
00 00 00 00 00 00 00 00 00 08 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 01 00 00
00 03 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00
"""

binary += section

binary += """
00 00 00 00 00 00 16 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 01 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00
"""

binary = binary.replace ( "\n", "" ).replace ( " ", "" )

f = open ( "a.out", "wb" )
f.write ( bytearray.fromhex ( binary ))
f.close ( )
