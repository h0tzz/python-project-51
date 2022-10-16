# !usr/bin/env python3
from page_loader import download
from page_loader.cli import parse_arguments


def main():
    """
        download all files from url
    """
    args = parse_arguments()

    try:
        print(
            download(args.url, args.output)
        )
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
