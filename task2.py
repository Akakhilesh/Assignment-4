user_input1 = input("Enter text to write to the file: ")
user_input2 = input("Enter additional text to append : ")

with open("output.txt","w") as file:
    file.write(user_input1)
    file.write("\n")
    print("Data successfully written to the output.txt file")

with open("output.txt","a") as file:
    file.write(user_input2)
    print("Data successfully append")

with open("output.txt","r") as file:
    print("Final content of the output.txt file")
    print(file.read())