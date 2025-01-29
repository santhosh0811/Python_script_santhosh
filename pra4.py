import os

# Define the root folder where license files are located
root_folder = "/home/ubuntu/hadoop"

# Define the name of the output file
output_file = "licence_append.txt"

# Open the output file in append mode
with open(output_file, "a") as outfile:
    # Walk through all subdirectories in the root folder
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            # Check if the file name matches typical license files (e.g., LICENSE, LICENSE.txt, etc.)
            if file.upper().startswith("NOTICE"):
                file_path = os.path.join(root, file)
                # Write the file path above the content
                outfile.write(f"File Path: {file_path}\n")
                # Append the content of the license file to the output file
                try:
                    with open(file_path, 'r') as fh:
                        outfile.write(fh.read())
                        outfile.write("\n\n")  # Add a newline between license contents
                except Exception as e:
                    outfile.write(f"Error reading {file_path}: {str(e)}\n")

