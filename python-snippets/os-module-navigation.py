# OS module filesystem navigation

import os

# Get current working directory
directory = os.getcwd()
print(directory)

# Create dir
os.mkdir("photos") # relative
os.mkdir("/home/bobby/photographs") # absolute

# Change working directory
os.chdir("/home/mike/testing/projects")

# Delete file or directory a la rmdir
os.remove("random.txt") # If file doesn't exist, will throw 'FileNotFoundError'
os.rmdir("/home/mike/testing/projects")

# List files and dirs
print(os.listdir())
