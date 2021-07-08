import concurrent.futures
import random
import time

import os


def some_logic(sec):
    print("Start execution")
    time.sleep(sec)
    print(f"End execution for {sec}")
    r = random.randint(1, 1000)
    print(f"Process id: {os.getpid()}, random num = {r}")
    return r


if __name__ == '__main__':
    # with multiprocessing.Pool(2) as p:
    #     a = [1, 2, 3]
    #     p.map(some_logic, a)
    # q = multiprocessing.Queue()
    # processes = [multiprocessing.Process(target=some_logic, args=(i, q)) for i in range(1, 32)]
    # for process in processes:
    #     process.start()
    #
    # for process in processes:
    #     process.join()
    #     print(q.get())

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     results = [executor.submit(some_logic, i) for i in [10, 3, 13, 2, 5, 7, 16]]
    #     for result in results:
    #         print(result)
    #     for f in concurrent.futures.as_completed(results):
    #         print(f.result())
    #
    # print(f"Finished in {time.perf_counter()} sec")

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(some_logic, [10, 3, 13, 2, 5, 7, 16])
        for result in results:
            print(result)

    print(f"Finished in {time.perf_counter()} sec")

# 1 - 100000000000000000000
# количество процессов CPUCore * 2


def prostie_chisla(n, k):
    pros_chisla = []
    for number in range(n, k+1):
        for devider in range(2,k):
            if number % devider == 0:
                break
        else:
            pros_chisla.append(number)
