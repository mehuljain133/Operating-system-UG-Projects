# Write a program (using fork() and/or exec() commands) where parent and child execute: a)same program, same code. b) same program, different code. - c) before terminating, the parentwaits for the child to finish its task.

import os
import time

# Function to demonstrate parent and child executing the same program, same code
def same_program_same_code():
    pid = os.fork()  # Create a child process

    if pid > 0:
        # Parent process
        print("Parent: I am the parent process.")
        time.sleep(1)  # Wait for the child to finish
        print("Parent: The child has finished.")
    elif pid == 0:
        # Child process
        print("Child: I am the child process, executing the same code.")
        time.sleep(1)
        print("Child: I am done.")

# Function to demonstrate parent and child executing the same program but with different code
def same_program_different_code():
    pid = os.fork()  # Create a child process

    if pid > 0:
        # Parent process
        print("Parent: I am the parent process, executing different code.")
        time.sleep(1)  # Simulate some work
        print("Parent: I am done with my task.")
    elif pid == 0:
        # Child process, replacing its image to run different code using exec()
        print("Child: I am the child process, executing different code.")
        time.sleep(1)
        print("Child: Child is now running a new program...")
        os.execvp("python3", ["python3", "-c", 'print("This is the new code running in the child process.")'])
        # exec() will replace the child's code, so anything after exec() won't be executed by the child.

# Function to demonstrate the parent waiting for the child to finish before terminating
def parent_waits_for_child():
    pid = os.fork()  # Create a child process

    if pid > 0:
        # Parent process
        print("Parent: Waiting for child to finish...")
        os.wait()  # Wait for child to finish
        print("Parent: Child has finished. Parent is exiting.")
    elif pid == 0:
        # Child process
        print("Child: I am the child process, performing a task.")
        time.sleep(2)  # Simulate work done by child
        print("Child: Task complete.")

if __name__ == "__main__":
    # Demonstrate same program, same code
    print("==== Same Program, Same Code ====")
    same_program_same_code()
    
    # Demonstrate same program, different code
    print("\n==== Same Program, Different Code ====")
    same_program_different_code()

    # Demonstrate parent waits for child
    print("\n==== Parent Waits for Child ====")
    parent_waits_for_child()

