import os
from config import *

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