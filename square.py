def Square(numrows):
    i = 0
    j = 0
    for i in range(numrows):
        for j in range(numrows):
            if(i == 0 or i == numrows-1 or j == 0 or j == numrows-1):{
                print('*', end = ' ')
            }
            else:{
                print(' ', end = ' ')
            }
        print()
        
Square(5)

#We have to use two for loops for this problem, because in one loop we will print all rows, but in other for loop
#which is inside of first loop, we will print * in the first and last row (numrows-1), otherwise will print empty string!