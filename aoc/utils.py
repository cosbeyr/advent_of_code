from datetime import datetime as dt
import os
from aocd import get_data

def build(day=None, year=None, return_data=False): 
    day = day if day is not None else dt.now().day
    year = year if year is not None else dt.now().year

    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, f'{year}', f'{day}')
    datapath = os.path.join(path, 'data.txt')

    if os.path.exists(path):
        print(f'Reading data: {path}')
        if return_data:
            with open(datapath, 'r') as f:
                data = f.read().splitlines()
                return data
        return 

    print(f'Building {year}/{day}: {path}')
    os.makedirs(path)
    data = get_data(day=day, year=year)
    with open(datapath, 'w') as f:
        f.write(data)

    answerpath = os.path.join(path, 'answer.txt')
    with open(answerpath, 'w') as f:
        f.write(f'# {year} - Day {day}')

    solutionpath = os.path.join(path, 'solution.py')
    with open(solutionpath, 'w') as f:
        f.write(f'\ndef day{day}_1(data):\n    raise NotImplementedError\n')
        f.write(f'\ndef day{day}_2(data):\n    raise NotImplementedError\n')

    if return_data:
        return data


def write_solution(filepath, answer, part):
    with open(filepath, 'a') as f:
        f.write(f'### Part {part}: {answer}\n')
