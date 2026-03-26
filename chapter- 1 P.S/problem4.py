import os
# Select the directory whose content you want to list
path = "."

contents = os.listdir(path)
# Use the os module to list the directory content
for item in contents:
    # Print yhe directory of the content
    print(item)