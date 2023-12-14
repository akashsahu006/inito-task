import os
import shlex
import shutil
import function
import grep

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
    # COMMAND touch
    elif main_command == "touch":
        if len(command_list) == 1:
            print("Error: No filename provided")
        elif len(command_list) > 1 and len(command_list) <= 2:
            function.touch(command_list[1])
        elif len(command_list) > 2:
            print("Error: Invalid command.")
    # COMMAND mkdir
    elif main_command == "mkdir":
        if len(command_list) > 2:
            print("Error: Invalid input.")
        else:
            nested_path_input = command_list[1]
            nested_path = os.path.join(current_path, nested_path_input)
            function.create_folder(nested_path)
    # COMMAND: ls
    elif main_command == "ls":
        if len(command_list) == 1:
            function.list_directory_contents()
        else:
            print("Please write valid command")
    # COMMAND: cat
    elif main_command == "cat":
        if len(command_list) == 2:
            function.display_file_contents(command_list[1])
        elif len(command_list) == 3 and command_list[1] == "-n":
            function.cat_with_line_numbers(command_list[2])
        else:
            print("Error: Invalid command.")

    # COMMAND: echo
    elif main_command == "echo":
        command_split = shlex.split(command)
        if len(command_split) == 4 and command_split[2] == ">":
            function.write_to_file(command_split[3], command_split[1])
        elif len(command_split) > 4 and command_split[2] != ">":
            print("Please provide input in quotes.")
        else:
            print("Error: Please write valid command.")
    # COMMAND rm
    elif main_command == "rm":
        if len(command_list) == 2:
            function.remove_file_or_directory(command_list[1])
        else:
            print("Error: Invalid command.")
    # COMMAND cd
    elif main_command == "cd":
        if len(command_list) == 2:
            function.change_path(command_list[1], root_path, current_path)
        else:
            print("Error:Invalid parameters.")
    # COMMAND mv
    elif main_command == "mv":
        command_split = shlex.split(command)
        if len(command_split) == 3:
            source_name = command_list[1]
            destination_folder = command_list[2]
            function.move_file_or_directory(source_name, destination_folder)
        else:
            print("Error: Invalid number of arguments.")
    # COMMAND cp
    elif main_command == "cp":
        command_split = shlex.split(command)
        source_name = command_list[1]
        destination_folder = command_list[2]
        function.copy_file_or_directory(source_name, destination_folder)

    elif main_command == "grep":
        if len(command_list) == 4:
            option = command_list[1]
            pattern = command_list[2]
            filename = command_list[3]
            grep.grep_function(option, pattern, filename)
        else:
            print("Error: Invalid command.")
    else:
        print("Command not recognized.")


print("end")
