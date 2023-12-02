import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def calculate(game_data):
    values = game_data.split(';')
    r, g, b = 12, 13, 14

    for value in values:
        current_data = {'red': 0, 'green': 0, 'blue': 0}
        for data in value.split(','):
            data = data.strip()
            if data:
                count, col = data.split()
                current_data[col] += int(count)

        if current_data['red'] > r or current_data['green'] > g or current_data['blue'] > b:
            return False

    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()
    total = 0
    with open(args.data_file) as f:
        for line in f:
            game_id_string, game_data = line.split(':')
            game_id_number = int(game_id_string.split()[1])
            if calculate(game_data):
                total += game_id_number
                
    print(total)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())