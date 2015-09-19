from ctypes import c_uint32
opcodes = dict({
				"add": 			0b00000000000000000000000000100000,
				"addu": 		0b00000000000000000000000000100001,
				"addi": 		0b00100000000000000000000000000000,
				"addiu": 		0b00100100000000000000000000000000,
				"and": 			0b00000000000000000000000000100100,
				"andi": 		0b00110000000000000000000000000000,
				"beq": 			0b00010000000000000000000000000000,
				"beql": 		0b01010000000000000000000000000000,
				"bgez": 		0b00000100000000000000000000000000,
				"bgezal": 		0b00000100000100010000000000000000,
				"bgezall": 		0b00000100000100110000000000000000,
				"bgezl": 		0b00000100000001110000000000000000,
				"bgtz": 		0b00011100000000000000000000000000,
				"bgtzl": 		0b01011100000000000000000000000000,
				"blez": 		0b00011000000000000000000000000000,
				"blezl": 		0b01011000000000000000000000000000,
				"bltz": 		0b00000100000000000000000000000000,
				"bltzal": 		0b00000100000100000000000000000000,
				"bltzall":		0b00000100000100100000000000000000,
				"bltzl": 		0b00000100000000100000000000000000,
				"bne": 			0b00010100000000000000000000000000,
				"bnel": 		0b01010100000000000000000000000000,
				"break": 		0b00000000000000000000000000001101,
				"cop0": 		0b01000000000000000000000000000000,
				"cop1": 		0b01000100000000000000000000000000,
				"cop2": 		0b01001000000000000000000000000000,
				"cop3": 		0b01001100000000000000000000000000,
				"dadd": 		0b00000000000000000000000000101100,
				"daddi": 		0b01100000000000000000000000000000,
				"daddiu": 		0b01100100000000000000000000000000,
				"daddu": 		0b00000000000000000000000000101101,
				"ddv": 			0b00000000000000000000000000011110,
				"ddvu": 		0b00000000000000000000000000011111,
				"div": 			0b00000000000000000000000000011010,
				"divu": 		0b00000000000000000000000000011011,
				"dmult": 		0b00000000000000000000000000011100,
				"dmultu": 		0b00000000000000000000000000011101,
				"dsll": 		0b00000000000000000000000000111000,
				"dsll32": 		0b00000000000000000000000000111100,
				"dsllv":		0b00000000000000000000000000010100,
				"dsra":			0b00000000000000000000000000111011,
				"dsra32":		0b00000000000000000000000000111111,
				"dsra32":		0b00000000000000000000000000010111,
				"dsrl":			0b00000000000000000000000000111010,
				"dsrl32":		0b00000000000000000000000000111110,
				"dsrlv":		0b00000000000000000000000000010110,
				"dsub": 		0b00000000000000000000000000101110,
				"dsubu":		0b00000000000000000000000000101111,
				"j":			0b00001000000000000000000000000000,
				"jal":			0b00001100000000000000000000000000,
				"jalr":			0b00000000000000000000000000001001,
				"jr":			0b00000000000000000000000000001000,
				"lb":			0b10000000000000000000000000000000,
				"lbu":			0b10010000000000000000000000000000,
				"ld":			0b11011100000000000000000000000000,
				"ldc1":			0b11010100000000000000000000000000,
				"ldc2":			0b11011000000000000000000000000000,
				"ldl":			0b01101000000000000000000000000000,
				"ldr":			0b01101100000000000000000000000000,
				"lh":			0b10000100000000000000000000000000,
				"lhu":			0b10010100000000000000000000000000,
				"ll":			0b11000000000000000000000000000000,
				"lld":			0b11010000000000000000000000000000,
				"lui":			0b00111100000000000000000000000000,
				"lw":			0b10001100000000000000000000000000,
				"lwc1":			0b11000100000000000000000000000000,
				"lwc2":			0b11001000000000000000000000000000,
				"lwc3":			0b11001100000000000000000000000000,
				"lwl":			0b10001000000000000000000000000000,
				"lwr":			0b10011000000000000000000000000000,
				"lwu":			0b10011100000000000000000000000000,
				"mfhi":			0b00000000000000000000000000010000,
				"mflo":			0b00000000000000000000000000010010,
				"movn":			0b00000000000000000000000000001011,
				"movz":			0b00000000000000000000000000001010,
				"mthi":			0b00000000000000000000000000010001,
				"mtlo":			0b00000000000000000000000000010011,
				"mult":			0b00000000000000000000000000011000,
				"multu":		0b00000000000000000000000000011001,
				"nor":			0b00000000000000000000000000100111,
				"or":			0b00000000000000000000000000100101,
				"ori":			0b00110100000000000000000000000000,
				"pref":			0b11001100000000000000000000000000,
				"sb":			0b10100000000000000000000000000000,
				"sc":			0b11100000000000000000000000000000,
				"scd":			0b11110000000000000000000000000000,
				"sd":			0b11111100000000000000000000000000,
				"sdc1":			0b11110100000000000000000000000000,
				"sdc2":			0b11111000000000000000000000000000,
				"sdl":			0b10110000000000000000000000000000,
				"sdr":			0b10110100000000000000000000000000,
				"sh":			0b10100100000000000000000000000000,
				"sll":			0b00000000000000000000000000000000,
				"sllv":			0b00000000000000000000000000000100,
				"slt":			0b00000000000000000000000000101010,
				"slti":			0b00101000000000000000000000000000,
				"sltiu":		0b00101100000000000000000000000000,
				"sltu":			0b00000000000000000000000000101011,
				"sra": 			0b00000000000000000000000000000011,
				"srav": 		0b00000000000000000000000000000111,
				"srl": 			0b00000000000000000000000000000010,
				"srlv": 		0b00000000000000000000000000000110,
				"sub": 			0b00000000000000000000000000100010,
				"subu": 		0b00000000000000000000000000100011,
				"sw": 			0b10101100000000000000000000000000,
				"swc1": 		0b11100100000000000000000000000000,
				"swc2": 		0b11101000000000000000000000000000,
				"swc3": 		0b11101100000000000000000000000000,
				"swl": 			0b10101000000000000000000000000000,
				"swr": 			0b10111000000000000000000000000000,
				"sync": 		0b00000000000000000000000000001111,
				"syscall": 		0b00000000000000000000000000001100,
				"teq": 			0b00000000000000000000000000110100,
				"teqi": 		0b00000100000011000000000000000000,
				"tge": 			0b00000000000000000000000000110000,
				"tgei": 		0b00000100000010000000000000000000,
				"tgeiu": 		0b00000100000010010000000000000000,
				"tgeu": 		0b00000000000000000000000000110001,
				"tlt": 			0b00000000000000000000000000110010,
				"tlti": 		0b00000100000010100000000000000000,
				"tltiu": 		0b00000100000010110000000000000000,
				"tltu": 		0b00000000000000000000000000110011,
				"tne": 			0b00000000000000000000000000110110,
				"tnei": 		0b00000100000011100000000000000000,
				"xor": 			0b00000000000000000000000000100110,
				"xori": 		0b00111000000000000000000000000000,
			  })
