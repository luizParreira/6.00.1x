

def count_bob(string):
    n = 0
    bob = 'bob'
    i = 0
    for s in range(len(string) - 2):
        print string[i : i + 3]
        if string[i : i + 3] == bob:
            n += 1
        i += 1
    return n

r = count_bob('azcbobobegghakl')
print r
        
    