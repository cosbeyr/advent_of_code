import pandas as pd

def parse(data):
    """ Extract Card, winning numbers / current numbers, find total of matching numbers and compute points """
    df = pd.DataFrame(data)
    df['Card'] = df[0].apply(lambda x: int(x.split(':')[0].split()[1]))
    df['Winning'] = df[0].apply(lambda x: x.split(':')[1].split(' |')[0].split())
    df['Numbers'] = df[0].apply(lambda x: x.split('| ')[1].split())
    df['Matching'] = df.apply(lambda x: len([n for n in x['Numbers'] if n in x['Winning']]), axis=1)
    df['Points'] = df['Matching'].apply(lambda x: lambda x: 0 if x == 0 else 2 ** (x-1))
    return df

def day4_1(data):
    """ Return the sum of points over all scratch cards """
    df = parse(data)
    return sum(df['Points'])

def day4_2(data):
    """ Return the total number of scratchcards after accumulating originals and copies """
    df = parse(data)
    cards, matching = list(df['Card']), list(df['Matching'])
    dictionary = {}
    for i, card in enumerate(cards, start=1):
        try:
            cards += dictionary[card]
        except:
            dictionary[card] = list(df.loc[i:i+matching[i-1]-1]['Card'])
            cards += dictionary[card]
    return i

