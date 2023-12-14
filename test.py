import unittest
import function
from io import StringIO
import os
from unittest.mock import patch


class Testing(unittest.TestCase):
    # TEST CASE: mkdir
    def test_mkdir(self):
        function.create_folder("Test_folder")
        self.assertTrue(os.path.exists("Test_folder"))
        os.rmdir("Test_folder")

    def test_mkdir_file_exists(self):
        folder_name = "Test_folder"
        os.makedirs(folder_name)  # create an existing folder
        function.create_folder(folder_name)
        os.rmdir(folder_name)

    # TEST CASE: cd
    def test_cd(self):
        initial_directory = os.getcwd()
        folder_name = "Test_folder"

        # Defining target directory
        os.makedirs(folder_name)
        target_directory = os.path.join(initial_directory, folder_name)

        # Calling the function that changes the directory
        function.change_path(target_directory, initial_directory, initial_directory)

        # Getting the current directory after calling the function
        new_directory = os.getcwd()

        # Asserting that the current directory has been changed as expected
        self.assertEqual(new_directory, os.path.abspath(target_directory))

        # Clean up: Change back to the initial directory
        os.chdir(initial_directory)
        os.rmdir(folder_name)

    def test_cd_parent(self):
        parent_directory = os.getcwd()
        # creating two folders
        folder_name = "Test_folder"
        os.makedirs(folder_name)
        target_directory = os.path.join(parent_directory, folder_name)
        function.change_path(target_directory, parent_directory, parent_directory)

        # using .. to go to root directory
        parent = ".."
        function.change_path(parent, parent_directory, os.getcwd())

        self.assertEqual(parent_directory, os.getcwd())
        os.rmdir(folder_name)

    def test_touch(self):
        # Call the function to create an empty file
        filename = "test_file_touch"
        try:
            # Call the function to create an empty file
            function.touch(filename)

            # Assert that the file was created
            self.assertTrue(os.path.exists(filename))

            # Assert that the file is empty
            with open(filename, "r") as test_file:
                content = test_file.read()
                self.assertEqual(content, "")

        finally:
            # Clean up: Remove the file
            if os.path.exists(filename):
                os.remove(filename)

    def test_echo(self):
        filename = "test_file"
        try:
            # Defining the text to write to the file
            function.touch(filename)
            text_write = "Dummy content to be written."

            # Calling the function to write text to the file
            function.write_to_file(filename, text_write)

            # Asserting that the file was created
            self.assertTrue(os.path.exists(filename))

            # Asserting that the file contains the expected content
            with open(filename, "r") as test_file:
                content = test_file.read()
                self.assertEqual(content, text_write)
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_echo_append(self):
        filename = "test_file"
        try:
            function.touch(filename)
            text_original = "Dummy content"
            with open(filename, "w") as test_file:
                test_file.write(text_original)

            function.write_to_file(filename, "New text")
            text_updated = text_original + "\n" + "New text"
            with open(filename, "r") as test_file:
                content = test_file.read()
                self.assertEqual(content, text_updated)

        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_rm_file(self):
        filename = "test_file"
        try:
            function.touch(filename)
            function.remove_file_or_directory(filename)
            self.assertFalse(os.path.exists(filename))
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_rm_folder(self):
        filename = "test_file"
        try:
            os.makedirs(filename)
            function.remove_file_or_directory(filename)
            self.assertFalse(os.path.exists(filename))
        finally:
            if os.path.exists(filename):
                os.remove(filename)


if __name__ == "__main__":
    unittest.main()
