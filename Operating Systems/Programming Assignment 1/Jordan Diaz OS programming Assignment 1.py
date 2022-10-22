from enum import Enum


class State(Enum):
    """This Enum holds the states of the processes in the process life cycle"""
    New = 0
    Ready = 1
    Running = 2
    Waiting = 3
    Terminated = 4


def calculate_turnaround_time(process):
    """ Calculates the turnaround time for a single process"""
    return abs(process.terminated_time - process.arrived_time)


def calculate_waiting_time(process):
    """ Calculates the waiting time for a single process"""
    total_burst = 0
    for burst in process.burst_values:
        total_burst += burst
    return abs(calculate_turnaround_time(process) - total_burst)


def calculate_response_time(process):
    """ Calculates the response time for a single process"""
    return abs(process.started_time - process.arrived_time)


def calculate_cpu_utilization(os):
    """ Calculates the cpu utilization of an entire process life cycle"""
    return (os.used_cpu_time / os.total_cpu_time) * 100


class ProcessLifeCycle(object):
    """ Controls the flow of processes and their states described as a process life cycle"""

    def __init__(self, all_processes, scheduling_method_str):
        self.current_process = None
        self.terminated_processes = []
        self.const_processes = all_processes
        self.processes = all_processes
        self.running_process = None
        self.ready_queue = []
        self.waiting_queue = []
        self.time = 0
        self.finished = False
        self.total_cpu_time = 0
        self.used_cpu_time = 0
        self.shortest_process = None
        self.queue1 = []
        self.queue2 = []
        self.queue3 = []
        self.scheduling_method = scheduling_method_str
        self.information_str = ""
        self.show_info = True
        for item in all_processes:
            self.new(item)  # append the ready queue
            for i in range(0, len(item.burst_values)):
                if i % 2 == 0:
                    self.used_cpu_time += item.burst_values[i]

    def new(self, process):
        """ Called for every new process"""
        self.ready_queue.append(process)
        process.state = State.Ready

    def ready(self, process):
        """ Manages the ready queue, chooses scheduling algorithm"""
        # Schedule
        if self.scheduling_method == "FCFS":
            self.first_come_first_served(self.ready_queue[0])  # FCFS
        elif self.scheduling_method == "SJF":
            self.shortest_job_first(process)  # SJF
        elif self.scheduling_method == "MLFQ":
            self.multilevel_feedback_queue(process)  # MLFQ

    def waiting(self, process):
        """ Manages the waiting queue"""
        if process == self.current_process:
            self.information_str += "I/O BURST LEFT: " + str(process.burst) + " " + str(process.name) + "\n"
            # if final process finished
            if process.burst == 0 and process.index == process.final_index:
                process.state = State.Terminated
                self.waiting_queue.remove(process)
                self.terminated(process)
            # if process finished
            elif process.burst == 0:
                process.state = State.Ready
                process.index += 1
                process.burst = process.burst_values[process.index]
                process.is_cpu_burst = True
                self.waiting_queue.remove(process)
                self.ready_queue.append(process)
                self.ready(process)
            # if process is not finished
            elif process.burst > 0:
                process.burst -= 1

    def running(self, process):
        """ Manages the currently running process"""
        if process == self.current_process:
            self.running_process = process
            # if last process finished
            if process.burst == 0 and process.index == process.final_index:
                self.show_info = True
                process.state = State.Terminated
                self.running_process = None
                if process == self.shortest_process:
                    self.shortest_process = None
                self.terminated(process)
            # if Process finished
            elif process.burst == 0:
                self.show_info = True
                self.information_str += str(process.name) + " FINISHED CPU BURST" + "\n"
                process.state = State.Waiting
                process.index += 1
                process.burst = process.burst_values[process.index]
                process.is_cpu_burst = False
                self.running_process = None
                if process == self.shortest_process:
                    self.shortest_process = None
                self.waiting_queue.append(process)
                self.waiting(process)

            elif process.counter == 0 and process.queue_number != 3:
                # Preempt the process
                self.show_info = True
                self.information_str += str(process.name) + " PREEMPTED" + "\n"
                self.running_process = None
                process.state = State.Ready
                self.ready_queue.append(process)

                # downgrade process if cpu burst did not finish and not preempted by a higher queue level process
                if process.queue_number != 3:  # and not next_process.queue_number < process.queue_number:
                    process.queue_number += 1
                    self.information_str += str(process.name) + " Moved to Queue " + str(process.queue_number) + "\n"
                    # print(process.name, "moved to Queue", process.queue_number)

                # because this is a round robin case reset the process counter
                if len(self.ready_queue) == 1:
                    process.counter = -1
                    self.ready(process)

            elif process.burst > 0:
                if not process.started:
                    self.show_info = True
                    process.started = True
                    process.started_time = self.time - 1
                    self.information_str += str(process.name) + " Started at " + str(process.started_time) + "\n"
                process.burst -= 1
                process.counter -= 1

    def terminated(self, process):
        """ Manages terminated processes"""
        self.information_str += str(process.name) + " TERMINATED" + "\n"
        process.terminated_time = self.time - 1
        self.information_str += str(process.name) + " Terminated at " + str(process.terminated_time) + "\n"
        self.terminated_processes.append(process)

    def time_tick(self):
        """ represents a clock tick"""
        self.information_str = ""  # Used to control when text is displayed

        # Controls end times
        if len(self.processes) != len(self.terminated_processes):
            self.information_str += "Time: " + str(self.time) + "\n"
            self.time += 1  # increment timer

            # go through each process and send to their respective functions based on their state
            for process in self.processes:
                self.current_process = process
                if process.state == State.Ready:
                    self.ready(process)
                elif process.state == State.Waiting:
                    self.waiting(process)
                elif process.state == State.Running:
                    self.running(process)

            # prepare the information of the ready queue if it is to be printed
            self.information_str += "READY QUEUE" + "\n"
            for element in self.ready_queue:
                self.information_str += str(element.name) + " <----------- "
                self.information_str += "Queue " + str(element.queue_number) + ", Burst = " + str(element.burst) + "\n"

            # Reorganize list of processes
            if self.running_process is not None:
                temp = [self.running_process]

                if self.scheduling_method == "FCFS" or self.scheduling_method == "SJF":
                    for item in self.processes:
                        if item.state == State.Waiting:
                            temp.append(item)
                elif self.scheduling_method == "MLFQ":
                    for item in self.waiting_queue:
                        temp.append(item)
                for items in self.ready_queue:
                    temp.append(items)
                for more_items in self.terminated_processes:
                    temp.append(more_items)
                self.processes = temp

            self.information_str += "\n"
            # print the information
            if self.show_info:
                print(self.information_str)
                self.show_info = False
        else:
            self.total_cpu_time = self.time - 1

    def first_come_first_served(self, process):
        """ FCFS Scheduling"""
        # continue by sending to running and out of ready
        if self.running_process is None:
            self.ready_queue.remove(process)
            process.state = State.Running
            self.running(process)

    def shortest_job_first(self, process):
        """ SJF Scheduling"""
        if self.running_process is None:

            # Find shortest job through the function
            self.calculate_shortest_job()

            # continue if process is shortest process
            if process == self.shortest_process:
                self.ready_queue.remove(process)
                process.state = State.Running
                self.running(process)

    def calculate_shortest_job(self):
        """ Function that helps SFJ Scheduling"""
        # Calculate the shortest job
        shortest = self.ready_queue[0]
        for i in range(1, len(self.ready_queue)):
            if self.ready_queue[i].burst < shortest.burst:
                shortest = self.ready_queue[i]
        self.shortest_process = shortest

    def round_robin(self, process, time_quantum):
        """ RR scheduling"""
        # Same as FCFS but with time quantum
        if self.running_process is None:
            process.counter = time_quantum
            self.ready_queue.remove(process)
            process.state = State.Running
            self.running(process)

    def multilevel_feedback_queue(self, process):
        """ MLFQ Scheduling"""
        # if no running processes or if queue has higher priority
        if self.running_process is None or process.queue_number < self.running_process.queue_number:

            q1_count = 0
            q2_count = 0
            q3_count = 0

            # Count how many processes in each queue
            for element in self.ready_queue:
                if element.queue_number == 1:
                    self.queue1.append(element)
                    q1_count += 1
                elif element.queue_number == 2:
                    self.queue2.append(element)
                    q2_count += 1
                elif element.queue_number == 3:
                    self.queue3.append(element)
                    q3_count += 1

            # add to print later
            self.information_str += "QUEUES:" + "\n" + "Q1: " + str(q1_count) + "\n" + "Q2: " + str(
                q2_count) + "\n" + "Q3: " + str(
                q3_count) + "\n"

            current_queue = process.queue_number

            # If there is a process with a higher priority
            if self.running_process is not None and process.queue_number < self.running_process.queue_number:
                self.information_str += str(process.name) + " Preempted" + "\n"
                self.ready_queue.append(self.running_process)
                self.running_process.state = State.Ready
                self.running_process.counter = -1
                self.running_process.burst += 1
                self.running_process = None

            # processes will do one of the following based on what the queues look like
            if q1_count > 0 and current_queue == 1:
                self.information_str += "Queue 1 " + str(process.name) + " in Queue " + str(current_queue) + "\n"
                self.queue1.remove(process)
                self.round_robin(process, 5)
            elif q2_count > 0 and current_queue == 2 and q1_count == 0:
                self.information_str += "Queue 2 " + str(process.name) + " in Queue " + str(current_queue) + "\n"
                self.queue2.remove(process)
                self.round_robin(process, 10)
            elif q3_count > 0 and current_queue == 3 and q1_count == 0 and q2_count == 0:
                self.information_str += "Queue 1 " + str(process.name) + " in Queue " + str(current_queue) + "\n"
                self.queue3.remove(process)
                self.first_come_first_served(process)


class Process(object):
    """ Class representation of a process"""

    def __init__(self, array_of_data, name):
        self.state = State.Ready
        self.name = name
        self.burst_values = array_of_data
        self.burst = array_of_data[0]
        self.is_cpu_burst = True
        self.started = False
        self.index = 0
        self.final_index = len(array_of_data) - 1
        self.arrived_time = 0
        self.started_time = 0
        self.terminated_time = 0
        self.counter = -1
        self.queue_number = 1


def main():
    """Main Driver function"""
    time_units = 1000

    p1 = Process([5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 5], "p1")
    p2 = Process([4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8], "p2")
    p3 = Process([8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6], "p3")
    p4 = Process([3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3], "p4")
    p5 = Process([16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4], "p5")
    p6 = Process([11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8], "p6")
    p7 = Process([14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10], "p7")
    p8 = Process([4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6], "p8")

    # This is the only place you have to do anything, change |
    #                                                        |
    #                                                        v
    os = ProcessLifeCycle([p1, p2, p3, p4, p5, p6, p7, p8], "FCFS")  # type "FCFS", "SJF", or "MLFQ"

    # Run the Simulation
    for i in range(0, time_units + 1):
        os.time_tick()

    # Calculating the Results
    print("Total Time is ", os.total_cpu_time)
    print()

    print("Turn Around Time")
    avg_ttr = 0
    for process0 in os.const_processes:
        print("{}:".format(process0.name), calculate_turnaround_time(process0))
        avg_ttr += calculate_turnaround_time(process0)
    print("Average Turn Around Time: ", avg_ttr / len(os.const_processes), "ms")
    print()

    print("Waiting Time")
    avg_wt = 0
    for process1 in os.const_processes:
        print("{}:".format(process1.name), calculate_waiting_time(process1))
        avg_wt += calculate_waiting_time(process1)
    print("Average Waiting Time: ", avg_wt / len(os.const_processes), "ms")
    print()

    print("Response Time")
    avg_tr = 0
    for process2 in os.const_processes:
        print("{}:".format(process2.name), calculate_response_time(process2))
        avg_tr += calculate_response_time(process2)
    print("Average Response Time: ", avg_tr / len(os.const_processes), "ms")
    print()

    print("CPU Utilization")
    u = calculate_cpu_utilization(os)
    print(u, "%")


if __name__ == "__main__":
    main()
