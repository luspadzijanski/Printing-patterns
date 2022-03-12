def Triangle(numrows):
    i = 0
    for i in range(numrows + 1):
        print("*" * i)

Triangle(5)
         
#If you want to print five rows, than the range will be equal to numrows + 1,
#because the iteration starts from 0 (counter i is 0!)
