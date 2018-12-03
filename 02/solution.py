from difflib import SequenceMatcher

sample_input_one = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab',
]


def is_count_letter_in(string, count):
    occurences = {}
    for char in string:
        if char in occurences:
            occurences[char] += 1
        else:
            occurences[char] = 1

    return count in occurences.values()


assert not is_count_letter_in('abcdef', 2)
assert is_count_letter_in('bababc', 2)
assert is_count_letter_in('bababc', 3)


def get_checksum(box_ids):
    doubles = 0
    triples = 0
    for box_id in box_ids:
        if is_count_letter_in(box_id, 2):
            doubles += 1
        if is_count_letter_in(box_id, 3):
            triples += 1
    return doubles * triples


assert get_checksum(sample_input_one) == 12

with open('input') as f:
    my_box_ids = f.read().splitlines()

print(get_checksum(my_box_ids))


def different_number_of_chars(a, b):
    assert len(a) == len(b)
    return len(a) - int(SequenceMatcher(None, a, b).ratio() * len(a))

sample_input_two = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz',
]


def get_common_letters(ids):
    for i, _id in enumerate(ids):
        for id_to_compare in ids[i+1:]:
            if different_number_of_chars(_id, id_to_compare) == 1:
                return ''.join([l[0] for l in zip(_id, id_to_compare) if l[0] == l[1]])


assert get_common_letters(sample_input_two) == 'fgij'

print(get_common_letters(my_box_ids))

