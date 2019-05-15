import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time
from collections import deque


def sum_overall_queue(n):
    sum = 0
    for i in range(n):
        sum += i
    print("Sum : " + str(sum))


def thread_test(queue):
    thread_1 = threading.Thread(target=sum_overall_queue(queue.popleft()))
    thread_2 = threading.Thread(target=sum_overall_queue(queue.popleft()))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()


def secvential_test(queue):
    sum_overall_queue(queue.popleft())
    sum_overall_queue(queue.popleft())


def proccess_test(queue):
    proccess_1 = multiprocessing.Process(target=sum_overall_queue(queue.popleft()))
    proccess_2 = multiprocessing.Process(target=sum_overall_queue(queue.popleft()))
    proccess_1.start()
    proccess_2.start()
    proccess_1.join()
    proccess_2.join()


def threadPool_test(queue):
    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(sum_overall_queue(queue.popleft()))
        future = executor.submit(sum_overall_queue(queue.popleft()))


if __name__ == '__main__':

    numbers = [3213, 21312]
    queue = deque()

    for i in range(4):
        for j in numbers:
            queue.append(j)

    start = time.time()
    thread_test(queue)
    end = time.time()
    print("Execution time pseudoparalelism cu GIL: " + str(end-start) + "\n")

    start = time.time()
    secvential_test(queue)
    end = time.time()
    print("Execution time secvential: " + str(end-start) + "\n")

    start = time.time()
    proccess_test(queue)
    end = time.time()
    print("Execution time multiprocessing: " + str(end-start) + "\n")

    start = time.time()
    threadPool_test(queue)
    end = time.time()
    print("Execution time concurrent futures: " + str(end-start) + "\n")