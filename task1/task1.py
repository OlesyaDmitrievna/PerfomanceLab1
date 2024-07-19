import sys

def find_circular_path(n, m):
    circular_array = list(range(1, n + 1))
    current_index = 0
    next_index = 3
    path = []

    while circular_array[next_index] != 1:
        next_index = (current_index + m - 1) % n
        path.append(circular_array[current_index])
        current_index = next_index
    return path

def cut_numbers(input_str):
    numbers = input_str.split()

    if len(numbers) == 2:
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        return num1, num2


if len(sys.argv) != 3:
    print("Usage: python task1.py <n> <m>")
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

circular_path = find_circular_path(n, m)
path = ''.join(map(str, circular_path))
print(path)