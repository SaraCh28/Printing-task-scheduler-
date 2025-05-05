# Step 1: Get number of printing tasks
n = int(input("Enter number of print jobs: "))

# Step 2: Input arrival time and printing time (burst time) for each job
print_jobs = []

for i in range(n):
    job_id = i + 1
    arrival = int(input(f"Enter arrival time for print job {job_id}: "))
    burst = int(input(f"Enter printing time (burst) for job {job_id}: "))
    print_jobs.append({
        "job_id": job_id,
        "arrival_time": arrival,
        "burst_time": burst,
        "completion_time": 0,
        "turnaround_time": 0,
        "waiting_time": 0
    })

# Step 3: Sort the print jobs based on arrival time
print_jobs.sort(key=lambda x: x["arrival_time"])

# Step 4: Schedule the print jobs using FCFS
current_time = 0
total_waiting_time = 0
total_turnaround_time = 0

for job in print_jobs:
    # If printer is idle, fast forward time
    if current_time < job["arrival_time"]:
        current_time = job["arrival_time"]
    
    job["completion_time"] = current_time + job["burst_time"]
    job["turnaround_time"] = job["completion_time"] - job["arrival_time"]
    job["waiting_time"] = job["turnaround_time"] - job["burst_time"]
    
    # Update current time
    current_time = job["completion_time"]
    
    # Add to totals for average calculation
    total_waiting_time += job["waiting_time"]
    total_turnaround_time += job["turnaround_time"]

# Step 5: Sort back by Job ID for neat output
print_jobs.sort(key=lambda x: x["job_id"])

# Step 6: Display the results
print("\n" + "-" * 70)
print("Job ID | Arrival | Print Time | Completion | Turnaround | Waiting")
print("-" * 70)
for job in print_jobs:
    print(f"{job['job_id']:>6} |"
          f"{job['arrival_time']:>8} |"
          f"{job['burst_time']:>11} |"
          f"{job['completion_time']:>11} |"
          f"{job['turnaround_time']:>11} |"
          f"{job['waiting_time']:>7}")
print("-" * 70)

# Step 7: Calculate and display averages
avg_waiting = total_waiting_time / n
avg_turnaround = total_turnaround_time / n

print(f"\nAverage Waiting Time   : {avg_waiting:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")
