import argparse

from .scanner import scan


def main():
    parser = argparse.ArgumentParser(
        prog="gozere",
        description="A home for things on their way somewhere,",
    )

    parser.add_argument(
        "command",
        choices=["scan"],
        help="Command to execute",
    )

    args = parser.parse_args()

    if args.command == "scan":
        scan()

if __name__ == "__main__":
    main()
