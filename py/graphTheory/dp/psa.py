arr=[10,20,5,7]
prefixSumArray = [0 for i in range(len(arr))]
prefixSumArray[0] = arr[0]
for i in range(1, len(arr)):
     prefixSumArray[i] = prefixSumArray[i-1] + arr[i]
print(prefixSumArray)
l=1
r=2
#when you add 20 and 5 together
ree=prefixSumArray[r] - prefixSumArray[l-1]
print(ree)
