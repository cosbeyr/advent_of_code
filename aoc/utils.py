from datetime import datetime as dt
import os
from aocd import get_data


def get_date(year, day):
    year = year if year is not None else dt.now().year
    day = day if day is not None else dt.now().day
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, f'{year}', f'{day}')
    return year, day, path 


def build(year=None, day=None, return_data=False): 
    year, day, path = get_date(year, day)
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
    data = get_data(year=year, day=day)
    data = data.splitlines()
    with open(datapath, 'w') as f:
        f.write('\n'.join(data))

    solutionpath = os.path.join(path, 'solution.py')
    with open(solutionpath, 'w') as f:
        f.write(f'\ndef day{day}_1(data):\n    raise NotImplementedError\n')
        f.write(f'\ndef day{day}_2(data):\n    raise NotImplementedError\n')

    if return_data:
        return data


def write_answer(answer, year=None, day=None):
    year, day, path = get_date(year, day)
    
    assert os.path.exists(path), f'Error! Year / Day entered ({year} / {day}) do not exist'

    answerpath = os.path.join(path, 'answer.txt')
    if not os.path.exists(answerpath):
        answer_str = '# {year} - Day {day}\n### Part 1: {answer}'
    else:
        answer_str = '### Part 2: {answer}'
    with open(answerpath, 'a') as f:
        f.write(answer_str)
