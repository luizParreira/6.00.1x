
def num_vowels(string):
    result = 0
    for s in string:
        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
            result += 1
    return result

a = num_vowels('azcbobobegghakl')
print(a)

    