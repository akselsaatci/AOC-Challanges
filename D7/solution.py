# aoc202207.py

import pathlib
import sys
with open('data.txt', "r") as datafile:
    puzzle_input = datafile.read()

def parse(puzzle_input: str) -> list[list[str]]:
    """ Parse input """
    data = puzzle_input.replace('$ ', '').splitlines()
    return [line.split(' ') for line in data]


def folder_sizes(output: list[list[str]]) -> dict[str, int]:
    """ Return a dict of folder sizes from commands """
    folders: dict[str, int] = {}
    path: list[str] = ['/']
    current_path: str = ''.join(path)
    folders.setdefault(current_path, 0)

    for line in output:
        if line[0] == "ls":
            continue
        elif line[0] == "dir":
            folders.setdefault(current_path + line[1] + '/', 0)
        elif line[0].isdigit():
            folders[current_path] += int(line[0])
        elif line[0] == "cd":
            if line[1] == "..":
                # Account for subfolder size
                subfolder_size: int = folders.get(current_path)
                path.pop()
                current_path = ''.join(path)
                folders[current_path] += subfolder_size
            elif line[1] == '/':
                path = [line[1]]
                current_path = ''.join(path)
            else:
                path.append(line[1] + '/')
                current_path = ''.join(path)

    # Add folder size for any remaining folders in stack
    for n in range(len(path) - 1):
        subfolder_size = folders.get(current_path)
        path.pop()
        current_path = ''.join(path)
        folders[current_path] += subfolder_size

    return folders


def part1(data: list[list[str]]) -> int:
    """ Solve part 1 """
    dirs: dict[str, int] = folder_sizes(data[1:])

    return sum(v for v in dirs.values() if v <= 100000)


def part2(data: list[list[str]]) -> int:
    """ Solve part 2 """
    dirs: dict[str, int] = folder_sizes(data[1:])
    total: int = 70000000
    space_needed: int = 30000000
    space_used: int = dirs.get('/')
    unused_space: int = total - space_used

    return min(v for v in dirs.values() if v > (space_needed - unused_space))


def solve(puzzle_input: str) -> tuple[int, int]:
    """ Solve the puzzle for the given input """
    data = parse(puzzle_input)
    solution1: int = part1(data)  # Correct answer was 1723892 (with my data)
    solution2: int = part2(data)  # Correct answer was 8474158 (with my data)

    return solution1, solution2


solutions = solve(puzzle_input)
print('\n'.join(str(solution) for solution in solutions))