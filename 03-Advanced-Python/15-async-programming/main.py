# Async Programming in Python

import asyncio
import time

print("=== Basic Async Function ===")

async def say_hello():
    """Simple async function (coroutine)"""
    print("Hello")
    await asyncio.sleep(1)  # Simulate async operation
    print("World")

# Run coroutine
print("Running async function:")
asyncio.run(say_hello())

print("\n=== Multiple Async Functions ===")

async def fetch_data(task_id, delay):
    """Simulate fetching data"""
    print(f"Task {task_id}: Starting")
    await asyncio.sleep(delay)
    print(f"Task {task_id}: Completed")
    return f"Data from task {task_id}"

async def main():
    """Main async function"""
    print("Starting multiple tasks...")
    result1 = await fetch_data(1, 1)
    result2 = await fetch_data(2, 1)
    print(f"Results: {result1}, {result2}")

print("Sequential execution:")
asyncio.run(main())

print("\n=== Concurrent Execution ===")

async def concurrent_main():
    """Run tasks concurrently"""
    print("Starting concurrent tasks...")
    start_time = time.time()
    
    # Run tasks concurrently
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 2),
        fetch_data(3, 2)
    )
    
    elapsed = time.time() - start_time
    print(f"All tasks completed in {elapsed:.2f} seconds")
    print(f"Results: {results}")

print("Concurrent execution:")
asyncio.run(concurrent_main())

print("\n=== Creating Tasks ===")

async def task_example():
    """Example of creating and managing tasks"""
    print("Creating tasks...")
    
    # Create tasks
    task1 = asyncio.create_task(fetch_data(1, 1))
    task2 = asyncio.create_task(fetch_data(2, 1))
    
    # Do other work while tasks run
    print("Tasks created, doing other work...")
    await asyncio.sleep(0.5)
    
    # Wait for tasks to complete
    result1 = await task1
    result2 = await task2
    
    print(f"Task results: {result1}, {result2}")

asyncio.run(task_example())

print("\n=== Async Context Manager ===")

class AsyncResource:
    """Async context manager"""
    async def __aenter__(self):
        print("Acquiring resource...")
        await asyncio.sleep(0.1)  # Simulate async setup
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource...")
        await asyncio.sleep(0.1)  # Simulate async cleanup
        return False
    
    async def do_work(self):
        print("Doing work with resource...")
        await asyncio.sleep(0.5)

async def context_manager_example():
    async with AsyncResource() as resource:
        await resource.do_work()

asyncio.run(context_manager_example())

print("\n=== Async Generator ===")

async def async_counter(n):
    """Async generator"""
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def generator_example():
    print("Async generator values:")
    async for value in async_counter(5):
        print(f"  {value}")

asyncio.run(generator_example())

print("\n=== Error Handling in Async ===")

async def might_fail(task_id, should_fail=False):
    """Async function that might fail"""
    await asyncio.sleep(0.5)
    if should_fail:
        raise ValueError(f"Task {task_id} failed")
    return f"Task {task_id} succeeded"

async def error_handling_example():
    """Handle errors in async code"""
    try:
        results = await asyncio.gather(
            might_fail(1, False),
            might_fail(2, True),  # This will fail
            might_fail(3, False),
            return_exceptions=True  # Return exceptions instead of raising
        )
        print("Results:")
        for i, result in enumerate(results, 1):
            if isinstance(result, Exception):
                print(f"  Task {i}: Error - {result}")
            else:
                print(f"  Task {i}: {result}")
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(error_handling_example())

print("\n=== Async with Timeout ===")

async def slow_operation():
    """Slow async operation"""
    await asyncio.sleep(2)
    return "Operation completed"

async def timeout_example():
    """Example with timeout"""
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=1.0)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("Operation timed out")

asyncio.run(timeout_example())

print("\n=== Async Queue ===")

async def producer(queue, n):
    """Produce items and put them in queue"""
    for i in range(n):
        await asyncio.sleep(0.1)
        await queue.put(i)
        print(f"Produced: {i}")
    await queue.put(None)  # Signal completion

async def consumer(queue):
    """Consume items from queue"""
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        await asyncio.sleep(0.2)

async def queue_example():
    """Producer-consumer pattern with async queue"""
    queue = asyncio.Queue()
    
    # Run producer and consumer concurrently
    await asyncio.gather(
        producer(queue, 5),
        consumer(queue)
    )

asyncio.run(queue_example())

print("\n=== Async Lock ===")

async def worker(lock, worker_id):
    """Worker that uses lock"""
    async with lock:
        print(f"Worker {worker_id} acquired lock")
        await asyncio.sleep(0.5)
        print(f"Worker {worker_id} released lock")

async def lock_example():
    """Example of async lock"""
    lock = asyncio.Lock()
    
    # Multiple workers compete for lock
    await asyncio.gather(
        worker(lock, 1),
        worker(lock, 2),
        worker(lock, 3)
    )

asyncio.run(lock_example())

