import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)

        if not abs_full_path.startswith(abs_working):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_full_path):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        completed = subprocess.run(['python', abs_full_path] + args, timeout=30, capture_output=True, text=True, cwd=abs_working)
        output = []

        if completed.stdout:
            output.append("STDOUT:\n" + completed.stdout)
        if completed.stderr:
            output.append("STDERR:\n" + completed.stderr)
        if completed.returncode != 0:
            output.append(f"Process exited with code {completed.returncode}")
        if not output:
            return "No output produced."
        return "\n".join(output)
    except Exception as e:
        return f"Error: {str(e)}"
