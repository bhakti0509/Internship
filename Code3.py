'''Objective: To identify and fix errors in a Python program that reads and writes to a file.
Here's the corrected code:'''

def read_and_write_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the content

        # Close the file before opening it for writing
        with open(filename, 'w') as file:
            file.write(content.upper())  # Write the uppercased content
        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = "sample.txt"
    read_and_write_file(filename)

if __name__ == "__main__":
    main()
