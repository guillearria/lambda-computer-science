"""CPU functionality."""
import sys

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010
ADD = 0b10100000
PUSH = 0b01000111
POP = 0b01001000


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
            self.reg[reg_a] += self.reg[reg_b]
        if op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
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
                # push value in given register on the stack
                # decrement stack pointer (SP)
                self.reg[7] -= 1

                # copy value in given register to address pointed by SP
                register_address = self.ram_read(self.pc + 1)
                value = self.reg[register_address]

                # copy value into our memory using SP
                stack_pointer = self.reg[7]
                self.ram[stack_pointer] = value

            elif instruction_register == POP: 
                # copy value from address pointed to by SP to given register
                stack_pointer = self.reg[7]
                value = self.ram[stack_pointer]

                # find target register address
                register_address = self.ram_read(self.pc + 1)

                # place value in that register
                self.reg[register_address] = value

                # increment stack pointer
                self.reg[7] += 1

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
            self.pc += (1 + num_ops)
