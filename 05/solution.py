import string
from functools import reduce

with open('input') as f:
    polymers = f.read().splitlines()[0]

# polymers = 'dabAcCaCBAcCcaDA'
# polymers = 'aABAaa'

def remove_if_matching(acc, letter):
    if len(acc) < 1:
        return acc + letter

    if is_matching(acc[-1], letter):
        return acc[:-1]
    return acc + letter


def is_matching(one, two):
    if (one.isupper() and two.isupper()) or (one.islower() and two.islower()):
        return False
    return one.lower() == two.lower()


assert is_matching('a', 'A')
assert is_matching('A', 'a')
assert not is_matching('a', 'a')
assert not is_matching('a', 'B')
assert not is_matching('B', 'a')

print(len(reduce(remove_if_matching, polymers)))
troublemaker = min(string.ascii_lowercase, key=lambda l: len(reduce(remove_if_matching, polymers.replace(l, '').replace(l.upper(), ''))))
print(len(reduce(remove_if_matching, polymers.replace(troublemaker, '').replace(troublemaker.upper(), ''))))