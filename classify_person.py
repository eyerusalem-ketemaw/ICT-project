classify_person=int(input("what is your age"))
if classify_person <= 12:
    print("Child")
elif classify_person <= 17:
    print("Teenager")
elif classify_person <= 64:
    print("Adult")
else:
    print("Senior")
