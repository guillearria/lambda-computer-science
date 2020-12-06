# Bitwise operations

## Logical bitwise operations
- combine two numbers in binary form to come up with a third number
- treats 1 as true and 0 as the Boolean false

Operation       Boolean Operator     Bitwise Operator
AND                  &&                    &
OR                   ||                    |
NOT                  !                     ~
XOR                  none                  ^
NAND, NOR

### AND
(true and true) --> true
(true and false) --> false

   0b1011
 & 0b0101
 --------
   0b0001

   0b01010110
 & 0b11100011
 ------------
   0b01000010 

### OR
(true OR true) -- > true
(true OR false) --> true

   0b1011
 | 0b0101
 --------
   0b1111

### NOT
~0b10 --> 0b01
~0b1011 --> 0b0100

### XOR "basically the inverse of or"
Also known as exclusive OR

(true XOR true)  --> false
(false XOR false)  --> false
(true XOR false)  --> true

   0b1011
 ^ 0b0101
 --------
   0b1110

   0b0101
 ^ 0b1000
 --------
   0b1101

   0b01010110
 ^ 0b11100011
 ------------
   0b10110101   

### NAND: true, unless both are true
      0b0101
 NAND 0b1000
 -----------
      0b1111

      0b1011
 NAND 0b0101
 -----------
        1110

## Bitwise shifting
### Right bit shifting
vv
10100000 
         |
 0b1010000 >> shift by 1
 0b0101000 >> shift by 2

10100000 >> 6 shifts required to isolate
      10 100000

00000010 # hey it's the number of operands!
Python equivalent: 160 >> 6

### Masking
Shift and use & operation  to essentially delete any higher bits

   0b1010
 & 0b0000  # blocking
   -------
   0b0000 

   0b1010
&  0b0011 # block first two, obtain last two
---------
   0b0010

#### Instruction Layout

Meanings of the bits in the first byte of each instruction: `AABCDDDD`

* `AA` Number of operands for this opcode, 0-2
* `B` 1 if this is an ALU operation
* `C` 1 if this instruction sets the PC
* `DDDD` Instruction identifier

Shift to the right, then mask
  v
10100000 
10100000 >> 5
     101
00000101
   
    00000101
  & 00000001 # is this an ALU operation?
  ----------
    00000001

is_alu_operation = ((IR >> 5) & 0b1) == 1

