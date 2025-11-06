t = int(input("what time is it"))
if t >= 5 and t <=11:
    print("morning")
elif t >= 12 and t <= 16:
    print ("afternoon")
elif t >= 17 and t <= 20:
    print("evening")
elif t >= 21 and t <= 24:
    print("night")
elif t >= 1 and t<=4:
    print("night")
else:
    print("invalid input")