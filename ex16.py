from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, mode='w+')

print("Truncating the file. Goodbye!")

# you don't need this line if you open file in 'w' mode. It will overwrite it anyway
target.truncate() 

print("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

target.write(line1 + "\n" + line2 + "\n" + line3)
print("We have entered text into the file the file!!!")
print("And finally, we close it.")
target.close()

# extra stuff

with open(filename, mode='r') as mynewfile:
    print(mynewfile.read())
