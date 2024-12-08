import argparse

parser = argparse.ArgumentParser()

parser.add_argument('number', type=int, help='Число')
parser.add_argument('string', type=str, help='Строка')

parser.add_argument('--verbose', action='store_true', help='Доп. информация')
parser.add_argument('--repeat', type=int, default=0, help='Количество повторений строки')

args = parser.parse_args()

if (args.verbose and args.repeat):
    print(f'Число: {args.number}, Строка: "{args.string}", Повторений строки = {args.repeat}')
    print(f'Число: {args.number}, Строка: "{args.string * args.repeat}"')
elif args.verbose:
    print(f'Число: {args.number}, Строка: "{args.string}"')
elif args.repeat:
    print(f'Число: {args.number}, Строка: "{args.string * args.repeat}"')
