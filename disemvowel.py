"""
Убирает гласные из строчек
"""


def disomvowel(s):
    string_ = ''
    vowels = "aeiouyAEIOY"
    for i in range(len(s)):
        if s[i] in vowels:
            continue
        else:
            string_ += s[i]
    return string_

disomvowel("This website is for losers LOL")
