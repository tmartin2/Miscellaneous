from functools import reduce
import numpy as np
import itertools 
def find_atts(num_atts=2, threshold=0.5):
    with open("census.csv") as file:
        lines = file.readlines()[:10]
        att_list = [set(elt.split(',')) for elt in lines]
        #unique_atts = set(list(reduce((lambda elt1,elt2: elt1+elt2),att_list)))
        #print(unique_atts)
        # unique_atts = set(lines.split(',')])
        #print(all_atts)
        check_against_all = lambda x, att_list: [elt for elt in att_list if len(x.intersection(elt)) == num_atts]
        common_atts = list(filter(lambda _list: len(_list) != 0,[check_against_all(_, att_list) for _ in att_list]))
        #common_atts = list(filter((lambda x: check_against_all(x, att_list)), att_list))
        common_atts = list(itertools.chain(common_atts))
        print(common_atts)
        file.close()
find_atts()


