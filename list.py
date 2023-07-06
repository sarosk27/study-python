c= 100
for i = 1 to n do 
    for j = 1 to n do {
        Temp = A[i][j]+c
        A[i][j] = A[j][i]
        A[j][i] = temp -c
    } 
for i = 1 to n do 
    for j = 1 to n do 
        Output(A[i][j]);