import random
import re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here


def analyze_text(text):
    words = re.sub(r"[^a-zA-Z ']", ' ', text).lower().split()
    chain = {}
    q = len(words) - 1
    for i, word in enumerate(words):
        if word in chain:
            if i < q:
                chain[word].append(words[i + 1])
        else:
            if i < q:
                chain[word] = [words[i+1]]
    return chain

# TODO: construct 5 random sentences
# Your code here


def generate_text(start, length, chain):
    print(start, end=' ')
    options = chain[start]
    if len(options) > 0 and length > 0:
        generate_text(random.choice(options), length - 1, chain)


if __name__ == '__main__':
    chain = analyze_text(words)
    generate_text('puzzled', 150, chain)
