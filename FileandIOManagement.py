# File and I/O Management: Directory structure, File access methods, Disk scheduling algorithms.

import random
import collections

# Directory Structure (Filesystem)
class DirectoryStructure:
    def __init__(self):
        # The directory is represented as a dictionary with filenames as keys
        # and file sizes as values
        self.files = {}

    def create_file(self, filename, size):
        """Creates a file with a specific size"""
        if filename in self.files:
            print(f"File {filename} already exists.")
        else:
            self.files[filename] = size
            print(f"File {filename} created with size {size} KB.")

    def delete_file(self, filename):
        """Deletes a file from the directory"""
        if filename in self.files:
            del self.files[filename]
            print(f"File {filename} deleted.")
        else:
            print(f"File {filename} not found.")

    def display_directory(self):
        """Displays all files in the directory"""
        print("\nDirectory Contents:")
        for filename, size in self.files.items():
            print(f"File: {filename}, Size: {size} KB")

# File Access Methods: Sequential and Random Access
class FileAccessMethods:
    def __init__(self, directory):
        self.directory = directory

    def sequential_access(self, filename):
        """Simulates sequential file access"""
        if filename in self.directory.files:
            print(f"Starting sequential access to file {filename}.")
            file_size = self.directory.files[filename]
            for i in range(file_size):
                print(f"Reading byte {i + 1} of {filename}...")
        else:
            print(f"File {filename} not found.")

    def random_access(self, filename):
        """Simulates random access to a file"""
        if filename in self.directory.files:
            print(f"Starting random access to file {filename}.")
            file_size = self.directory.files[filename]
            random_byte = random.randint(0, file_size - 1)
            print(f"Randomly accessing byte {random_byte + 1} of {filename}.")
        else:
            print(f"File {filename} not found.")

# Disk Scheduling Algorithms: FCFS, SSTF, SCAN
class DiskSchedulingAlgorithms:
    def __init__(self, total_tracks):
        self.total_tracks = total_tracks
        self.requests = []

    def add_request(self, request):
        """Adds a new disk I/O request"""
        if 0 <= request < self.total_tracks:
            self.requests.append(request)
            print(f"Disk request for track {request} added.")
        else:
            print(f"Invalid disk request for track {request}. Must be between 0 and {self.total_tracks - 1}.")

    def fcfs(self):
        """First-Come, First-Served (FCFS) Disk Scheduling Algorithm"""
        print("\nFCFS Disk Scheduling Algorithm:")
        current_head = 0  # Assuming the initial head position is at track 0
        total_seek_time = 0
        for request in self.requests:
            seek_time = abs(request - current_head)
            total_seek_time += seek_time
            print(f"Moving from track {current_head} to {request}, seek time: {seek_time}")
            current_head = request
        print(f"Total seek time using FCFS: {total_seek_time} tracks.")

    def sstf(self):
        """Shortest Seek Time First (SSTF) Disk Scheduling Algorithm"""
        print("\nSSTF Disk Scheduling Algorithm:")
        current_head = 0
        total_seek_time = 0
        requests_copy = self.requests.copy()

        while requests_copy:
            closest_request = min(requests_copy, key=lambda req: abs(req - current_head))
            seek_time = abs(closest_request - current_head)
            total_seek_time += seek_time
            print(f"Moving from track {current_head} to {closest_request}, seek time: {seek_time}")
            current_head = closest_request
            requests_copy.remove(closest_request)

        print(f"Total seek time using SSTF: {total_seek_time} tracks.")

    def scan(self):
        """SCAN Disk Scheduling Algorithm"""
        print("\nSCAN Disk Scheduling Algorithm:")
        current_head = 0
        total_seek_time = 0
        left = [req for req in self.requests if req < current_head]
        right = [req for req in self.requests if req >= current_head]
        left.sort(reverse=True)
        right.sort()

        print(f"Requests in left: {left}")
        print(f"Requests in right: {right}")

        # Move to the leftmost track first
        for request in left:
            seek_time = abs(current_head - request)
            total_seek_time += seek_time
            print(f"Moving from track {current_head} to {request}, seek time: {seek_time}")
            current_head = request

        # Then move to the rightmost track
        for request in right:
            seek_time = abs(current_head - request)
            total_seek_time += seek_time
            print(f"Moving from track {current_head} to {request}, seek time: {seek_time}")
            current_head = request

        print(f"Total seek time using SCAN: {total_seek_time} tracks.")

# Simulation of the File and I/O Management System
def file_and_io_simulation():
    # Step 1: Directory Management
    directory = DirectoryStructure()
    directory.create_file("file1.txt", 100)
    directory.create_file("file2.txt", 200)
    directory.create_file("file3.txt", 150)
    directory.display_directory()
    directory.delete_file("file2.txt")
    directory.display_directory()

    # Step 2: File Access Methods
    file_access = FileAccessMethods(directory)
    file_access.sequential_access("file1.txt")
    file_access.random_access("file1.txt")

    # Step 3: Disk Scheduling Algorithms
    disk_scheduling = DiskSchedulingAlgorithms(total_tracks=200)
    disk_scheduling.add_request(50)
    disk_scheduling.add_request(120)
    disk_scheduling.add_request(30)
    disk_scheduling.add_request(180)
    disk_scheduling.add_request(100)

    # Using FCFS
    disk_scheduling.fcfs()

    # Using SSTF
    disk_scheduling.sstf()

    # Using SCAN
    disk_scheduling.scan()

# Run the simulation
if __name__ == "__main__":
    file_and_io_simulation()
