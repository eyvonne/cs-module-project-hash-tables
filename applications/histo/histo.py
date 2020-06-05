import re


def word_count(s):
    # Your code here
    cache = {}
    for word in re.sub(r"[^a-zA-Z ']", ' ', s).lower().split():
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    return cache


def histo_from_file(file):
    with open(file, 'r') as f:
        words = f.read()

    counts = list(word_count(words).items())

    counts.sort(key=lambda x: x[0])
    counts.sort(key=lambda x: x[1], reverse=True)

    width = int(max([len(x[0]) for x in counts]))

    for word in counts:
        bar = '#' * word[1]
        print(f'{word[0]: <{width}}  {bar}')


if __name__ == '__main__':
    histo_from_file('robin.txt')
