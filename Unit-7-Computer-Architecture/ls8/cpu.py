"""CPU functionality."""
import sys

LDI = 0b10000010  # LDI x, y
PRN = 0b01000111  # PRN x
HLT = 0b00000001  # HLT


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

    def load(self, filename):
        """Load a program into memory."""
        address = 0

        with open(filename) as f:
            for line in f:
                split_line = line.split("#")[0]
                stripped_split_line = split_line.strip()

                if stripped_split_line != "":
                    command = int(stripped_split_line, 2)
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
        # elif op == "SUB": etc
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

            if instruction_register == LDI: # set the value of a register to an integer
                num = int(self.ram_read(self.pc + 2))
                register_id = int(self.ram_read(self.pc + 1))

                self.reg[register_id] = num
                self.pc += 2

            elif instruction_register == PRN: # numeric value stored in a register
                register_id = self.ram_read(self.pc + 1)
                num = int(self.reg[register_id])
                
                print(num)
                self.pc += 1

            elif instruction_register == HLT: # stop running machine
                running = False

            # move to next item in memory
            self.pc += 1
