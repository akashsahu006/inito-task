import re


def grep_case_insensitive(pattern, filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if re.search(pattern, line, re.IGNORECASE):
                    print(f"{filename}:{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


def grep_count(pattern, filename):
    count = 0
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                if re.search(pattern, line):
                    count += 1
            print(count)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    return count


def grep_with_line_numbers(pattern, filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if re.search(pattern, line):
                    print(f"{line_number}:{line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


def grep_no_match(pattern, filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if not re.search(pattern, line):
                    print(f"{filename}:{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


def grep_function(option, pattern, filename):
    if option == "-i":
        grep_case_insensitive(pattern, filename)
    elif option == "-c":
        grep_count(pattern, filename)
    elif option == "-n":
        grep_with_line_numbers(pattern, filename)
    elif option == "-v":
        grep_no_match(pattern, filename)
    else:
        print("Invalid option. Please use following options: \n-i \n-c \n-n \n-v")
