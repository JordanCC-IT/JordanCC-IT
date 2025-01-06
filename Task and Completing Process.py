from multiprocessing import Pool, Manager
import time

# Example tasks with priority, task name, and duration
tasks = [
    (3, "Task A", 5),  # Priority 3, should run last
    (1, "Task B", 2),  # Priority 1, should run first
    (2, "Task C", 3),  # Priority 2, should run second
    (4, "Task D", 1),  # Priority 4, should run last
    (5, "Task E", 0),  # Priority 5, will simulate an error
]

MAX_RETRIES = 3  # Maximum retry attempts for failed tasks

def worker(task_info):
    """Worker function to process tasks based on priority, with retries."""
    priority, task_name, duration = task_info
    attempt = 0
    success = False

    while attempt < MAX_RETRIES and not success:
        try:
            print(f"Processing {task_name} with priority {priority}, attempt {attempt + 1}, sleeping for {duration} seconds.")
            time.sleep(duration)

            # Simulate an error for a specific task (Task E)
            if task_name == "Task E" and attempt < 2:
                raise ValueError(f"Simulated error in {task_name} on attempt {attempt + 1}!")

            # Task completed successfully
            success = True
            print(f"Finished {task_name}.")
            return (task_name, "Success")
        except Exception as e:
            print(f"Error in {task_name} (Attempt {attempt + 1}): {e}")
            attempt += 1
            if attempt == MAX_RETRIES:
                print(f"Failed {task_name} after {MAX_RETRIES} attempts.")
                return (task_name, f"Failed after {MAX_RETRIES} attempts")

def handle_results(results):
    """Callback to handle the results from completed tasks."""
    print("\nAll tasks completed. Results:")
    for result in results:
        print(result)

def pool_handler():
    """Main function to handle the pool of workers and manage task prioritization."""
    with Pool(3) as pool:
        # Use pool.map to apply the worker function to each task
        results = pool.map(worker, tasks)

    # Handle results (success or failure)
    handle_results(results)

    print("\nAll tasks completed!")

if __name__ == '__main__':
    pool_handler()
