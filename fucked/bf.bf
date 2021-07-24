Brainfuck transpiler to C written in brainfuck ;)
Sadly could not add those fixes I did in python and C
Reads from stdin until EOF (may not work on all devices)
Normally all non instruction characters should
be ignored but did not test

++++++++++[>+++>++++++++++>+++++++++++>++++++++++>
+++++++++++>++++++++++++>++++++++++>++++++++++>+++
>++++++>+++++++++++>++++++++++++>++++++++++>++++++
++++>+++++++++++>+++++>++++++++++>++++++>+<<<<<<<<
<<<<<<<<<<<-]>+++++.>+++++.>.>-.>--.>---.>.>+.>++.
>.>+++++.>----.>.>+++++.>+.>----.>++++.>++.>.[[-]<
]++++++++++[>++++++++++++>+++++++++++>+++++++++++>
++++++++++>++++++++++>+++++++++++>++++++++++>+++++
+++++>+++>++++++++++>++++++++++>++++++++++>+++++++
++++>+++>++++++++++>++++++++++>+++++++++++>+++++++
+++>+++>+++++++++>+++>+++++>+++++>+++++>+++++>++++
+>+++>+++++++++>+++>++++++>+++>++++++++++++>+++>++
+++>+++>++++++++++++>++++++>+<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<-]>---.>.>+++++.>+++++.>+++.>.>+.
>.>++.>-.>++++.>---.>++++.>++.>+++.>---.>-.>+.>++.
>+.>++.>++++.>+++.>+++.>+.>++++.>++.>+++.>++.>+.>+
+.>+++.>++.>--.>++.>+++++.>-.>.[[-]<]++++++++++[>+
+++++++++++>+++++++++++>+++++++++++>++++++++++>+++
+++++++>+++++++++++>++++++++++>++++++++++>+++>++++
++++++>++++++++++>++++++++++>+++++++++++>+++>++++>
+++++++++++>++++++++++++>+++++++++++>+++>++++++>++
+>++++++++++>++++++++++>+++++++++++>++++++++++>+++
+++>+<<<<<<<<<<<<<<<<<<<<<<<<<<<-]>---.>.>+++++.>+
++++.>+++.>.>+.>.>++.>-.>++++.>---.>++++.>++.>++.>
++.>----.>++++.>++.>+.>++.>+++.>---.>-.>+.>-.>.[[-
]<]++++++++++[>++++++++++>+++++++++++>++++++++++++
>+++>+++++++++++>++++++++++>++++++++++>+++++++++++
>+++>++++>+++>++++++++++++>+++++++++++>++++++++++>
++++++++++>+++>++++>+++>++++++++++++>+<<<<<<<<<<<<
<<<<<<<<-]>+++++.>.>----.>++.>-.>---.>+++++.>.>++.
>.>++.>--.>+.>+++++.>.>++.>+.>++.>+++.>.[[-]<]+[,>
[-]>++++++[<+++++++>-]<+[<->-]<>[-]+>[-]<<[-[-[-[>
>[-]++++++++++++++[<<->>-]<<[--[>>[-]>++++[<++++++
+>-]<+[<<->>-]<<[--[>>[-]>++++++++[<------------>-
]<++[<<->>-]<<[>[-]]>[<>>->[-]>]<<>[-]]>[<>>>+++++
+++[>++++>++++>++++++++++++++++>+<<<<-]>.>.>---.>+
+.[[-]<]<<<>[-]>]<<>[-]]>[<>>>++++++++++[>+++>+++>
++++++++++++>++++++++++>++++++++++>+++++++++++>+++
+++++++>+++>++++>+++>++++>+++++++++++>++++++++++++
>+++++++++++>+++>++++>+++>++++++++++++>+<<<<<<<<<<
<<<<<<<<<-]>++.>++.>-.>++++.>+++++.>--.>+.>++.>.>+
+.>++.>++.>----.>++++.>++.>+.>++.>+++.>.[[-]<]<<<>
[-]>]<<>[-]]>[<>>>++++++++++[>+++>+++>++++>++++>++
+++++++++>++++++++++++>+++++++++++>++++++>+<<<<<<<
<<-]>++.>++.>+++.>+++.>++.>----.>++++.>-.>.[[-]<]<
<<>[-]>]<<>[-]]>[<>>>++++++++++[>+++>+++>++++>++++
>+++++++++++>++++++++++++>+++++++++++>++++++>+<<<<
<<<<<-]>++.>++.>+++++.>+++++.>++.>----.>++++.>-.>.
[[-]<]<<<>[-]>]<<>[-]]>[<>>>++++++++++[>+++>+++>++
+++++++++>++++++++++++>++++++++++++>++++++++++>+++
+++++++>++++++++++>+++++++++++>+++>++++>+++>++++>+
++++++++++>++++++++++++>+++++++++++>+++>++++>+++++
+>+<<<<<<<<<<<<<<<<<<<<-]>++.>++.>++.>---.>----.>-
.>++++.>---.>++++.>++.>.>++.>++.>++.>----.>++++.>+
+.>+.>-.>.[[-]<]<<<>[-]>]<<>[-]]>[<>>>++++++++++[>
+++>+++>++++>++++>++++>+++++++++++>++++++++++++>++
+++++++++>++++++>+<<<<<<<<<<-]>++.>++.>+++++.>++++
+.>++.>++.>----.>++++.>-.>.[[-]<]<<<>[-]>]<<>[-]]>
[<>>>++++++++++[>+++>+++>++++>+++++++++++>++++++++
++++>+++++++++++>+++>++++++>+++>++++++++++>+++++++
+++>++++++++++++>++++++++++>++++++++++>++++++++++>
+++++++++++>+++>++++>+++>++++>++++++>+<<<<<<<<<<<<
<<<<<<<<<<-]>++.>++.>++.>++.>----.>++++.>++.>+.>++
.>+++.>+.>----.>-.>++++.>---.>++++.>++.>.>++.>+.>-
.>.[[-]<]<<<>[-]>]<<>[-]]>[<>>>++++++++++[>+++>+++
>++++>++++>++++>+++++++++++>++++++++++++>+++++++++
++>++++++>+<<<<<<<<<<-]>++.>++.>+++.>+++.>++.>++.>
----.>++++.>-.>.[[-]<]<<<>[-]>]<<+][-]++++++++++[>
+++>+++>+++++++++++>++++++++++>++++++++++++>++++++
++++++>+++++++++++>+++++++++++>+++>+++++>++++++>+<
<<<<<<<<<<<-]>++.>++.>++++.>+.>----.>---.>++++.>.>
++.>--.>-.>.[[-]<]+++++++++[>++++++++++++++>+<<-]>
-.>+.[[-]<]
