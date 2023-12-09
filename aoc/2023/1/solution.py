import re

def day1_1(data):
    """ Remove non-digits, reduce to first and last, sum """
    keep_digits = lambda x: re.sub("[^1-9]", "", x) 
    digits = [keep_digits(x) for x in data]
    twodigits = [int(f'{x[0]}{x[-1]}') for x in digits]
    return sum(twodigits)


def word2digit(x):
    """ Find word representation spans, sort by start index, replace start letter with digit """ 
    word_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
                 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    results = [(sub.span(), key, value) for key, value in word_dict.items() for sub in re.finditer(key, x)]
    results = sorted(results, key=lambda x: x[0][0])
    
    for span, key, digit in results:
        idx = span[0]
        x = f'{x[:idx]}{digit}{x[idx+1:]}'
    return x

def day1_2(data):
    """ Replace start of word representation with digit, apply day1_1 logic """
    digits = [word2digit(x) for x in data]
    return day1_1(digits)
