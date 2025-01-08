n = int(input())
arr = [0] + list(map(int, input().split()))
def heapify(n,i):
    largest = i
    l = i * 2
    r = i * 2 +1 
    if l <= n and arr[l] > arr[largest]:
        largest = l
    if r <= n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(n, largest)


def heap_sort(n):
    for i in range(n//2, 0, -1):
        heapify(n,i)
    for i in range(n,0,-1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(i-1, 1)
# Write your code here!
'''
function heapify(arr[], n, i)
  set largest = i
  set l = i * 2
  set r = i * 2 + 1

  if l <= n && arr[l] > arr[largest]
    largest = l

  if r <= n && arr[r] > arr[largest]
    largest = r

  if largest != i
    swap(arr[i], arr[largest])
    heapify(arr, n, largest)

function heap_sort(arr[], n)
  for i = n / 2 ... i >= 1
    heapify(arr, n, i)

  for i = n ... i > 1
    swap(arr[1], arr[i])
    heapify(arr, i - 1, 1)
'''
heap_sort(n)
print(*arr[1:])