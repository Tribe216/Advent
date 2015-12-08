#!/usr/bin/python

vowels = ['a', 'e', 'i', 'o', 'u']
banned_set = ['ab', 'cd', 'pq', 'xy']
nice_num = 0
for word in open('day_5_input.txt', 'r'):
    vowel_count = 0
    double_letter = False
    has_banned = False
    for c in word:
        if c in vowels:
            vowel_count += 1

    if vowel_count < 3:
        continue

    for x in range(len(word) - 1):
        if word[x] == word[x + 1]:
            double_letter = True

    if not double_letter:
        continue

    for b in banned_set:
        if b in word:
            has_banned = True

    if has_banned:
        continue

    nice_num += 1

    print word, nice_num
