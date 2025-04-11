import sys
from stats import make_report




def get_book_text(f):
    return f.read()


def main():

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            contents = get_book_text(file)
            make_report(contents)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()