import os

directory_name = None
while directory_name == None:
    directory_name = input("Enter the directory you would like to save your file to: ")
    if not os.path.isdir (directory_name):
        print("Please enter a valid directory name: ")
        directory_name = None
        
file_name = None
while file_name == None:
    file_name = input("Enter the file name you would like to save that is txt or csv: ")
    if os.path.isfile(file_name):
        print ("File is already present.")
        file_name = None

name = input("Enter your name: ")
address = input("Enter your address: ")
phone_number = input("Enter your phone number: ")

full_path = os.path.join(directory_name, file_name)
file = open(full_path, 'w')
file.write ("Name,Address,Phone\n")
file.write (f'{name},{address},{phone_number}')
file.close()
print(f"File successfully written to {full_path}")

      

