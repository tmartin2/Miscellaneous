# Date: 27 April 2020
# Decodes a message with letters offset by some length in the alphabet
import string

__author__ = "TP"

with open("code.txt") as code_file:
    lines = code_file.read()
    letters = list(set(lines).intersection(string.ascii_lowercase))
    counts = [lines.count(letter) for letter in letters]
    most_freq = (letters[counts.index(max(counts))], max(counts))
    diff = (ord(most_freq[0])-ord('e'))%26 + 97
    shift = lambda c: chr((ord(c)-diff)%26 + 97) if (c.isalpha() and len(c) < 2) else c
    lines = ''.join(list(map(shift, lines)))
    print(lines)
    code_file.close()
    
    
