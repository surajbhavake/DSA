nums = [1,1,2,3,3,4]

freq ={}

for num in nums:
    freq[num] = freq.get(num,0) +1



unique = []

for key,value in freq.items():
    if value == 1:
        unique.append(key)

print(freq,unique)