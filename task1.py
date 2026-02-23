try:
    with open("sample.txt", "r") as file:
        print(f" Line 1: {file.readline()}")
        print(f" Line 2: {file.readline()}")
except FileNotFoundError:
     print("The file 'sample.txt' not found")