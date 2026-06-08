nums = [4, 4, 4, 5, 5, 6]

freq = {}

for num in nums :
    freq[num] = freq.get(num,0)+1

print(freq)

least_num = None
least_count = float('inf')

for num,count in freq.items():
    if count<least_count:
        least_count = count
        least_num = num 

print({'least_num' : least_num ,'least_count' : least_count})