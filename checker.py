with open("highscore.txt") as usm:
    print(type(usm.read()))
    u=usm.read()
    u=int(u)
    print(type(u))