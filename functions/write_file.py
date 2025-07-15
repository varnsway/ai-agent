import os

def write_file(working_directory, file_path, content):
    try:
        joined_file_path = os.path.join(working_directory, file_path)
        abs_joined = os.path.abspath(joined_file_path)
        abs_working = os.path.abspath(working_directory)

        if not abs_joined.startswith(abs_working):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_joined):
            os.makedirs(os.path.dirname(abs_joined), exist_ok=True)

        with open(abs_joined, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"