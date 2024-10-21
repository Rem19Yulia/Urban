import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line: 
                break
            all_data.append(line.strip())  

if __name__ == '__main__':
    filenames = [f'./file 1.txt, file 2.txt, file 3.txt, file 4.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"{linear_time:.6f} (линейный)")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_time = time.time() - start_time
    print(f"{parallel_time:.6f} (многопроцессный)")