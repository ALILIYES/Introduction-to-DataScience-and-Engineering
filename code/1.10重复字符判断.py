def is_exist(s):
    d = {}
    for i in s:
        if i in d:
            return True
        else:
            d[i]=1
    return False

if __name__ == "__main__":
    s = input()
    print(is_exist(s))
