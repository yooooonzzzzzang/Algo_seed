def solution(triangle):
    answer = 0
    n = len(triangle)
    for i in range(n-1, 0,-1):

        for j in range(len(triangle[i])-1):
            # print(i,j,j+1)
            tmp = max(triangle[i][j],triangle[i][j+1])
            triangle[i-1][j] = tmp+triangle[i-1][j]
        
            
    # print(triangle)
    return triangle[0][0]