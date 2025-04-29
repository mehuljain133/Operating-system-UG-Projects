# Write a program to print file details including owner access permissions, file access time,where file name is given as argument.

import os
import sys
import stat
import pwd
import time

def file_details(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    try:
        file_stat = os.stat(file_path)

        # Owner (username)
        uid = file_stat.st_uid
        owner = pwd.getpwuid(uid).pw_name

        # Permissions
        permissions = stat.filemode(file_stat.st_mode)

        # Last access time
        access_time = time.ctime(file_stat.st_atime)

        print(f"\n=== File Details ===")
        print(f"File: {file_path}")
        print(f"Owner: {owner} (UID: {uid})")
        print(f"Permissions: {permissions}")
        print(f"Last Access Time: {access_time}")

    except Exception as e:
        print(f"Error reading file details: {e}")

# Main block
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_info.py <filename>")
    else:
        file_path = sys.argv[1]
        file_details(file_path)
