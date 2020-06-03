digits = {'one': '1',
          'two': '2',
          'three': '3',
          'four': '4',
          'five': '5',
          'six': '6',
          'seven': '7',
          'eight': '8',
          'nine': '9',
          'zero': '0'}
doubles = {'ten': '10',
           'elven': '11',
           'twelve': '12',
           'thirteen': '13',
           'fourteen': '14',
           'fifteen': '15',
           'sixteen': '16',
           'seventeen': '17',
           'eighteen': '18',
           'nineteen': '19',
           'twenty': '20',
           'thirty': '30',
           'fourty': '40',
           'fifty': '50',
           'sixty': '60',
           'seventy': '70',
           'eighty': '80',
           'ninty': '90',
           'hundred': '00'}


def translate_number(num_string):
    words = num_string.split()
    num_total = '0'
    for word in words:
        if word in digits.keys():
            if num_total[-1] == '0':
                num_total = num_total[:-1] + digits[word]
            else:
                num_total += digits[word]
        elif word in doubles.keys():
            num_total.strip('0')
            num_total += doubles[word]
    return int(num_total)


if __name__ == '__main__':
    arr = [
        "five",
        "twenty six",
        "nine hundred ninety nine",
        "twelve",
        "eighteen",
        "one hundred one",
        "fifty two",
        "forty one",
        "seventy seven",
        "six",
        "twelve",
        "four",
        "sixteen"
    ]

    for a in arr:
        if translate_number(a) % 3 == 0:
            print(a)
