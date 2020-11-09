import itertools

pattern = {
    ' ': ' ',
    '⭐':'1',
    '🌈': '6',
    '🌑': '🌑',
    '🍀': '3',
    '🎈': '7',
    '🐴': '🐴',
    '💜': '💜',
    '🦄': '5'
}

string = `the encoded string`
output = [""] * len(string)
keys = ['2', '4', '0']

def decode():
    for i in range(0, len(output)):
        output[i] = pattern[string[i]]
    
    temp = "".join(output)
    temp = temp.split(" ")
    
    new = [""] * len(string)
    ind = 0
    for i in temp:
        new[ind] = chr(int(i, 8))
        ind += 1

    return "".join(new)

for combo in list(itertools.permutations(keys)):
    pattern['🌑'] = combo[0]
    pattern['🐴'] = combo[1]
    pattern['💜'] = combo[2]

    print("Combo", combo)
    print(decode())
    
# set our vals for unknown emojis

string = "⭐🌈🍀 ⭐🌈🦄 ⭐🦄🌈 ⭐🎈🍀 ⭐🦄🌑 ⭐🌈🦄 ⭐🌑🍀 ⭐🦄🍀 ⭐🎈⭐ 🦄🦄 ⭐🦄🎈 ⭐🌑🍀 ⭐🌈🌑 ⭐🌑⭐ ⭐🦄🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄⭐ ⭐🌈🍀 🦄🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🌑🦄 🦄🦄 ⭐🌑🐴 ⭐🌑🦄 ⭐🌈🍀 ⭐🌈🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄🦄 ⭐🌑🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🦄🎈 ⭐🌑🌑 ⭐🎈🦄"


