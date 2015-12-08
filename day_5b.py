#!/usr/bin/python

nice_num = 0
for word in open('day_5_input.txt', 'r'):
    spaced_repeat = False
    two_letter_repeat = False

    for x in range(len(word) - 2):
        if word[x] == word[x + 2]:
            spaced_repeat = True
            break

    if not spaced_repeat:
        continue

    for x in range(len(word) - 3):
        if (word[x] + word[x + 1]) in word[(x+2):]:
            two_letter_repeat = True
            break

    if not two_letter_repeat:
        continue

    nice_num += 1

    print word, nice_num
