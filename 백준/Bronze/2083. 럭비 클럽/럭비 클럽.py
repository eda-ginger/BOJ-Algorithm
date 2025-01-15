while True:
    try:
        inform = input().split()
        if inform[0] == '#':
            break
        elif int(inform[1]) > 17 or int(inform[2]) >= 80:
            print(inform[0], 'Senior')
        else:
            print(inform[0], 'Junior')
    except:
        break