import os

directory = 'C:\\Users\\vetha\\Desktop\\New folder (2)'

for root, dirs, files in os.walk(directory):
    for filename in files:
        path=os.path.join(root, filename)
        with open(path, 'r') as file:
            content = '\n'.join(file.readlines())

