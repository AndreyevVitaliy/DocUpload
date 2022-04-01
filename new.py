
def find_in_list(alphabet, find_string=""):
    for x in alphabet:
        if x == find_string:
            return ord(x)
    return -1


def alphabet_generation(shift=5):
    alphabet = {}
    for i in range(65, 65+26):
        alphabet[chr(i)] = chr(i+shift)

    for i in range(97, 97+26):
        alphabet[chr(i)] = chr(i+shift)

    return alphabet

def shift_alphabet(alphabet):
    word = "Helloz"
    new_word = ""
    for x in word:
        for a in alphabet:
            if x == a:
                new_word = new_word + alphabet[a]



    return new_word

alphabet_dict = alphabet_generation(5)
result = shift_alphabet(alphabet_dict)

print(result)