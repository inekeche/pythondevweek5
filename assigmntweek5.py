def read_and_modify_file():
    try:
        filename = input("Enter the filename to read from: ").strip()

        # Try opening the input file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        with open('output.txt', 'w') as output_file:
            output_file.write(modified_content)

        print("File read successfully and modified content written to 'output.txt'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"❌ Error: The file '{filename}' could not be read.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()