'''
5 7
4 5 1 3 2
'''
def Dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt)//2
        Dsort(lt, mid)
        Dsort(mid+1, rt)

        merge(lt, rt, mid)



def merge(lt, rt, mid):
    global cnt
    p1 = lt
    p2 = mid+1
    tmp = []
    while p1 <= mid and p2 <= rt:
        if arr[p1] < arr[p2] :
            tmp.append(arr[p1])
            p1 += 1
        else:
            tmp.append(arr[p2])
            p2 +=1
    if p1 <= mid:
        tmp = tmp + arr[p1:mid+1]
    elif p2 <=rt:
        tmp = tmp + arr[p2:rt+1]
    for i in range(len(tmp)):
        cnt += 1
        if cnt == k:
            print(tmp[i])
            exit(0)
        arr[lt+i] = tmp[i]


if __name__ == "__main__":
    n, k = map(int, input().split())
    cnt = 0
    arr = list(map(int, input().split()))
    Dsort(0, n-1)
    print(-1)


