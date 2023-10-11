import sys
import os
import zlib
import typing


def init():
    os.mkdir(".git")
    os.mkdir(".git/objects")
    os.mkdir(".git/refs")
    with open(".git/HEAD", "w") as f:
        f.write("ref: refs/heads/master\n")
    print("Initialized git directory")


def cat_file(option: str, blob_sha: str) -> str:
    if option == "-p":
        print_blob(blob_sha)

def print_blob(blob_sha: str) -> None:
    path = f".git/objects/{blob_sha[0:2]}/{blob_sha[2:]}"
    with open(path, "rb") as f:
        file = zlib.decompress(f.read())
        _, content = file.split(b"\x00", maxsplit=1)
        print(content.decode())

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    
    command = sys.argv[1]
    if command == "init":
        init()
    elif command == "cat-file":
        cat_file(sys.argv[2], sys.argv[3])
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
