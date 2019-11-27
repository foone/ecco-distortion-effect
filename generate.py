SCREEN_HEIGHT = 224

# based on the code at 0x066c84 in Ecco the Dolphin (USA, Europe).md

# This is based on the table at 32F8 in the ROM, preprocessed through the following:
# RAM_TABLE is based on the ram dump at 0x00FFF190
# D2 = RAM_TABLE[i] 
# D2=(0xFF00 if D2 & 128 else 0x0000) | D2
# D2-= 0x40
# D2= (D2>>1) | (0x8000 if D2 else 0)
# D2= (-D2)&0xFFFF

SCREEN_SHIFTS = [
	55, 20, 59, 42, 51, 18, 5, 1, 0, 64, 33, 10, 3, 64, 35, 54, 45, 14, 4, 63,
	28, 56, 44, 14, 4, 1, 64, 35, 11, 62, 39, 52, 47, 16, 60, 41, 51, 18, 5,
	63, 36, 11, 62, 26, 8, 2, 64, 35, 54, 19, 59, 24, 7, 62, 38, 12, 3, 63,
	28, 8, 2, 64, 30, 9, 62, 38, 12, 3, 1, 64, 30, 56, 44, 51, 47, 15, 60, 24,
	7, 62, 27, 57, 21, 6, 2, 1, 0, 0, 0, 0, 64, 31, 55, 44, 51, 18, 5, 63, 28,
	8, 2, 64, 30, 9, 3, 1, 64, 31, 55, 44, 14, 61, 39, 53, 46, 49, 17, 5, 1, 1,
	0, 64, 31, 9, 62, 27, 56, 44, 50, 17, 60, 41, 52, 19, 59, 23, 7, 63, 28, 8,
	62, 38, 53, 46, 49, 48, 16, 5, 63, 28, 8, 2, 64, 35, 54, 44, 14, 60, 40,
	52, 46, 15, 60, 40, 13, 3, 63, 29, 9, 62, 38, 12, 3, 1, 64, 30, 56, 21, 58,
	22, 6, 63, 28, 8, 62, 26, 57, 21, 58, 22, 6, 63, 37, 11, 3, 1, 0, 64, 33,
	10, 3, 64, 35, 54, 19, 6, 63, 37, 11, 61, 39, 13, 4, 1, 64, 30, 9, 62, 27,
	8, 62, 26, 8, 62, 38, 11, 62, 38, 12, 3, 1, 0, 0, 0, 0, 64, 32, 55, 20, 6,
	63, 37, 53, 45, 14, 4, 63, 28, 9, 62, 38, 53, 46, 49, 48, 16
]

def generate_for_offset(offset):
	output_shifts = [0]*SCREEN_HEIGHT
	for current_line in range(SCREEN_HEIGHT):
		output_shifts[current_line] = SCREEN_SHIFTS[(current_line+offset) & 0xFF]
	return output_shifts

