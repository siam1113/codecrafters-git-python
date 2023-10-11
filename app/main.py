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
        return zlib.decompress(open(f".git/objects/{blob_sha[0:2]}/{blob_sha[2:]}").read()).decode()

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    
    command = sys.argv[1]
    if command == "init":
        init()
    elif command == "cat-file":
        print(cat_file(sys.argv[2], sys.argv[3]))
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
