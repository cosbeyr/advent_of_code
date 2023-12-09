import re
import math

def parse(data):
    """ Extract (x, y) pairs adjacent to symbols and (x,y) paris from each number span"""
    adjacent, spans = [], []
    for y, row in enumerate(data):
        symbol_matches = list(re.finditer(r"[^0-9.]", row)) 
        for match in symbol_matches:
            x = match.span()[0]
            adj = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
            symbol = match.group()
            adjacent.append((symbol, adj))
        number_matches = list(re.finditer(r"\d+", row)) 
        for match in number_matches:
            span = list(range(*match.span()))
            number = match.group()
            spans.append((number, [(x, y) for x in span]))
    return adjacent, spans

def day3_1(data):
    """ Return sum of numbers adjacent to symbols in engine schematic """
    adjacent, spans = parse(data)
    adjacent = list(set(sum([adj[1] for adj in adjacent], []))) 
    numbers = [int(span[0]) for span in spans if any([s in adjacent for s in span[1]])]
    return sum(numbers)

def day3_2(data):
    """ Return sum of gear ratios for gears (*) with exactly two adjacent part numbers"""
    adjacent, spans = parse(data)
    adjacent = [adj[1] for adj in adjacent if adj[0] == '*']
    part_numbers = [[int(span[0]) for span in spans if any([s in gear for s in span[1]])] for gear in adjacent]
    return sum([math.prod(parts) for parts in part_numbers if len(parts) == 2])
