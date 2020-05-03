def plusdash(plus, dash):
    for i in range((plus-1)*dash + plus):
        if i%(dash+1)==0:
            print('+', end='')
        else:
            print('-', end='')
    print('')

def pipe(pipe, space):
    for i in range((pipe-1)*space + pipe):
        if i % (space+1) == 0:
            print('|', end='')
        else:
            print(' ', end='')
    print('')


def wordinbar(word, space):
    pipe = len(word) + 1
    j = 0
    for i in range((pipe-1)*space + pipe):
        if i % (space+1) == 0:
            print('|', end='')
        elif i % (space//2 + 1) == 0:
            print(word[j], end='')
            j += 1
        else:
            print(' ', end='')
    print('')


def wordinbox(word, space):
    plusdash(len(word)+1, space)
    for i in range(1):
        wordinbar(word, space)
    plusdash(len(word)+1, space)


def wordinsquare(word, height):
    if height % 2 == 0:
        space = height + 1
    else:
        space = height
    space = space * 3
    plusdash(len(word)+1, space)
    for i in range(space//6):
        pipe(len(word)+1, space)
    for i in range(1):
        wordinbar(word, space)
    for i in range(space//6):
        pipe(len(word)+1, space)
    plusdash(len(word)+1, space)

wordinsquare('SURAJ W', 3)
