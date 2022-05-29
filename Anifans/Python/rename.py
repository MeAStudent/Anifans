import os
import re

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

folder = r'C:\xampp\htdocs\www\Anifans\HomeImg\\'
count = 1

for old_name in sorted(os.listdir(folder), key=numericalSort):

    new_name = str(count) + ".jpg"
    source = folder + old_name
    
    if os.path.isfile(new_name):
        print('The file already exists"')
        count += 1
    else:
        destination = folder + str(count) + ".jpg"
        os.rename(source, destination)
        count += 1
    
    
print('All Files Renamed')