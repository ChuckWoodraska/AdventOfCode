def run(program):
    program_counter = 0
    while True:
        op_code = program[program_counter]
        if op_code == 1:
            program[program[program_counter + 3]] = program[program[program_counter + 2]] + program[
                program[program_counter + 1]]
        elif op_code == 2:
            program[program[program_counter + 3]] = program[program[program_counter + 2]] * program[
                program[program_counter + 1]]
        elif op_code == 99:
            return program[0]
        program_counter += 4


def main():
    with open('input.txt', 'r') as f:
        program = [int(item) for item in f.read().split(',')]
        program[1] = 12
        program[2] = 2
        print(run(program))


def main2():
    with open('input.txt', 'r') as f:
        program = [int(item) for item in f.read().split(',')]
        for noun in range(100):
            for verb in range(100):
                temp = program[:]
                temp[1] = noun
                temp[2] = verb
                if run(temp) == 19690720:
                    print(100 * noun + verb)


if __name__ == '__main__':
    main()
