
def read_input_file(day: int):
    with open(f'input/day{day}.txt') as f:
        return f.read()


def lines(day: int):
    return read_input_file(day).splitlines()

def intmap(arr):
   return list(map(int, arr))
