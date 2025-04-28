# Write a program to report behaviour of Linux kernel including kernel version, CPU type andmodel. (CPU information)

import os
import platform
import subprocess

# Function to get kernel version
def get_kernel_version():
    return platform.uname().release  # Using platform.uname() to get kernel information

# Function to get CPU information
def get_cpu_info():
    cpu_info = {}
    
    # Using `cat /proc/cpuinfo` to get CPU info
    try:
        with open("/proc/cpuinfo", "r") as file:
            cpu_info_raw = file.readlines()
            for line in cpu_info_raw:
                if line.startswith("model name"):
                    cpu_info["model_name"] = line.split(":")[1].strip()
                elif line.startswith("cpu family"):
                    cpu_info["cpu_family"] = line.split(":")[1].strip()
                elif line.startswith("cpu MHz"):
                    cpu_info["cpu_mhz"] = line.split(":")[1].strip()
                elif line.startswith("flags"):
                    cpu_info["flags"] = line.split(":")[1].strip()
    except FileNotFoundError:
        return None

    return cpu_info

# Function to get CPU architecture
def get_cpu_architecture():
    return platform.machine()

# Main function to report Linux Kernel and CPU information
def report_system_info():
    print("=== Linux Kernel and CPU Information ===")

    # Kernel Version
    kernel_version = get_kernel_version()
    print(f"Kernel Version: {kernel_version}")

    # CPU Information
    cpu_info = get_cpu_info()
    if cpu_info:
        print("\nCPU Information:")
        print(f"Model Name: {cpu_info.get('model_name', 'N/A')}")
        print(f"CPU Family: {cpu_info.get('cpu_family', 'N/A')}")
        print(f"CPU MHz: {cpu_info.get('cpu_mhz', 'N/A')} MHz")
        print(f"Flags: {cpu_info.get('flags', 'N/A')}")
    else:
        print("\nCould not retrieve CPU information.")

    # CPU Architecture
    cpu_arch = get_cpu_architecture()
    print(f"\nCPU Architecture: {cpu_arch}")

# Execute the reporting
if __name__ == "__main__":
    report_system_info()
