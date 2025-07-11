import os
from config import *

def get_files_info(working_directory, directory=None):
    try:
        if directory is None:
            directory = " "
        full_path = os.path.join(working_directory, directory)
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(full_path)

        if not abs_target.startswith(abs_working):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        contents_list = []
        for item in os.listdir(full_path):
            contents_list.append(f"- {item}: file_size={os.path.getsize(os.path.join(full_path, item))} bytes, is_dir={os.path.isdir(os.path.join(full_path, item))}")
        return "\n".join(contents_list)

    except Exception as e:
        return f"Error: {str(e)}"

def get_file_content(working_directory, file_path):
    try:
        joined_file_path = os.path.join(working_directory, file_path)
        abs_joined = os.path.abspath(joined_file_path)
        abs_working = os.path.abspath(working_directory)

        if not abs_joined.startswith(abs_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_joined):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abs_joined, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string += f"[...File {file_path} truncated at 10000 characters]"
            return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"
