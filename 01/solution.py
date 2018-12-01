from functools import reduce

sample_input = ['+1', '-2', '+3', '+1']


def to_change(change):
    if change[0] == '-':
        return lambda x: x - int(change[1:])
    else:
        return lambda x: x + int(change[1:])


def get_frequency(changes):
    return reduce(lambda acc, x: to_change(x)(acc), changes, 0)


assert get_frequency(sample_input) == 3

# solution one
with open('input') as f:
    input = f.readlines()

print(get_frequency(input))


# solution two
def frequency_generator(values):
    i = 0
    while True:
        yield values[i]
        i += 1
        if i >= len(values):
            i = 0


gathered_frequencies = set()
current_freq = 0
gen = frequency_generator(input)
while current_freq not in gathered_frequencies:
    gathered_frequencies.add(current_freq)
    current_freq = to_change(next(gen))(current_freq)

print(current_freq)
