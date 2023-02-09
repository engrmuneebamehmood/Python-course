'''for a in range(1,6):
    for b in range(1, a+1):
        print(b, end='')
    print()'''

'''for a in range(1,6):
    for b in range(1, 6):
        print(b, end='')
    print()'''

for a in range(1,6):
    for b in range(1, a+1):
        for c in range(1,b+1):
            print("   *", end='')
    print()
