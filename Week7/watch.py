import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url_match = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z0-9_]+)", s)
        if url_match:
            split_url = url_match.groups()
            return "https://youtu.be/" + split_url[3]

if __name__ == "__main__":
    main()