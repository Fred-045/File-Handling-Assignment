try:
    
    with open("rick_file.txt", 'w') as file:
        
        file.write("This is the first line.\n")
        file.write("Number of participants: 25\n")
        file.write("Success rate: 90%\n")
    print("File created and written successfully.")

#  Error Handling 
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")

#File Reading and Display
try:
    # Reading the contents of the file
    with open("rick_file.txt", 'r') as file:
        print("\nContents of the file:")
        content = file.read()
        print(content)

# Handling errors during file reading
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")

 # File Appending
try:
    # Opening the file in append mode and adding more lines
    with open("rick_file.txt", 'a') as file:
        file.write("This is an appended line.\n")
        file.write("New participants: 10\n")
        file.write("Completion rate: 85%\n")
    print("\nFile appended successfully.")

    # Reading the updated content
    with open("rick_file.txt", 'r') as file:
        print("\nUpdated contents of the file:")
        content = file.read()
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")


    print("\nFile operations completed.")