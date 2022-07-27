y = input("type asc, desc or none: ")
res = [10, 34, 54, 65, 23, 54, 23, 3, 5, 76]
if y == "asc":
     res.sort()
     print(str(res))
if y == "desc":
    res.sort(reverse=True)
    print(str(res))
if y == "none":
    print(str(res))