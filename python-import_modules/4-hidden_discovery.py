#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for i in range(0, len(names)):
        if "__" != names[i][:2]:
            print(names[i])
