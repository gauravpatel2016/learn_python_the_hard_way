from sys import argv
from os.path import exists

script, from_file, to_file = argv


print(f"Copying content from {from_file} to {to_file}")

# you can enable next 3 lines
# in_file = open(from_file, mode = 'r')
# print(in_file.read())
# in_file.close()

## or you can do 
in_data = open(from_file, mode = 'r').read()


print(f"The input file is {len(in_data)} bytes long") 
print(f"Does the output file exist? {exists(to_file)}") 
print("Ready, hit RETURN to continue, CTRL-C to abort.")

with open(to_file, mode = 'w+') as out_content:
    out_content.write(in_data)
    out_content.readlines()


#  or you can 
#  open(to_file, 'w+').write(in_data)

