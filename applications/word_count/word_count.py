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


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))
