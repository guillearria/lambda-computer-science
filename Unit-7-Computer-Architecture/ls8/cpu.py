"""CPU functionality."""
import sys

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010
ADD = 0b10100000
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

        # stack pointer
        self.reg[7] = 0xF4

    def load(self, filename):
        """Load a program into memory."""
        address = 0

        with open(filename) as f:
            for line in f:
                split_line = line.split("#")[0]
                stripped_split_line = split_line.strip()

                if stripped_split_line != "":
                    command = int(stripped_split_line, 2) # convert binary to int
                    self.ram[address] = command
                    address += 1
        
    def ram_read(self, memory_address_register):
        instruction = self.ram[memory_address_register]
        return instruction

    def ram_write(self, memory_address_register, memory_data_register):
        self.ram[memory_address_register] = memory_data_register

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.reg[reg_a] = self.reg[reg_a] + self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == "CMP":
            # set last three register values to zero
            # if values are equal, set Equal (E) flag to 1, otherwise 0
            # elif rA > rB, sett Greater-than (G) flag to 1, otherwise 0
            # elif rA < rB, sett Less-than (L) flag to 1, otherwise 0
            self.reg[-3:] = [0,0,0]

            if self.reg[reg_a] == self.reg[reg_b]:
                self.reg[7] = 1
            elif self.reg[reg_a] > self.reg[reg_b]:
                self.reg[6] = 1
            elif self.reg[reg_a] < self.reg[reg_b]:
                self.reg[5] = 1
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running:
            # read instruction from memory
            instruction_register = self.ram_read(self.pc)

            if instruction_register == LDI: 
                # set the value of a register to an integer
                num_to_save = self.ram_read(self.pc + 2)
                register_address = self.ram_read(self.pc + 1)

                self.reg[register_address] = num_to_save

            elif instruction_register == PRN: 
                # numeric value stored in a register
                register_address = self.ram_read(self.pc + 1)
                saved_num = self.reg[register_address]

                print(saved_num)

            elif instruction_register == PUSH: 
                # push the value in the given register to the stack
                ## decrement stack pointer (SP)
                self.reg[7] -= 1

                # find value in given register
                register_address = self.ram_read(self.pc + 1)
                value = self.reg[register_address]

                # copy value into our stack using SP
                stack_pointer = self.reg[7]
                self.ram[stack_pointer] = value

            elif instruction_register == POP: 
                # pop the value at the top of the stack into the given register
                ## find value in memory from address pointed to by SP
                stack_pointer = self.reg[7]
                value = self.ram[stack_pointer]

                # copy value into register using given register
                register_address = self.ram_read(self.pc + 1)
                self.reg[register_address] = value

                # increment stack pointer
                self.reg[7] += 1

            elif instruction_register == JMP:
                # jump to the address stored in the given register, similar to CALL
                ## get instruction address to jump to using given register
                register_address = self.ram_read(self.pc + 1)
                instruction_address = self.reg[register_address]

                # set PC to new instruction address
                self.pc = instruction_address

            elif instruction_register == CALL:
                # calls a subroutine at the address stored in the register
                ## implement PUSH functionality for instruction index AFTER current
                next_instruction = self.pc + 2

                self.reg[7] -= 1
                stack_pointer = self.reg[7]

                self.ram[stack_pointer] = next_instruction

                # jump to subroutine, set PC to address in register
                register_address = self.ram_read(self.pc + 1)
                subroutine_address = self.reg[register_address]

                self.pc = subroutine_address

            elif instruction_register == RET:
                # return from subroutine
                ## POP value from top of stack
                stack_pointer = self.reg[7]
                value = self.ram[stack_pointer]
                
                # store it as PC
                self.pc = value

                # move stack pointer back up
                self.reg[7] += 1

            elif instruction_register == CMP:
                # compare values in two registers
                reg_a = self.ram_read(self.pc + 1)
                reg_b = self.ram_read(self.pc + 2)

                self.alu("CMP", reg_a, reg_b)

            elif instruction_register == JEQ:
                # if `equal` flag is true, jump to the address stored in the given register
                ## check equal flag, `FL` bits: `00000LGE`
                if self.reg[7]:
                    # get address to jump to in given register
                    register_address = self.ram_read(self.pc + 1)
                    instruction_address = self.reg[register_address]

                    # set PC to new instruction address
                    self.pc = instruction_address

            elif instruction_register == JNE:
                # if `equal` flag is false, jump to the address stored in the given register
                ## check equal flag, `FL` bits: `00000LGE`
                if not self.reg[7]:
                    # get address to jump to in given register
                    register_address = self.ram_read(self.pc + 1)
                    instruction_address = self.reg[register_address]

                    # set PC to new instruction address
                    self.pc = instruction_address

            elif instruction_register == ADD:
                reg_a = self.ram_read(self.pc + 1)
                reg_b = self.ram_read(self.pc + 2)

                self.alu("ADD", reg_a, reg_b)

            elif instruction_register == MUL:
                reg_a = self.ram_read(self.pc + 1)
                reg_b = self.ram_read(self.pc + 2)
                
                self.alu("MUL", reg_a, reg_b)

            elif instruction_register == HLT: 
                # stop running machine
                running = False

            # move to next item in memory
            num_ops = instruction_register >> 6

            # bit shift and mask to isolate the 'C' bit
            sets_pc_directly = ((instruction_register >> 4) & 0b001) == 0b001
            
            if not sets_pc_directly:
                self.pc += (1 + num_ops)
