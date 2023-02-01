def mult_list(lis):
    if len(lis) == 0:
        return 1
    else:
        return lis.pop() * mult_list(lis)

def reverse(x):
    st = ""
    for i in range(len(x)-1, -1, -1):
        st += x[i]
    return st

#returns the pascal triangle
def pascal(x):

    #Holds the rows of numbers
    triangle_row = []

    #Holds the whole triangle as its being made
    triangle_column = []

    #Error if bad number
    if x < 1:
        print("error: lines less than 1")
        return

    #Base case 1
    if x >= 1:
        triangle_column.append([1])

    #Base case 2
    if x >= 2:
        triangle_column.append([1,1])

    #From pascal triangle length 3 onwards

    #Start is the start of the smallest row without base case (3)
    start = 3

    #J is range from row 3 to x (the total amount of rows to generate)
    for j in range(2,x):
        #I is range of the length of each row
        for i in range(0,start):
            #The beginning and end of every pascal triangle is "1"
            if i == 0 or i == start-1:
                triangle_row.append(1)
            #J-1 is the previous row and i is the iteration of that row, add the previous and current i's to append
            else:
                triangle_row.append(triangle_column[j-1][i-1] + triangle_column[j-1][i])

        #Append the full contents to column
        triangle_column.append(triangle_row[:])
        #Reset triangle_row for next row
        triangle_row.clear()
        #increase length of the row
        start += 1
    
    #For every row in the triangle
    for i in triangle_column:
        #Reset string to blank
        string = ""
        #For every number in the row
        for j in range(0,len(i)):
            #Add number and space
            string += (str(i[j]) + " ")
        #Print out the row of numbers minus the last space
        #Repeats until triangle_column is empty
        print(string[:-1])


pascal(30)