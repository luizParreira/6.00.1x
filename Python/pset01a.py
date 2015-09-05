
def num_vowels(string):
    result = 0
    for s in string:
        vowels = ['a', 'e', 'i', 'o', 'u']
        if s in vowels:
            result += 1
    return result

a = num_vowels('azcbobobegghakl')
print(a)

    