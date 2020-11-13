from time import sleep

# In this part the program will make the output increase or decrease the counting


def counter(s, e, st):
    if s > e:
        print('DECREASING COUNT')
        if st < 0:
            st *= -1
        if st == 0:
            st = 1
        for l in range(s, e - 1, -st):
            print(l, end=' ')
            sleep(0.5)
        print()
    else:
        print('INCREASING COUNT')
        for c in range(s, e + 1, st):
            print(c, end=' ')
            sleep(0.5)
        print()


#  PRESENTATION PROGRAM
counter(1, 10, 1)
counter(10, 0, 2)
#  MAIN PROGRAM
#  Here the program ask to output witch number start, witch number ends and how many steps will need
print('YOUR TURN')
start = int(input('Start with witch number: '))
end = int(input('End with witch number: '))
step = int(input('How much steps: '))
counter(start, end, step)
