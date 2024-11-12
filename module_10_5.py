from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            content = file.readline()
            if not content:
                break
            else:
                all_data.append(content)

def line(filenames):
    start_line = datetime.now()
    for files in filenames:
        read_info(files)
    print(f'Время работы линейного вызова : {datetime.now() - start_line}')

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    line(filenames)
    start_multiproc = datetime.now()

    with Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)

    print(f'Время работы мультипроцесса : {datetime.now() - start_multiproc}')