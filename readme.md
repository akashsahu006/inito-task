# Assignment Submission: In-Memory File System

# Setup

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- pip for Python package management
- Access to a terminal or command line interface

### Additional requirement

- Before installing the project, ensure you have setuptools installed, as it is required for the installation process.

```bash
pip install setuptools
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/akashsahu006/inito-task.git
cd inito-task
```

### 2. Install the Package

Navigate to the directory containing setup.py and run the following command to install the package and its dependencies:

```bash
pip install .
```

## Running the Project

```bash
python main.py
```

## Running Unit tests

```bash
python test.py
```

# Project Description

## Using the project

1. To create a new directory:

```bash
mkdir directoryname
```

2. To change directories use following options:

```bash
cd directoryname
cd ~
cd /
cd ..
```

3. To list contents in a directory:

```bash
ls
```

4. To search within files: grep "pattern" filename.txt

```bash
grep -i pattern filename
grep -c pattern filename
grep -n pattern filename
grep -v pattern filename
```

5. To display the contents of a file:

```bash
cat filename
cat -n filename
```

6. To create a new file:

```bash
touch filename
```

7. To write to a file: echo "text" > filename.txt

```bash
 echo "text" > filename
```

8. To move or rename a file/directory:

```bash
mv source target
```

9. To copy a file or directory: cp source target

```bash
cp source target
```

10. To remove a file or directory:

```bash
rm filename
```

## Function for each command

1. `mkdir:` It is implemented in function - **create_folder**. The os.makedirs("file_name") is used to create new folder. Errors like "file exists" or "no file name given" errors are checked.
2. `cd:` It is implemented in function - **change_path**. The function os.chdir(path) is used. Use cases like _".." to go to parent directory_, _"~" or "/" to go to root directory_ and absolute path are considered. Errors like "invalid path" are checked.
3. `ls:` It is implemented in function - **list_directory_contents**. The function os.listdir() is used. The error like invalid commands are checked.
4. `grep:` It is implemented in file **grep**.py. Total four variation are implemented those are:- -n -i -v -c.
5. `cat:` It is implemented in function **display_file_contents**. It is implemented using file.read() function. Use cases like **cat filename.txt** and **cat -n filename.txt** (Read file content with line number) is considered. Errors like "file does not exist" are checked.
6. `touch:` It is implemented in function - **touch**. It uses function open(filename, "x"). Cases like if file already exist is also considered.
7. `echo:` It is implemented in function - **write_to_file**. It uses function open(filename, "a") to write to file. Use cases like _retaining previous content_ in existing file and _writing into empty file_ is considered.
8. `mv:` It is implemented in function - **move_file_or_directory**. It uses function shutil.move(source, destination).
9. `cp:` It is implemented in function - **copy_file_or_directory**. It uses function shutil.copy(source, destination).
10. `rm:` It is implemented in function - **remove_file_or_directory()**. It uses os.remove() and os.rmdir() functions. Errors like file does not exist are accounted.

## UNIT TESTS

1. `test_mkdir:` This test checks if a new directory gets created or not using mkdir command.
2. `test_mkdir_file_exists:` This test tries to create an existing directory to check if correct error message is given.
3. `test_cd:` This test checks if cd command is executed or not.
4. `test_cd_parent:` This test checks if cd command takes back to parent directory when "cd .." command is given.
5. `test_touch:` This test checks if touch command creates a new file.
6. `test_echo:` This test checks if echo command writes new text to the empty file.
7. `test_echo_append:` This test checks if the original content is maintained or lost after execution of echo command.
8. `test_rm_file:` This test checks if a file is removed or not after execution of rm command.
9. `test_rm_folder:` This test checks if a directory is removed or not after execution of rm command.
10. `test_cat:` This test checks if cat command read properly from the file or not.
11. `test_mv:` This test checks if mv command moves a file to destination folder.
