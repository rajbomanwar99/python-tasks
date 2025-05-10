# Task 1: Read a File and Handle Errors

try:
    # Attempt to open and read the file
    with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())  # strip() removes trailing newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
