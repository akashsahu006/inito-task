import os
import shlex
import shutil
import function

status = True


root_path = os.getcwd()

while status:
    current_path = os.getcwd()
    print(current_path + "> ", end="", flush=True)
    command = input()
    command_list = command.split()
    main_command = command_list[0]

    if main_command == "exit":
        status = False
    elif main_command == "touch":
        if len(command_list) > 1 and len(command_list) < 5:
            function.touch(command_list[1])
        elif len(command_list) > 4:
            print("Please write text to be added in quotes.")
        else:
            print("File name not provided.")
    elif main_command == "mkdir":
        nested_path_input = command_list[1]
        nested_path = os.path.join(current_path, nested_path_input)
        function.create_folder(nested_path)
    elif main_command == "ls":
        function.list_directory_contents()
    elif main_command == "cat":
        if len(command_list) > 1:
            function.display_file_contents(command_list[1])
        else:
            print("File name not provided.")
    elif main_command == "echo":
        command_split = shlex.split(command)
        # print(command_split)
        function.write_to_file(command_split[3], command_split[1])
    elif main_command == "rm":
        if len(command_list) > 1:
            function.remove_file_or_directory(command_list[1])
        else:
            print("Provide file or directory name to be removed.")
    elif main_command == "cd":
        if len(command_list) > 1:
            function.change_path(command_list[1], root_path, current_path)
    elif main_command == "mv":
        command_split = shlex.split(command)
        source_name = command_list[1]
        destination_folder = command_list[2]
        function.move_file_or_directory(source_name, destination_folder)
    elif main_command == "cp":
        command_split = shlex.split(command)
        source_name = command_list[1]
        destination_folder = command_list[2]
        function.copy_file_or_directory(source_name, destination_folder)


print("end")
