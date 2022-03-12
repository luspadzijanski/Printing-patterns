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
