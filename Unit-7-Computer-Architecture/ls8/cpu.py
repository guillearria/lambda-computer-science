"""CPU functionality."""
import sys

LDI = 0b10000010  # LDI x, y
PRN = 0b01000111  # PRN x
HLT = 0b00000001  # HLT


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = []
        self.reg = [0]*8
        self.pc = 0

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
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
                num = int(self.reg[self.pc + 1])
                
                print(num)
                self.pc += 1

            elif instruction_register == HLT: # stop running machine
                running = False

            # move to next item in memory
            self.pc += 1
