# FOLDER.py should perhaps be replaced with FILE.py

# A Directory node(or a Folder node) will contain information about Files and Directores(FOLDERS) beneath it.
# The root directory by convention is called "/"
# Each "process of archiving" is associated with a current working directory.

# A file is of the following types:
  # “Regular file
# Directory
# Symbolic link
# Block-oriented device file
# Character-oriented device file
# Pipe and named pipe (also called FIFO)
# Socket”


# FILES are associated with INODES

Number of hard links associated with the file
File length in bytes
Device ID (i.e., an identifier of the device containing the file)
Inode number that identifies the file within the filesystem
UID of the file owner
User group ID of the file
Several timestamps that specify the inode status change time, the last access time, and the last modify time
Access rights and file mode.


*** Access Rights and File Mode ***
The potential users of a file fall into three classes:

1. The user who is the owner of the file
2. The users who belong to the same group as the file, not including the owner
3. All remaining users (others)”

