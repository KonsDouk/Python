year = int(input("Etos = "))


if (((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)):
    disekto = True
    print(disekto)
else:
    disekto = False
    print(disekto)
