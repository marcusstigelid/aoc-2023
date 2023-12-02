import argparse
import os.path
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# Part 1
def calculate(s: str):
     lines = s.split("\n")
     numbers = [re.findall("\d", line) for line in lines]
     return sum(int(n[0] + n[-1]) for n in numbers)

# Part 2
def calculate_part_2(s: str):
    s = (
        s.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    return calculate(s)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(calculate_part_2(f.read().strip()))

    return 0

if __name__ == "__main__":
    raise SystemExit(main())