# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
import re
# Your code here

letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
           'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


def word_count(s):
    # Your code here
    cache = {}
    for word in re.sub(r"[^a-zA-Z ']", ' ', s).upper().split():
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    return cache


def crack_ceasar(text):
    word_frequency = word_count(text)
    letter_frequency = {}
    for word, count in word_frequency.items():
        for letter in word:
            if letter in letter_frequency:
                letter_frequency[letter] += count
            else:
                letter_frequency[letter] = count
    frequencies = list(letter_frequency.items())
    frequencies.sort(key=lambda x: x[1], reverse=True)
    guess = [x[0] for x in frequencies]
    guess_map = dict(zip(guess, letters))
    decoded = ''
    for letter in text:
        if letter.upper() in guess_map:
            decoded += guess_map[letter]
        else:
            decoded += letter
    return decoded


if __name__ == '__main__':
    with open('ciphertext.txt', 'r') as c:
        cypher = c.read()

    print(crack_ceasar(cypher))
