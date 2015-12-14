#!/usr/bin/python
def get_new_word(word):
    word += 'ee'
    new_word = ''
    i = 0
    while i < len(word)-2:

        sub_char = word[i]
        sub_len = 1
        if word[i] == word[i+1] and word[i] == word[i+2]:
            sub_len += 2
            i += 2
        elif word[i] == word[i+1]:
            sub_len += 1
            i += 1

        i += 1

        new_word += str(sub_len) + sub_char

    return new_word

the_word = '3113322113'
print the_word
for num in range(50):
    the_word = get_new_word(the_word)
    print num, len(the_word)
# print the_word
