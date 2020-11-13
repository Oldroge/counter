from time import sleep


def counter(s, e, st):
    print('INCREASING COUNT')
    for c in range(s, e + 1, st):
        print(c, end=' ')
        sleep(0.5)
    print()


def ncounter(s, e, st):
    print('DECREASING COUNT')
    if st < 0:
        st *= -1
    if st == 0:
        st = 1
    for l in range(s, e - 1, -st):
        print(l, end=' ')
        sleep(0.5)
    print()


#  PRESENTATION PROGRAM
counter(1, 10, 1)
ncounter(10, 0, 2)
#  MAIN PROGRAM
print('YOUR TURN:')
start = int(input('Start with witch number: '))
end = int(input('End with witch number: '))
step = int(input('How much steps: '))
if start > end:
    ncounter(start, end, step)
else:
    counter(start, end, step)
