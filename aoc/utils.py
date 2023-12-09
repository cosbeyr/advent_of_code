from datetime import datetime as dt
import os
from aocd import get_data
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_date(year, day):
    year = year if year is not None else dt.now().year
    day = day if day is not None else dt.now().day
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, f'{year}', f'{day}')
    return year, day, path 

def get_example(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    example = soup.find("pre").get_text()
    return example

def build(year=None, day=None, return_data=True): 
    year, day, path = get_date(year, day)
    datapath = os.path.join(path, 'data.txt')
    examplepath = os.path.join(path, 'example.txt')

    if os.path.exists(path):
        print(f'Reading data: {path}')
        if return_data:
            with open(datapath, 'r') as f:
                data = f.read().splitlines()
            with open(examplepath, 'r') as f:
                example = f.read().splitlines()
            return data, example
        return 

    print(f'Building {year}/{day}: {path}')
    os.makedirs(path)
    data = get_data(year=year, day=day)
    with open(datapath, 'w') as f:
        f.write(data)

    example = get_example(year, day)
    with open(examplepath, 'w') as f:
        f.write(example)

    solutionpath = os.path.join(path, 'solution.py')
    with open(solutionpath, 'w') as f:
        f.write(f'\ndef day{day}_1(data):\n    raise NotImplementedError\n')
        f.write(f'\ndef day{day}_2(data):\n    raise NotImplementedError\n')

    if return_data:
        return data.splitlines(), example.splitlines()


def write_answer(answer, year=None, day=None):
    year, day, path = get_date(year, day)
    assert os.path.exists(path), f'Error! Year / Day entered ({year} / {day}) do not exist'

    answerpath = os.path.join(path, 'answer.txt')
    answer_str = ''

    if not os.path.exists(answerpath):
        answer_str = f'# {year} - Day {day}\n### Part 1: {answer}'
        line_count = 0
    else: 
        with open(answerpath, 'r') as f:
            line_count = sum(1 for _ in f)

    if line_count == 2:    
        answer_str = f'\n### Part 2: {answer}'
    
    if answer_str != '':    
        with open(answerpath, 'a') as f:
            f.write(answer_str)

    with open(answerpath, 'r') as f:
        print(f.read())



