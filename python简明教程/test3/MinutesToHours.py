import sys


def Hours(min):
    if min < 0:
        raise ValueError
    else:
        hours = min // 60
        mins = min % 60
        print("{} H, {} M".format(hours, mins))


try:
    Hours(int(sys.argv[1]))
except ValueError:
    print('Parameter Error')
