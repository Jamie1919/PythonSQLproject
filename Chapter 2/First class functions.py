from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        return elem
    raise RuntimeError(f"Could not find an element with {expected}.")



friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


print(search(friends, "Rolf Smith", itemgetter(name)))