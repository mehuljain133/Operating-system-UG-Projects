# Write a program to report behaviour of Linux kernel including information on 19 configuredmemory, amount of free and used memory. (memory information)

import os

# Function to get memory information from /proc/meminfo
def get_memory_info():
    memory_info = {}

    try:
        with open("/proc/meminfo", "r") as file:
            meminfo_raw = file.readlines()
            for line in meminfo_raw:
                if line.startswith("MemTotal"):
                    memory_info["Total Memory"] = line.split(":")[1].strip()
                elif line.startswith("MemFree"):
                    memory_info["Free Memory"] = line.split(":")[1].strip()
                elif line.startswith("MemAvailable"):
                    memory_info["Available Memory"] = line.split(":")[1].strip()
                elif line.startswith("Buffers"):
                    memory_info["Buffers"] = line.split(":")[1].strip()
                elif line.startswith("Cached"):
                    memory_info["Cached"] = line.split(":")[1].strip()
                elif line.startswith("MemUsed"):
                    memory_info["Used Memory"] = str(int(memory_info.get("Total Memory", 0)) - int(memory_info.get("Free Memory", 0)))  # Calculate used memory
    except FileNotFoundError:
        return None

    return memory_info

# Main function to display system memory info
def report_memory_info():
    print("=== Linux Memory Information ===")
    
    # Get memory details
    memory_info = get_memory_info()

    if memory_info:
        print(f"Total Memory: {memory_info.get('Total Memory', 'N/A')} KB")
        print(f"Free Memory: {memory_info.get('Free Memory', 'N/A')} KB")
        print(f"Available Memory: {memory_info.get('Available Memory', 'N/A')} KB")
        print(f"Buffers: {memory_info.get('Buffers', 'N/A')} KB")
        print(f"Cached: {memory_info.get('Cached', 'N/A')} KB")
        print(f"Used Memory: {memory_info.get('Used Memory', 'N/A')} KB")
    else:
        print("Could not retrieve memory information.")

# Execute the reporting
if __name__ == "__main__":
    report_memory_info()
