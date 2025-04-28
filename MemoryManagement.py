# Memory Management: Physical and Logical address space; Memory allocation strategies -Fixed and Variable Partitions, Paging, Segmentation, Demand Paging and virtual memory, PageReplacement algorithm.

import random
import time
from collections import deque

# Constants
PAGE_SIZE = 4  # Size of a page in memory (in terms of memory units)
RAM_SIZE = 16  # Total physical memory (in terms of memory units)
NUM_PAGES = RAM_SIZE // PAGE_SIZE  # Number of pages that fit in RAM

# Helper function to simulate logical-to-physical address translation
def logical_to_physical_address(logical_address):
    return logical_address % RAM_SIZE  # Simple modulo to simulate translation

# Memory allocation strategies

class FixedPartitioning:
    def __init__(self, memory_size, partition_size):
        self.memory_size = memory_size
        self.partition_size = partition_size
        self.num_partitions = memory_size // partition_size
        self.memory = [None] * self.num_partitions  # Each partition starts as empty

    def allocate(self, process_id, partition_index):
        if partition_index < self.num_partitions and self.memory[partition_index] is None:
            self.memory[partition_index] = process_id
            print(f"Allocated process {process_id} to partition {partition_index}")
        else:
            print(f"Partition {partition_index} is already occupied or out of range.")

    def deallocate(self, partition_index):
        if partition_index < self.num_partitions and self.memory[partition_index] is not None:
            print(f"Deallocated partition {partition_index}")
            self.memory[partition_index] = None
        else:
            print(f"Partition {partition_index} is empty or out of range.")

class VariablePartitioning:
    def __init__(self):
        self.memory = []

    def allocate(self, process_id, size):
        if sum([part[1] for part in self.memory]) + size <= RAM_SIZE:
            self.memory.append((process_id, size))  # Allocating memory for the process
            print(f"Allocated process {process_id} with size {size}")
        else:
            print(f"Not enough memory to allocate process {process_id} with size {size}")

    def deallocate(self, process_id):
        for i, (pid, _) in enumerate(self.memory):
            if pid == process_id:
                self.memory.pop(i)
                print(f"Deallocated process {process_id}")
                break
        else:
            print(f"Process {process_id} not found.")

# Paging Simulation: Divide memory into fixed-size pages
class Paging:
    def __init__(self):
        self.page_table = {}  # Maps logical page to physical frame
        self.memory = [None] * NUM_PAGES  # Frames in physical memory (RAM)

    def access_page(self, logical_address):
        page_num = logical_address // PAGE_SIZE
        if page_num in self.page_table:
            frame_num = self.page_table[page_num]
            print(f"Page {page_num} mapped to frame {frame_num}")
            return frame_num
        else:
            print(f"Page {page_num} not in memory. Performing page fault.")
            return None  # Simulate a page fault

    def load_page(self, page_num):
        empty_frame = self.find_empty_frame()
        if empty_frame is not None:
            self.page_table[page_num] = empty_frame
            self.memory[empty_frame] = page_num
            print(f"Loaded page {page_num} into frame {empty_frame}")
        else:
            print("No empty frames available for page load.")
            self.page_replacement(page_num)

    def find_empty_frame(self):
        for i in range(NUM_PAGES):
            if self.memory[i] is None:
                return i
        return None

    def page_replacement(self, page_num):
        print(f"Page replacement required for page {page_num}")
        self.page_table.clear()  # Simplified page replacement (clear entire table)

class Segmentation:
    def __init__(self):
        self.segment_table = {}  # Maps segment number to segment size
        self.memory = []

    def allocate_segment(self, segment_num, size):
        if sum(self.segment_table.values()) + size <= RAM_SIZE:
            self.segment_table[segment_num] = size
            self.memory.append((segment_num, size))
            print(f"Allocated segment {segment_num} of size {size}")
        else:
            print(f"Not enough memory for segment {segment_num} of size {size}")

    def deallocate_segment(self, segment_num):
        if segment_num in self.segment_table:
            self.memory = [seg for seg in self.memory if seg[0] != segment_num]
            del self.segment_table[segment_num]
            print(f"Deallocated segment {segment_num}")
        else:
            print(f"Segment {segment_num} not found.")

# Demand Paging and Virtual Memory
class DemandPaging:
    def __init__(self):
        self.page_table = {}  # Logical pages -> Physical frames
        self.virtual_memory = [None] * RAM_SIZE  # Virtual memory space
        self.physical_memory = [None] * RAM_SIZE  # Physical memory (RAM)

    def page_fault(self, logical_address):
        page_num = logical_address // PAGE_SIZE
        if page_num not in self.page_table:
            print(f"Page fault: Page {page_num} is not in physical memory.")
            self.load_page(page_num)
        else:
            print(f"Page {page_num} is in physical memory.")

    def load_page(self, page_num):
        free_frame = self.find_free_frame()
        if free_frame is not None:
            self.page_table[page_num] = free_frame
            self.physical_memory[free_frame] = page_num
            print(f"Page {page_num} loaded into physical memory frame {free_frame}")
        else:
            print("Physical memory is full, performing page replacement.")
            self.page_replacement(page_num)

    def find_free_frame(self):
        for i in range(len(self.physical_memory)):
            if self.physical_memory[i] is None:
                return i
        return None

    def page_replacement(self, page_num):
        print(f"Replacing page {page_num} in physical memory")
        self.page_table.clear()  # Simple clear (FIFO replacement in this case)

# Page Replacement Algorithms

class PageReplacement:
    def __init__(self):
        self.pages = []
        self.page_table = {}

    def fifo(self, page_sequence):
        print("\nFIFO Page Replacement Algorithm")
        for page in page_sequence:
            if page not in self.page_table:
                if len(self.page_table) >= NUM_PAGES:
                    # Replace the oldest page
                    oldest_page = self.pages.pop(0)
                    self.page_table.pop(oldest_page)
                    print(f"Page {oldest_page} removed.")
                self.page_table[page] = True
                self.pages.append(page)
                print(f"Page {page} added to memory.")

    def optimal(self, page_sequence):
        print("\nOptimal Page Replacement Algorithm")
        for i, page in enumerate(page_sequence):
            if page not in self.page_table:
                if len(self.page_table) < NUM_PAGES:
                    self.page_table[page] = True
                else:
                    # Find the page that will not be used for the longest time in the future
                    farthest_use = -1
                    page_to_replace = None
                    for p in self.page_table.keys():
                        try:
                            next_use = page_sequence[i+1:].index(p)
                        except ValueError:
                            next_use = float('inf')
                        if next_use > farthest_use:
                            farthest_use = next_use
                            page_to_replace = p
                    self.page_table.pop(page_to_replace)
                    self.page_table[page] = True
                print(f"Page {page} added to memory.")

    def lru(self, page_sequence):
        print("\nLRU Page Replacement Algorithm")
        page_order = deque()
        for page in page_sequence:
            if page not in page_order:
                if len(page_order) >= NUM_PAGES:
                    removed_page = page_order.popleft()
                    print(f"Page {removed_page} removed from memory.")
                page_order.append(page)
            print(f"Page {page} added to memory.")

# Simulation to test the memory management techniques

def memory_management_simulation():
    # Fixed Partitioning
    print("Fixed Partitioning:")
    fixed_partition = FixedPartitioning(RAM_SIZE, 4)
    fixed_partition.allocate("Process1", 0)
    fixed_partition.allocate("Process2", 1)
    fixed_partition.deallocate(0)

    # Variable Partitioning
    print("\nVariable Partitioning:")
    variable_partition = VariablePartitioning()
    variable_partition.allocate("Process3", 6)
    variable_partition.allocate("Process4", 5)
    variable_partition.deallocate("Process3")

    # Paging
    print("\nPaging Simulation:")
    paging = Paging()
    paging.load_page(0)
    paging.load_page(1)
    paging.access_page(4)

    # Segmentation
    print("\nSegmentation Simulation:")
    segmentation = Segmentation()
    segmentation.allocate_segment(1, 5)
    segmentation.deallocate_segment(1)

    # Demand Paging
    print("\nDemand Paging and Virtual Memory:")
    demand_paging = DemandPaging()
    demand_paging.page_fault(2)
    demand_paging.page_fault(5)
    demand_paging.page_fault(2)

    # Page Replacement Algorithms
    page_sequence = [1, 2, 3, 4, 1, 5, 1, 2]
    page_replacement = PageReplacement()
    page_replacement.fifo(page_sequence)
    page_replacement.optimal(page_sequence)
    page_replacement.lru(page_sequence)

if __name__ == "__main__":
    memory_management_simulation()
