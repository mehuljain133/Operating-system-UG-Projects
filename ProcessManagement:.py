# Process Management: Process concept, Operation on processes, Multi-threaded processes andmodels, Multicore systems, Process scheduling algorithms, Process synchronization. TheCritical-section problem and deadlock characterization, deadlock handling

import threading
import time
import random
from queue import Queue

# Process class to simulate a process in the system
class Process:
    def __init__(self, pid, burst_time, priority=0):
        self.pid = pid  # Process ID
        self.burst_time = burst_time  # CPU burst time
        self.priority = priority  # Process priority
        self.state = "New"  # Initial state

    def run(self):
        self.state = "Running"
        print(f"Process {self.pid} is running for {self.burst_time} seconds.")
        time.sleep(self.burst_time)  # Simulate the burst time
        self.state = "Terminated"
        print(f"Process {self.pid} terminated.")

# Process Scheduler class simulates process scheduling algorithms
class ProcessScheduler:
    def __init__(self):
        self.process_queue = Queue()  # Queue to manage processes
        self.lock = threading.Lock()  # Lock to avoid race conditions

    def add_process(self, process):
        self.process_queue.put(process)

    def round_robin(self, time_quantum):
        print("Using Round Robin Scheduling...")
        while not self.process_queue.empty():
            process = self.process_queue.get()
            if process.burst_time > time_quantum:
                process.burst_time -= time_quantum
                print(f"Process {process.pid} executed for {time_quantum} seconds. Remaining time: {process.burst_time}")
                self.process_queue.put(process)  # Re-queue the process
            else:
                process.run()

    def priority_scheduling(self):
        print("Using Priority Scheduling...")
        processes = list(self.process_queue.queue)
        processes.sort(key=lambda x: x.priority)  # Sort by priority (lowest priority first)
        for process in processes:
            process.run()

# Synchronization Mechanism: Mutex lock for critical section handling
class CriticalSection:
    def __init__(self):
        self.lock = threading.Lock()
        self.shared_data = 0

    def increment(self, thread_name):
        with self.lock:
            print(f"{thread_name} is in the critical section.")
            self.shared_data += 1
            print(f"Shared data incremented to {self.shared_data} by {thread_name}")
            time.sleep(random.uniform(0.1, 0.5))  # Simulate some work
            print(f"{thread_name} is leaving the critical section.")

# Deadlock Simulation: Simple resource allocation and deadlock detection
class DeadlockSimulation:
    def __init__(self):
        self.resources = {1: 1, 2: 1}  # Resources with 1 unit each
        self.waiting_queue = Queue()  # Queue for processes waiting for resources

    def request_resource(self, process_id, resource_id):
        if self.resources[resource_id] > 0:
            self.resources[resource_id] -= 1  # Resource allocated
            print(f"Process {process_id} acquired resource {resource_id}.")
        else:
            print(f"Process {process_id} is waiting for resource {resource_id}.")
            self.waiting_queue.put(process_id)  # Process waits in queue

    def release_resource(self, process_id, resource_id):
        self.resources[resource_id] += 1  # Resource released
        print(f"Process {process_id} released resource {resource_id}.")
        if not self.waiting_queue.empty():
            next_process = self.waiting_queue.get()
            print(f"Process {next_process} is now acquiring resource {resource_id}.")
            self.request_resource(next_process, resource_id)

# Simulate multi-threaded process execution
def simulate_threads():
    print("Starting multi-threaded process simulation.")
    
    # Create a few processes with burst time and priority
    processes = [
        Process(pid=1, burst_time=3, priority=2),
        Process(pid=2, burst_time=5, priority=1),
        Process(pid=3, burst_time=2, priority=3)
    ]
    
    # Create a Process Scheduler
    scheduler = ProcessScheduler()
    
    # Add processes to the scheduler
    for process in processes:
        scheduler.add_process(process)
    
    # Start Round Robin Scheduling with a time quantum of 2 seconds
    scheduler.round_robin(time_quantum=2)
    
    # Start Priority Scheduling
    scheduler.priority_scheduling()

# Simulate process synchronization
def simulate_critical_section():
    print("Simulating Critical Section Handling.")
    
    # Create a CriticalSection instance
    cs = CriticalSection()
    
    # Create threads to simulate the critical section access
    thread_1 = threading.Thread(target=cs.increment, args=("Thread-1",))
    thread_2 = threading.Thread(target=cs.increment, args=("Thread-2",))
    
    # Start the threads
    thread_1.start()
    thread_2.start()
    
    # Wait for threads to finish
    thread_1.join()
    thread_2.join()

# Simulate deadlock handling
def simulate_deadlock():
    print("Simulating Deadlock Handling.")
    
    # Create a DeadlockSimulation instance
    deadlock = DeadlockSimulation()
    
    # Request resources for processes
    deadlock.request_resource(process_id=1, resource_id=1)
    deadlock.request_resource(process_id=2, resource_id=1)
    
    # Release resources
    deadlock.release_resource(process_id=1, resource_id=1)
    deadlock.release_resource(process_id=2, resource_id=1)

if __name__ == "__main__":
    # Simulate Threaded Process Scheduling
    simulate_threads()

    # Simulate Critical Section Handling (Synchronization)
    simulate_critical_section()

    # Simulate Deadlock Handling
    simulate_deadlock()
