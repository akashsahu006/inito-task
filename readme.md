# Assignment Question:In-Memory File System

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

## Functions

1. `ls` : It is implemented in function - create_folder.

## Testcases

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
