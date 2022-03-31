"""
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an
 application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club,
handicaps range from -2 to +26; the better the player the lower the handicap."""


def open_or_senior(data):
    open_or_not = []
    for i in range(len(data)):
        age = int((data[i])[0])
        handicap = int((data[i])[1])
        if age >= 55 and handicap > 7:
            open_or_not.append("Senior")
        else:
            open_or_not.append("Open")
    print(open_or_not)
    return data


open_or_senior([[45, 12], [55, 21], [19, -2], [104, 20]])
