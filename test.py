students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
 
inputsize=int(input())
students=[[input(),float(input())] for i in range(inputsize)]#for taking the input values
lnew=sorted(list(set([students[i][1] for i in range(inputsize)])),key=float)#for comparing float values
lnew1=sorted([students[i][0] for i in range(inputsize) if lnew[1]==students[i][1]])#list with names having second least score in sorted manner
for i in range(len(lnew1)):
    print(lnew1[i])