import re
import os

# ANSI escape sequence for red color
RED_COLOR = "\033[91m"
# ANSI escape sequence for yellow color
YELLOW_COLOR = "\033[93m"
# ANSI escape sequence to reset color
RESET_COLOR = "\033[0m"

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Prompt the user to enter the search queries
queries = input("Enter the search queries (separated by commas): ")
queries_list = [q.strip() for q in queries.split(",")]

# Iterate over queries
for query in queries_list:
    # Convert asterisks to regular expression pattern
    pattern = query.replace('*', r'\w')

    # Flag to track if matches were found for the current query
    matches_found = False

    # Iterate over files in the directory
    for filename in os.listdir(current_dir):
        file_path = os.path.join(current_dir, filename)

        # Check if the file is a regular file
        if os.path.isfile(file_path):
            # Open the file
            with open(file_path, 'r') as file:
                # Read the contents of the file
                contents = file.read()

                # Search for the modified query within the contents of the file
                matches = [email for email in contents.split('\n') if re.match(pattern, email)]

                # Print the matching emails with file name
                if matches:
                    matches_found = True
                    print(f"{RED_COLOR}Matches found in file: {filename}{RESET_COLOR}")
                    for email in matches:
                        print(email)

    # Print "No matches found" if no matches were found for the current query
    if not matches_found:
        print(f"{YELLOW_COLOR}No matches found for query: {query}{RESET_COLOR}")
