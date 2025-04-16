import gevent
from gevent.queue import Queue, Empty
import time
import random
import logging

# === Logging Setup ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%H:%M:%S"
)

# === Configuration ===
NUM_TASKS = 20
NUM_WORKERS = 3
QUEUE_MAX_SIZE = 5

# Shared task queue
tasks = Queue(maxsize=QUEUE_MAX_SIZE)

# Worker function
def worker(name):
    logger = logging.getLogger(f"Worker-{name}")
    try:
        while True:
            task = tasks.get(timeout=2)  # Wait up to 2s for a task
            logger.info(f"🛠️  Got task: {task}")
            gevent.sleep(random.uniform(0.5, 1.5))  # Simulate work time
            logger.info(f"✅ Finished task: {task}")
    except Empty:
        logger.info("🛑 No more tasks. Shutting down.")

# Boss function (task producer)
def boss():
    logger = logging.getLogger("Boss")
    logger.info(f"🧠 Assigning {NUM_TASKS} tasks...")
    for i in range(1, NUM_TASKS + 1):
        tasks.put(i)
        logger.info(f"📦 Put task {i} into the queue")
        gevent.sleep(random.uniform(0.1, 0.3))  # Simulate task creation delay
    logger.info("📣 All tasks assigned!")

# Spawn boss and workers
def main():
    workers = [gevent.spawn(worker, name) for name in ["Steve", "John", "Bob"][:NUM_WORKERS]]
    all_greenlets = [gevent.spawn(boss)] + workers
    gevent.joinall(all_greenlets)

    logging.getLogger("System").info("🎉 All tasks completed and workers have shut down.")

if __name__ == "__main__":
    main()
