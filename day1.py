import utils


def part_1():
    lines = utils.lines(1)
    last = lines[0]
    increment = 0
    for i in lines[1:]:
        if int(i) > int(last):
            increment += 1
        last = i
    print(increment)


def part_2():
    f = utils.read_input_file(1)
    lines = list(map(int, f.splitlines()))
    last = 99999
    increment = 0
    for i, val in enumerate(lines[:-2]):
        val = sum(lines[i:i+3])
        if val > last:
            increment += 1
        last = val
    print(increment)


print("part 1: ")
part_1()

print("part 2: ")
part_2()

