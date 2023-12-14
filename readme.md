# Assignment Submission: In-Memory File System

##Commands

1. `mkdir`: Create a new directory.
2. `cd`: Changes the current directory. Support navigating to the parent directory using `..`, moving to the root directory using `/`, and navigating to a specified absolute path. Basically anything that you can do in a normal terminal. Since there is no user level implementation, ~ and / should take you to root.
3. `ls`: List the contents of the current directory or a specified directory.
4. `grep`: Search for a specified pattern in a file. **PS: Its a bonus**
5. `cat`: Display the contents of a file.
6. `touch`: Create a new empty file.
7. `echo`: Write text to a file. ex - `echo 'I am "Finding" difficult to write this to file' > file.txt`
8. `mv`: Move a file or directory to another location. ex - `mv /data/ice_cream/cassata.txt ./data/boring/ice_cream/mississippimudpie/`
9. `cp`: Copy a file or directory to another location. ex - `cp /data/ice_cream/cassata.txt .` **. For current directory **
10. `rm`: Remove a file or directory.

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
