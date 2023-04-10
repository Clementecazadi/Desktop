import sys

if len(sys.argv) != 2:
    print("Error! Could not run the program!")
    sys.exit(1)
print(f"Hello {sys.argv[1]}.")
