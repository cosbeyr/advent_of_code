import pandas as pd
import math

def max_per_color(x):
    """ Group by color, return max number of cubes per color """
    df = pd.DataFrame(x, columns=['color', 'count'])  
    return df.groupby('color')['count'].apply(lambda x: max([int(count) for count in x])).to_dict()

def parse(data):
    """ Extract Game number and cube counts per color, compute max_per_color per set """
    df = pd.DataFrame(data)
    df['Game'] = df[0].apply(lambda x: int(x.split(': ')[0].split(' ')[1]))
    
    cube_counts = lambda x: [s.split(' ')[::-1] for sets in x.split(': ')[1].split('; ') for s in sets.split(', ')] 
    df['Cubes'] = df[0].apply(lambda x: cube_counts(x))
    df['Max'] = df['Cubes'].apply(lambda x: max_per_color(x))
    return df 

def day2_1(data):
    """ Find Games applicable to provided gold, return sum of applicable Game numbers """
    gold = {'red':12, 'green':13, 'blue':14}
    df = parse(data)
    df = df[df['Max'].apply(lambda x: all([x[color] <= max_count for color, max_count in gold.items()]))]
    return sum(df['Game'])

def day2_2(data):
    """ Find the minimum set of cubes that must be present, return the sum of the power of these sets """
    df = parse(data)
    return sum(df['Max'].apply(lambda x: math.prod(x.values())))
