# Introduction: Operating systems (OS) definition, Multiprogramming and Time Sharingoperating systems, real time OS, Multiprocessor operating systems, Multicore operating systems,Various computing environments.

import time
import random
from threading import Thread, Lock

# Simulate Resource Allocation and Management
class ResourceManager:
    def __init__(self):
        self.cpu_lock = Lock()
        self.memory_lock = Lock()
        self.disk_lock = Lock()

    def allocate_cpu(self, process_name):
        with self.cpu_lock:
            print(f"Allocating CPU to {process_name}")
            time.sleep(random.uniform(0.5, 2))  # Simulate CPU allocation delay

    def allocate_memory(self, process_name):
        with self.memory_lock:
            print(f"Allocating Memory to {process_name}")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate memory allocation delay

    def allocate_disk(self, process_name):
        with self.disk_lock:
            print(f"Allocating Disk resources to {process_name}")
            time.sleep(random.uniform(1, 3))  # Simulate disk allocation delay

class OperatingSystem:
    def __init__(self, os_type, name):
        self.os_type = os_type
        self.name = name
        self.resource_manager = ResourceManager()
        self.processes = []

    def start_process(self, process_name):
        print(f"Starting process: {process_name} on {self.name}")
        process_thread = Thread(target=self.run_process, args=(process_name,))
        process_thread.start()
        self.processes.append(process_thread)

    def run_process(self, process_name):
        print(f"Running process: {process_name} on {self.name}")
        self.resource_manager.allocate_cpu(process_name)
        self.resource_manager.allocate_memory(process_name)
        self.resource_manager.allocate_disk(process_name)
        print(f"Process {process_name} completed.")

    def monitor_system(self):
        print(f"Monitoring system health of {self.name}")
        for process in self.processes:
            process.join()  # Wait for all processes to complete

    def display_info(self):
        print(f"Operating System: {self.name}")
        print(f"OS Type: {self.os_type}")

# Simulate different OS types
class Multiprogramming(OperatingSystem):
    def __init__(self, name):
        super().__init__('Multiprogramming', name)

    def manage_processes(self, processes):
        print(f"{self.name} is managing multiple processes.")
        for process in processes:
            self.start_process(process)

class TimeSharing(OperatingSystem):
    def __init__(self, name):
        super().__init__('Time Sharing', name)

    def allocate_cpu_time(self, processes):
        print(f"{self.name} is allocating CPU time slices.")
        for process in processes:
            self.start_process(process)

class RealTimeOS(OperatingSystem):
    def __init__(self, name):
        super().__init__('Real-Time OS', name)

    def allocate_resources_for_critical_tasks(self, processes):
        print(f"{self.name} is processing critical real-time tasks.")
        for process in processes:
            self.start_process(process)

class MultiprocessorOS(OperatingSystem):
    def __init__(self, name):
        super().__init__('Multiprocessor OS', name)

    def coordinate_processors(self, processes):
        print(f"{self.name} is coordinating multiple processors.")
        for process in processes:
            self.start_process(process)

class MulticoreOS(OperatingSystem):
    def __init__(self, name):
        super().__init__('Multicore OS', name)

    def optimize_multithreading(self, processes):
        print(f"{self.name} is optimizing multithreading.")
        for process in processes:
            self.start_process(process)

# Computing Environments for System Interaction
class ComputingEnvironment:
    def __init__(self, environment_type, description):
        self.environment_type = environment_type
        self.description = description

    def simulate_environment(self):
        print(f"Simulating {self.environment_type} environment.")
        print(f"Description: {self.description}")

# Performance Benchmarking
class PerformanceBenchmark:
    def __init__(self):
        self.start_time = time.time()

    def stop_benchmark(self):
        end_time = time.time()
        print(f"Benchmark duration: {end_time - self.start_time:.2f} seconds")

# Running a simulation and benchmarking
def simulate_system():
    benchmark = PerformanceBenchmark()

    # Define processes
    processes = ['Process_1', 'Process_2', 'Process_3', 'Process_4']

    # Simulate different OS types
    linux_mp = Multiprogramming("Linux")
    linux_mp.display_info()
    linux_mp.manage_processes(processes)

    windows_ts = TimeSharing("Windows")
    windows_ts.display_info()
    windows_ts.allocate_cpu_time(processes)

    vxworks_rt = RealTimeOS("VxWorks")
    vxworks_rt.display_info()
    vxworks_rt.allocate_resources_for_critical_tasks(processes)

    aix_mp = MultiprocessorOS("AIX")
    aix_mp.display_info()
    aix_mp.coordinate_processors(processes)

    ubuntu_mc = MulticoreOS("Ubuntu")
    ubuntu_mc.display_info()
    ubuntu_mc.optimize_multithreading(processes)

    # Simulating computing environments
    cloud_env = ComputingEnvironment("Cloud Computing", "On-demand resource provision via the internet.")
    cloud_env.simulate_environment()

    distributed_env = ComputingEnvironment("Distributed Computing", "Distributing tasks across multiple machines.")
    distributed_env.simulate_environment()

    network_env = ComputingEnvironment("Networked Computing", "Shared resources over a network.")
    network_env.simulate_environment()

    # Stop the benchmark
    benchmark.stop_benchmark()

if __name__ == "__main__":
    simulate_system()

