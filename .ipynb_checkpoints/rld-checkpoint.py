def rld(mess):
    res = ''
    count = 0
    for c in mess:
        if c.isdigit():
            count = count*10 + int(c)
        else:
            res += c*count
            count = 0
    return  res


if __name__ == '__main__':
    import sys
    argv = sys.argv
    print(argv)
    