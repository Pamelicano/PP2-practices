

# To move a file from one location to another, you can use the shutil.move() function from the shutil module.

import shutil
shutil.move("source_file.txt", "destination_folder/")
# The first parameter is the path to the file you want to move, and the second parameter is the path to the destination folder where you want to move the file.

# You can also specify a new name for the file in the destination folder:
import shutil
shutil.move("source_file.txt", "destination_folder/new_file_name.txt")
# If the destination folder does not exist, it will be created automatically. However, if a file with the same name already exists in the destination folder, it will be overwritten without any warning.

