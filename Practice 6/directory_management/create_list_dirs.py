# To create a directory in Python, you can use the os.mkdir() method. This method takes the name of the directory as a parameter and creates it in the current working directory.
import os
os.mkdir("myfolder")

# To create a directory in a different location, you can specify the path to the directory as a parameter:

import os
os.mkdir("D:\\myfiles\\newfolder")

# To create a directory and all intermediate-level directories needed to contain it, you can use the os.makedirs() method:
import os
os.makedirs("D:\\myfiles\\newfolder\\subfolder")


