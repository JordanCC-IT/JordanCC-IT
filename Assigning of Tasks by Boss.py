import gevent
from gevent.queue import Queue, Empty

tasks = Queue(maxsize=3)

def worker(name):
    try:
        while True:
            task = tasks.get(timeout=1)  # Blocks until a task is available or timeout occurs
            print('Worker %s got task %s' % (name, task))
            gevent.sleep(0)  # Yield control to other greenlets
    except Empty:
        print(f'Worker {name}: Quitting time!')

def boss():
    """
    Boss will wait to hand out work until an individual worker is
    free since the maxsize of the task queue is 3.
    """
    for i in range(1, 10):  # Replaced xrange with range for Python 3 compatibility
        tasks.put(i)
    print('Assigned all work in iteration 1')

    for i in range(10, 20):  # Replaced xrange with range for Python 3 compatibility
        tasks.put(i)
    print('Assigned all work in iteration 2')

gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'bob'),
])
