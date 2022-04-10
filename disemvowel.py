"""
Убирает гласные из строчек
"""

def disomvowel(s):
    vowels = "aeiouyAEIOY"
    for i in range(len(s)):
        if s[i] in vowels:
            continue
        else:
            print(s[i], end='')


disomvowel("This website is for losers LOL")
