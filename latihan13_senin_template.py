HALF = 'HALF'
SINGLE = 'SINGLE'
DOUBLE = 'DOUBLE'

ADD = 'ADD'
SUBTRACT = 'SUBTRACT'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'

def main():
    type_1 = input()
    fp_1 = input()
    type_2 = input()
    fp_2 = input()
    operator = input()

    if type_1 == HALF:
        num_1 = parse_ieee754_half(fp_1)
    elif type_1 == SINGLE:
        pass
    # continue the implementation

def parse_ieee754_half(fp):
    return parse_floating_point(fp, 5, 10, 15)

def parse_ieee754_single(fp):
    return parse_floating_point(fp, 8, 23, 127)

def parse_ieee754_double(fp):
    return parse_floating_point(fp, 11, 52, 1023)

def parse_ieee754(fp, exponent_bit_count, fraction_bit_count, exponent_bias):
    # implement here
    return 0

if __name__ == "__main__":
    main()
