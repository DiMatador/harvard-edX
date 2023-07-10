def gen_level():
    ct = 0
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level < 1 or level > 3:
                continue
        except ValueError:
            # if error do something
            continue
        break

    return level

gen_level()
