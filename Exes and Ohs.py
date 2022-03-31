def xo(s):
    count_o, count_upper_o = s.count('o'), s.count('O')
    count_x, count_upper_x = s.count('x'), s.count('X')
    if count_x + count_upper_x == count_o + count_upper_o:
        return True
    else:
        return False


xo("xxOo")