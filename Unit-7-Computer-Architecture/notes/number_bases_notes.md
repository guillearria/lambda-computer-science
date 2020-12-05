# Why different number bases?
  
Commonly used bases?
- binary: base 2
- hexadecimal (aka hex): base 16 
- decimal: base 10
- octal: base 8
  
## BINARY
Alan Turing
John von Neumann

At the hardware level, it's easier to store numbers as a series of 'off' and 'on' data-points. It's also easier to represent voltage in base 2

Binary is useful for:
- yes /no
- true/false
- on/off

Origin: George Boole. Boolean logic. ((true and true) or (false and false)) --> True

Why not base 3? Difficult to use. Later a prototype. zero voltage is 0, medium voltage is 1, high voltage is 2.

## HEX
- Hex is easy to convert to from binary
- Hex is compact (used to print hashes, often)
- Computer memory works in multiples of 8

## DECIMAL
- Easy for humans
- Reading: Arithmetic for Billy Goats
  
## Place-Based Number Systems
- Hindu-Arabic number system vs Roman numerals
- VII * CXLCX = ????, difficult to calculate quickly

### DECIMAL
- Symbols available: 0-9

### BINARY  
0        0 ---> 1 bit
1        1
2       10 
3       11 
4      100  
5      101  
6      110  
7      111 
8     1000   
9     1001   
10    1010
11    1011
12    1100
13    1101
14    1110
15    1111 ---> 4 bits, 1/2 byte, nibble

+------ 8's place
|+----- 4's place
||+---- 2's place
|||+--- 1's place
||||
1010

+------ 8's place
|+----- 4's place
||+---- 2's place
|||+--- 1's place
||||
1000

8 bits = byte
4 bits = 1/2 byte, a nibble

### HEXADECIMAL
6 + 10, we have 10 symbols to work with: 0-9, A-F

0         0
1         1
2         2
3         3
4         4
5         5
6         6
7         7
8         8
9         9
10        A
11        B
12        C
13        D
14        E
15        F
16       10
17       11
18       12
19       13
20       14
21       15
22       16
23       17
24       18
25       19
26       1A
27       1B
28       1C
29       1D
30       1E
31       1F
32       20

### Conversions
0b --> denotes writing in binary, bytes
0d --> denotes writing in decimals
0x --> denotes writing in hex

- 0x1F == 0d31 
- 54 --> hex == 0x36

Rules:
- Decimal to hex: divide by 16, then add back the remainder
- Hex to decimal: multiply the symbol in the 16's place by 16, then add the remainder
  
- ie. 0xE3 to decimal: (E * 16) + 3 = (14 * 16) + 3 = 224 + 3 = 227
- 0b00011010 --> decimal == 26, ie. 0d10 + 0d16 == 0d26
- 43 --> binary == 0b00101011

binary   hex
nibble: 1111 --> F

        F    F
byte: 1111 1111

Binary split into nibbles > hex > decimal is a good route:

ie. 
0101 0101 --> decimal
5    5
0x55 ---> (5 * 16) + 5 == 85

ie.
1110 0110 --> decimal
E    6
0xE6 --> decimal --> (14 * 16) + 6 == 230

ie.
0d73 --> binary
73 --> 0x49 --> 0b01001001
(4 * 16) + 9 = 64
0x49
  4    9
0100  1001

#ff ff ff
 R  G   B
 
#00 00 00

- leading 0s are just to pad out the byte, 0b00000001
- don't change the number
- number bases don't change underlying
- computer represents everything in binary, down deep