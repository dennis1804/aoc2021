import utils



def part_1():
    lines = utils.lines(2)
    h = 0
    d = 0

    positive = ["forward", "down"]
    negative = ["up"]
    hMod = ["forward"]
    dMod = ["down", "up"]

    for l in lines:
        line = l.split()
        mod = int(line[1])
        if line[0] in negative:
            mod = mod * -1
        if line[0] in hMod:
            h= h+mod
        elif line[0] in dMod:
            d= d+mod
    print(h * d)


def part_2():
    lines = utils.lines(2)
    h = 0
    d = 0
    a = 0

    positive = ["forward", "down"]
    negative = ["up"]
    hMod = ["forward"]
    dMod = ["down", "up"]

    for l in lines:
        line = l.split()
        mod = int(line[1])
        if line[0] in negative:
            mod = mod * -1
        if line[0] in hMod:
            h= h+mod
            d = d + ( mod*a )
        elif line[0] in dMod:
            a = a+mod
    print(h * d)



print("part 1: ")
part_1()

print("part 2: ")
part_2()

