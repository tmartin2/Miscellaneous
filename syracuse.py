# Date: 26 April 2020
import typing
import sys

__author__ = "TM"

def syracuse(number: int, seq_len: int = 1):
    if number == 1:
        return number , seq_len
    elif number % 2 != 0:
        return syracuse((3*number + 1), seq_len+1)
    else:
        return syracuse((number / 2), seq_len+1)

def main():
    print(f"To exit this program type ""\"q""\" please")
    while True:
        seq_len = str(input("Please enter a sequence length for this program: "))
        if seq_len.isdigit():
            number = 1
            while True:
                if syracuse(number)[1] >= int(seq_len):
                    print(number)
                    break
                number+=1
        else:
            print("Something went wrong or you typed ""\"q""\"")
            sys.exit()

if __name__ == "__main__":
    main()
