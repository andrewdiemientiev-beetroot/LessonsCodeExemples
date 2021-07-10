import concurrent.futures
import threading
import time

counter = 0


def increment_counter(fake_value):
    global counter
    print(counter)
    for _ in range(100):
        counter += 1


if __name__ == '__main__':
    fake_data = [x for x in range(500000)]
    start = time.time()
    list(map(increment_counter, fake_data))
    print(counter)
    print(f'Duration: {time.time() - start} sec')

