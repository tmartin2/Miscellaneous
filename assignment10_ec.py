'''
Program that cleans a file or phrase, and in the case of the file, finds word frequency.

Author: Trevor Martin
'''
import sys
# import string


def remove_punc(file_lines):
    # punc = string.punctuation
    punc = '~!@#$%^&*()_+`-=[]\{}|,./<>?;:'+"\""+"\'"
    lines_wo_punc = ''.join([line.strip(punc) for line in file_lines.strip()])
 
    # failures
    # line = ' '.join([word.replace(char,'') for word in line for char in word if char in punc])
    # line = [map(lambda char: word.replace(char,'') if char in punc,word.split()) for word in line]
    # line = [list(map(lambda: word.replace(char,'') if char in punc else pass)) for word in line for char in word]
    # line = [''.join([word.replace(char,'') for char in word if char in punc]) for word in line]

    return lines_wo_punc


def word_freq(lines_wo_punc, gender=False, omit_list=None, int_limit=0):
    
    if omit_list is not None:
        word_list = lines_wo_punc.lower().split()
        word_set = set(word_list).difference(set(omit_list))
        alp_word_list = sorted(word_set)
        frequencies = [len(set(word).intersection(set(word_list)))+1 for word in alp_word_list]
        freq = list(zip(alp_word_list, frequencies))
        for tuple in freq:
            word,frequency = tuple
            print(f"{word} : {frequency}")
        
    if int_limit > 0:
        
        word_list = list(filter(lambda word: len(word) > int_limit, lines_wo_punc.lower().split()))
        word_set = set(word_list)
        alp_word_list = sorted(word_set)
        frequencies = [len(set(word).intersection(set(word_list)))+1 for word in alp_word_list]
        freq = list(zip(alp_word_list, frequencies))
        for tuple in freq:
            word,frequency = tuple
            print(f"{word} : {frequency}")

    if gender > 0:
        male_pronouns = ['he','him','his']
        female_pronouns = ['she','her','hers']
        # complete this
        pass
    
    if (gender == 0) and (int_limit == 0) and (omit_list == None):
        word_list = lines_wo_punc.lower().split()
        word_set = set(word_list)
        alp_word_list = sorted(word_set)
        frequencies = [len(set(word).intersection(set(word_list)))+1 for word in alp_word_list]
        freq = list(zip(alp_word_list, frequencies))
        for tuple in freq:
            word,frequency = tuple
            print(f"{word} : {frequency}")

    

def main():
    available_texts = []
    message = (
        f"\nWelcome to my word frequency device!\n"
        f"You have several options, but first I must tell you how this works\n"
        f"1. Enter a word or phrase with punctuation and have them cleaned\n"
        f"2. Enter a text file and have the word frequency displayed\n"
        f"3. Display these options by typing o\n"
        f"4. Quit the program by pressing q\n"
        )
    print(message)
    while True:
        input_ = str(input("Please enter one of the inputs described in the options.\nHere: "))
        if input_ == 'o': print(message)
        if input_ == 'q': sys.exit()
        if input_ != ('o' or 'q') and len(input_) >= 1:
            
                try:
                    file_lines = open(input_).read()
                except:
                    print(f"{remove_punc(input_)}")
                else:
                    message2  = (
                        f"\n1. Type a list of words (i.e. an the but) to be omitted.\n"
                        f"2. Type an integer to omit words over that length.\n"
                        f"3. Type gender to get a comparison based on gender.\n"
                        f"4. Type none to just get the alphabetical word frequency.\n"
                        f"5. Type b to go back to the main options.\n"
                        )
                    print(message2)
                    while True:
                        input2 = str(input("\nPlease enter one of the options.\nHere: "))
                        lines_wo_punc = remove_punc(file_lines)
                        if input2 == 'b':
                            print(message)
                            break
                        if input2 == 'gender':
                            word_freq(lines_wo_punc, gender=True)
                        if (input2 != ('gender' or 'none')) and (input2 not in '123456789'):
                            word_freq(lines_wo_punc, omit_list=input2.split())
                        if input2 in '123456789':
                            word_freq(lines_wo_punc, int_limit=int(input2)) 
                        if input2 == 'none':
                            word_freq(lines_wo_punc)
                        else:
                            print(f"\n{message2}")
                            continue 
        else:
            print(f"\n{message}")
        
if __name__ == '__main__':
    main()
