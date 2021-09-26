
def binsearch(l, key):
    if len(l) == 0:
        return False
    else:
        mid = len(l) // 2
        for elem in l:
            if l[mid] == key:
                return True
            elif key < l[mid]:
                return binsearch(l[:mid], key)
            else:
                return binsearch(l[mid+1:], key)


if(__name__ == "__main__"):
    l = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    key = 700
    print(binsearch(l, key))
    key = 900
    print(binsearch(l, key))
    key = 100
    print(binsearch(l, key))
    key = 0
    print(binsearch(l, key))
    key = 1000
    print(binsearch(l, key))


# print(__name__)  # will be "__main__" when we run this file directly;
# will be "myfunctions" when we run this code after import in a different module
