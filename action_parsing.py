"""
Contains a function to parse a string representation of an action list, and return a list
of tuples, each tuple containing the range of numbers indicated by the action list.

@author: Andrew Curry
"""


def parse_action_list(action_list: str) -> list[tuple[int, int]]:
    """
    Parses a string representation of an action list, and return a list of tuples, each 
    tuple containing the range of numbers indicated by the action list.
    Assumes the action list will be in the format 'PrintXXXXtoYYYY,PrintAAAAtoBBBB'
    """
    ranges: list[tuple[int, int]] = []
    for action in action_list.split(','):
        range_strs = action[5:].split('to')
        ranges.append((int(range_strs[0]), int(range_strs[1])))
    return ranges