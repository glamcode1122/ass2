def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return None

def write_file(output_filename, contents):
    try:
        with open(output_filename, 'w') as file:
            file.write(contents)
        print(f"Modified content successfully written to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to the file '{output_filename}'.")

def modify_content(content):
    # Example modification: convert content to uppercase
    return content.upper()

def main():
    input_filename = input("Enter the filename to read: ")
    contents = read_file(input_filename)

    if contents is not None:
        modified_contents = modify_content(contents)
        output_filename = input("Enter the output filename: ")
        write_file(output_filename, modified_contents)

if __name__ == "__main__":
    main()
