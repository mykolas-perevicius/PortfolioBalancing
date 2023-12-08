import os
from zipfile import ZipFile, ZIP_DEFLATED

# Define your project directory
project_dir = r'C:\Users\miciu\Desktop\PortfolioBalanc.ing'
# Define the name of the zip file you want to create
zip_filename = os.path.join(project_dir, 'project_backup.zip')

# List of directories to exclude from the zipping process
excluded_dirs = {'node_modules', 'venv', '__pycache__', '.git'}

# List of file extensions to exclude from the zipping process
excluded_extensions = {'.pyc', '.env'}

def should_include_file(file_path):
    # Exclude files based on directory
    for excluded_dir in excluded_dirs:
        if f"{os.sep}{excluded_dir}{os.sep}" in file_path or file_path.endswith(excluded_dir):
            return False
    # Exclude files based on extension
    for excluded_extension in excluded_extensions:
        if file_path.endswith(excluded_extension):
            return False
    return True

with ZipFile(zip_filename, 'w', ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_dir):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for file in files:
            file_path = os.path.join(root, file)
            if should_include_file(file_path):
                # Write the file to the zip file
                zipf.write(file_path, os.path.relpath(file_path, project_dir))

print(f'Project zipped into {zip_filename}')
