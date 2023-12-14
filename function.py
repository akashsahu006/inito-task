import os
import shlex
import shutil


def create_folder(path):
    try:
        # Create nested folders
        os.makedirs(path)
        print(f"Folder structure '{path}' created successfully.")
    except FileExistsError:
        print(f"Folder structure '{path}' already exists.")


# Get the current working directory


# touch is implemented here
def touch(filename):
    try:
        with open(filename, "x") as file:
            print("File created and written successfully.")
    except FileExistsError:
        print(f"Error: File '{filename}' already exists.")


def list_directory_contents(directory="."):
    try:
        # Get the list of files and directories in the specified directory
        contents = os.listdir(directory)

        # Print the contents
        # print(f"Contents of directory '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")


def display_file_contents(file_path):
    try:
        with open(file_path, "r") as file:
            # Read and print the contents of the file
            file_contents = file.read()
            print(f"Contents of file '{file_path}':\n{file_contents}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError as e:
        print(f"Error: Unable to read file '{file_path}'. {e}")


def write_to_file(filename, content):
    try:
        with open(filename, "r") as file:
            file_content = file.read()
            with open(filename, "a") as file_w:
                if file_content == "":
                    file_w.write(content)
                else:
                    file_w.write("\n" + content)

    except FileNotFoundError:
        print("Error: File not found.")


def remove_file_or_directory(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"File '{path}' removed successfully.")
        elif os.path.isdir(path):
            os.rmdir(path)
            print(f"Directory '{path}' removed successfully (recursively).")
        else:
            print(f"Error: Path '{path}' does not exist.")
    except Exception as e:
        print(f"Error: Unable to remove '{path}'. {e}")


def move_file_or_directory(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source '{source}' not found.")
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(f"Error: Unable to move '{source}' to '{destination}'. {e}")


def copy_file_or_directory(source, destination):
    try:
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print(f"Copied file '{source}' to '{destination}' successfully.")
        elif os.path.isdir(source):
            shutil.copytree(source, destination)
            print(f"Copied directory '{source}' to '{destination}' successfully.")
        else:
            print(f"Error: Source '{source}' does not exist.")
    except Exception as e:
        print(f"Error: Unable to copy '{source}' to '{destination}'. {e}")


def change_path(destination, root_path, current_path):
    if destination == "/" or destination == "~":
        os.chdir(root_path)
    else:
        nested_path_input = destination
        nested_path = os.path.join(current_path, nested_path_input)
        try:
            os.chdir(nested_path)
        except FileNotFoundError:
            print("File not found.")
