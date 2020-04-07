import sys
import string

__author__ = 'Trevor Martin'

print("Welcome to my concorder!\nIF YOU WANT TO QUIT, type in ""\"q""\" where it says enter file")

def setup_concordance(lines, filename):
    proper_form = [line.strip().split() for line in lines]
    proper_form = list(filter(None, proper_form))
    # now each index of proper_form is a (line number - 1)
    punCd = lambda line: [elt.strip(string.punctuation).lower() for elt in line]
    clean_text = [punCd(line) for line in proper_form]
    clean_textv2 = [list(filter(None, line)) for line in clean_text]
    # now clean_textv2 has no empty strings
    uniq_words = set([sub_elt for elt in clean_textv2 for sub_elt in elt])
    word_concord = dict(zip(list(uniq_words), [[] for _ in range(len(uniq_words))]))
    for index, line in enumerate(clean_textv2): 
        for word in line:
            word_concord[word].append(index+1) # recall the indices are one off
    for key in sorted(list(word_concord.keys())):
        line_nums = " ".join([str(elt) for elt in word_concord[key]])
        print(f"{key} : {line_nums[:]}")    
    num_uniq_words = len(uniq_words)
    num_lines = len(clean_textv2)
    print(f"There are {num_uniq_words} unique words in {num_lines} lines")


def main():
    while True:
        try:
            file = input("Enter file: ")
            if str(file) == 'q': sys.exit()
            with open(file) as f:
                lines = f.readlines()
                filename = str(file)
            setup_concordance(lines, filename)            
        except FileNotFoundError:
            print("There was something erroneous with the file, try again please.")

if __name__ == '__main__':
    main()
