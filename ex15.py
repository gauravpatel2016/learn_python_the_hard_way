from sys import argv

script, filename = argv

f = open(filename)

print(f"My filename is {filename}")
print(f.read())

print("Type the filename again:") 
file_again = input("> ") 
txt_again = open(file_again) 
print(txt_again.read())