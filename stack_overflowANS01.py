d = {1:2, 2:3, 4:5}

keys = list(d.keys())
values = list(d.values())


#def get_final(next, d):
#    for key in list(d.keys()):
#        if (d[key] not in list(d.keys())) :
#            d[key] = 
#        else:
#            get_final(d)

#def check_amount(d):
#    for key, val in list(d.items()):
#        if val in list(d.keys()):
#            return d[val]
#        else:
#            return key

#for val in list(d.values()):
#    if val in list(d.keys()):

def find_end(val, d):
    for _ in range(len(list(d.keys()))):
        if val in list(d.keys()):
            val = d[val]
    return val

new_dict = {}
for key, val in list(d.items()):
    d.pop(key)
    # val = 2, check if there is a key that is 2, check if the val of that is in the keys, if the next val is not in the keys return it if it is keep going
    #end_map = list(it.dropwhile(lambda val: , d.values()))
    new_dict[key] = find_end(val, d)
    
    
    #[v for k in list(d.keys()) for v in list(d.values()) if val == k]
    #print(end_map)
    #if len(end_map) >= 1:
    #    new_dict[key] = end_map[-1]
    #else:
    #    new_dict[key] = val
    
print(new_dict)
