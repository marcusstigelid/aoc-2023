import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def calculate(game_data):
    values = game_data.split(';')
    min_cube = {'red': 0, 'green': 0, 'blue': 0}

    for value in values:
        current_cube = {'red': 0, 'green': 0, 'blue': 0}
        for data in value.split(','):
            data = data.strip()
            if data:
                count, col = data.split()
                current_cube[col] += int(count)

        for col in min_cube:
            min_cube[col] = max(min_cube[col], current_cube[col])

    return min_cube

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()
    total = 0
    with open(args.data_file) as f:
        for line in f:
            _, game_data = line.split(':')
            min_cube = calculate(game_data)
            total += min_cube['red'] * min_cube['green'] * min_cube['blue']

    print(total)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())