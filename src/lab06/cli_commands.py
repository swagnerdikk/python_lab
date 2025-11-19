import argparse
import os
import sys
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lab04.text_report import frequencies_from_text, sorted_word

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_pars = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_pars.add_argument("--input", required=True, help='Путь к фходному файлу')
    cat_pars.add_argument("-n", action="store_true", help="Нумеровать строки")
    
    stats_pars = subparsers.add_parser("stats", help="Частоты слов")  
    stats_pars.add_argument("--input", required=True)
    stats_pars.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        input_path = Path(args.input)
        if not input_path.exists():
            cat_pars.error(f"Файл не найден: '{args.input}'")
        
        try:
            for i, line in enumerate(input_path.read_text(encoding='utf-8').splitlines()):
                print(f"{i + 1}. {line}" if args.n else line)
        except FileNotFoundError:
            cat_pars.error(f"Файл не найден: '{args.input}'")
        except Exception as e:
            cat_pars.error(f"Ошибка при чтении файла: {e}")
            
    elif args.command == "stats":
        if args.top <= 0:
            stats_pars.error(f"--top должен быть положительным числом, получено: {args.top}")
        
        input_path = Path(args.input)
        if not input_path.exists():
            stats_pars.error(f"Файл не найден: '{args.input}'")
        
        try:
            new_str = input_path.read_text(encoding='utf-8')
            sorted_list = sorted_word(frequencies_from_text(new_str))
            for word, count in sorted_list[:args.top]:
                print(f"{word}: {count}")
        except FileNotFoundError:
            stats_pars.error(f"Файл не найден: '{args.input}'")
        except Exception as e:
            stats_pars.error(f"Ошибка при обработке файла: {e}")

if __name__ == "__main__":
    main()