# Task 2: Write and Append Data to a File

# Step 1: Take user input and write to the file
user_input = input("Enter some data to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data to the same file
additional_data = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
