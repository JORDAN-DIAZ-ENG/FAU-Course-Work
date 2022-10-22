
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @author: Michael Mesquita | Midlight25
    Date: 6/21/2021

    Description: Simulates round-robin process scheduling.

    License: MIT (c) Midlight25 2021
"""
# %%
# Common Libraries
from collections import deque
from typing import Deque, List
from matplotlib import pyplot as plt


class Process:
    """
        Process

        A class for process units. Used to store individual information about
        each process.
    """

    def __init__(self, burst_time: int = 0):
        # CPU Burst units left to complete
        self.burst_time: int = burst_time

        # Total time process spends in "Ready queue"
        self.wait_time: int = 0

        # Last time unit process was accessed, used to calculate
        # total time in waiting state.
        self._last_accessed: int = 0

        # State of the process, false once it's completed.
        self.running: bool = True

    def run(self, processing_time: int = 0,
            global_clock: int = 0) -> int:
        """Run the process by subtracting the alloted processing time
            from the remaining burst time, and update the PCB metadata.

            Returns unused processing time as a positive int."""

        if self.running:
            # Calculate waiting time against global process and save
            self.wait_time += (global_clock - self._last_accessed)

            # Remove alloted processsing time from burst time.
            self.burst_time -= processing_time

            # If self.burst_time is negative, that means the process has
            # finished and that there is unused time. Cast as positive integer
            # for the return and for the logic below.
            unused_time: int = abs(min(self.burst_time, 0))

            # Check for process termination state.
            self.running = self.burst_time > 0

            # Rollback clock using unused time if there is any
            self._last_accessed = (global_clock + processing_time)
            self._last_accessed -= unused_time

            # Return unused time as positive integer
            return unused_time
        else:
            return processing_time

    def __repr__(self):
        return f"Process(burst={self.burst_time}, wait={self.wait_time})"

    @property
    def turnaround_time(self) -> int:
        if not self.running:
            return self._last_accessed
        else:
            raise Exception("Process has not terminated yet.")

    def __bool__(self):
        return self.running


# %%
if __name__ == "__main__":

    # Define bursts to generate processes
    process_bursts: List[int] = [5, 4, 2, 7, 3]

    t_waits: List[float] = []
    t_turns: List[float] = []

    time_quanta_range = range(1, 8)

    for time_quanta in time_quanta_range:

        # Instantiate Round Robin queue
        process_queue: Deque[Process] = deque()

        avg_wait: float = 0
        avg_turnaround: float = 0

        # Generate processes from list and add to queue.
        for burst in process_bursts:
            process_queue.append(Process(burst))

        # Instantiate global clock to keep accurate wait and
        # turnaround times.
        clock = 0

        # Using this later to calculate average times for time
        # quantum.
        number_processes: int = len(process_queue)

        # Main processing loop
        while len(process_queue) > 0:

            # Get process at front of queue
            process = process_queue[0]

            # Run process
            unused_time: int = process.run(time_quanta, clock)

            # Increment global clock based on time_quanta used by
            # process
            clock += (time_quanta - unused_time)

            # Check running state of the process, it will be removed from list
            # or moved to the back of the queue if it's not yet done.
            if not process:

                avg_turnaround += process.turnaround_time
                avg_wait += process.wait_time

                # Remove process from queue
                process_queue.popleft()

            else:
                process_queue.rotate(-1)

        avg_wait /= number_processes
        avg_turnaround /= number_processes

        print(
            f"For time-quanta {time_quanta}:",
            f"Tw {avg_wait} and Tr {avg_turnaround} | Clock: {clock}")

        t_waits.append(avg_wait)
        t_turns.append(avg_turnaround)

    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    fig = plt.figure(figsize=(12, 4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.plot(time_quanta_range, t_waits)
    ax1.set_title("Avg Waits")
    ax1.set_xlabel("Time Quanta")

    ax2.plot(time_quanta_range, t_turns)
    ax2.set_title("Avg Turnaround Times")
    ax2.set_xlabel("Time Quanta")