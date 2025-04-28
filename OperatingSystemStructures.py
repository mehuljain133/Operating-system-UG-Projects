# Operating System Structures: Operating Systems services, System calls and System programs,operating system architecture (Micro Kernel, client server) operating

import time
import random
from threading import Thread, Lock

# Operating System Services
class OperatingSystemServices:
    def __init__(self):
        self.process_lock = Lock()
        self.memory_lock = Lock()
        self.device_lock = Lock()
        self.file_lock = Lock()

    def manage_process(self, process_name):
        with self.process_lock:
            print(f"Managing process {process_name}")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate process management delay

    def manage_memory(self, process_name):
        with self.memory_lock:
            print(f"Managing memory for {process_name}")
            time.sleep(random.uniform(0.5, 1.0))  # Simulate memory allocation delay

    def manage_device(self, device_name):
        with self.device_lock:
            print(f"Managing device: {device_name}")
            time.sleep(random.uniform(0.5, 1.0))  # Simulate device management delay

    def manage_files(self, file_name):
        with self.file_lock:
            print(f"Managing file: {file_name}")
            time.sleep(random.uniform(0.5, 2))  # Simulate file management delay

# System Calls (Interface for OS functionality)
class SystemCalls:
    def __init__(self, os_service):
        self.os_service = os_service

    def create_process(self, process_name):
        print(f"System Call: Creating process {process_name}")
        self.os_service.manage_process(process_name)

    def allocate_memory(self, process_name):
        print(f"System Call: Allocating memory for {process_name}")
        self.os_service.manage_memory(process_name)

    def open_file(self, file_name):
        print(f"System Call: Opening file {file_name}")
        self.os_service.manage_files(file_name)

    def access_device(self, device_name):
        print(f"System Call: Accessing device {device_name}")
        self.os_service.manage_device(device_name)

# System Programs (User level programs interacting with the OS)
class SystemPrograms:
    def __init__(self, system_calls):
        self.system_calls = system_calls

    def run_program(self, program_name, process_name, file_name, device_name):
        print(f"Running program: {program_name}")
        self.system_calls.create_process(process_name)
        self.system_calls.open_file(file_name)
        self.system_calls.access_device(device_name)
        print(f"Program {program_name} executed successfully.")

# Operating System Architecture - Microkernel Model
class MicroKernelOS:
    def __init__(self, os_services):
        self.os_services = os_services

    def start_kernel_services(self):
        print("Starting Microkernel OS services.")
        # Only the essential services are running in the kernel
        print("Process management, memory management, device management are handled by microkernel.")

    def user_services(self):
        print("User services (e.g., file system, network) run in user space.")

# Operating System Architecture - Client-Server Model
class ClientServerOS:
    def __init__(self, os_services):
        self.os_services = os_services

    def start_server(self):
        print("Starting Client-Server OS services.")
        print("OS is running as a server, providing resources to clients.")

    def client_request(self, request_type, data):
        print(f"Client request: {request_type} for {data}")
        # The OS server handles the request (via system calls)
        if request_type == 'process':
            self.os_services.manage_process(data)
        elif request_type == 'memory':
            self.os_services.manage_memory(data)
        elif request_type == 'file':
            self.os_services.manage_files(data)
        elif request_type == 'device':
            self.os_services.manage_device(data)
        print(f"Request {request_type} processed for {data}")

# Simulation of OS services, system calls, and programs
def simulate_os():
    # Create Operating System Services
    os_service = OperatingSystemServices()

    # Create System Calls Interface
    system_calls = SystemCalls(os_service)

    # Create System Programs interacting with System Calls
    system_program = SystemPrograms(system_calls)

    # Create Microkernel OS
    micro_kernel_os = MicroKernelOS(os_service)
    micro_kernel_os.start_kernel_services()
    micro_kernel_os.user_services()

    # Create Client-Server OS
    client_server_os = ClientServerOS(os_service)
    client_server_os.start_server()

    # Simulate running programs in the OS
    system_program.run_program("Editor", "Process_1", "file1.txt", "Disk_1")
    system_program.run_program("Browser", "Process_2", "file2.html", "Network_Device")

    # Simulate client-server communication
    client_server_os.client_request('process', 'Process_3')
    client_server_os.client_request('file', 'file3.log')
    client_server_os.client_request('device', 'Printer')

if __name__ == "__main__":
    simulate_os()

