from pathlib import Path

from .classifier import classify

INBOX = Path("F:/_GOZERE")

def scan():
    if not INBOX.exists():
        print(f"Inbox not found: {INBOX}")
        return

    files = sorted(
        (item for item in INBOX.iterdir() if item.is_file()),
        key=lambda item: item.name.lower(), # sort() filesnames.alphabetically.ignore-case
    )

    print("\nGOZERE - Intake Discovery")
    print(f"Inbox: {INBOX}")
    print(f"Files found: {len(files)}\n")

    for file in files:
        category = classify(file)
        print(f"  [{category:<10}] {file.name}")

    if not files:
        print("  Inbox is empty.")

    print()
