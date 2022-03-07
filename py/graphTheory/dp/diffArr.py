arr=[9,20,5,7]
differenceArray = [0 for i in range(len(arr) + 1)]
differenceArray[0] = arr[0]
for i in range(1, len(arr)):
    differenceArray[i] = arr[i] - arr[i-1]
print(differenceArray)
l=1
r=2
differenceArray[l] += 10
differenceArray[r+1] -= 10
print(differenceArray)
arr[0] = differenceArray[0]
for i in range(1, len(arr)):
    arr[i] = arr[i - 1] + differenceArray[i]
print(arr)
