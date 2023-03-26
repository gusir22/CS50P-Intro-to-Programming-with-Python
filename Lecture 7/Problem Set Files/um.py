import re


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"(?:\W|\A)(um)(?:\W|\Z)", s, flags=re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
