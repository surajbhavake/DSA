

nums = [1,1,1,2,2,3]

freq3 = {}

for num in nums:
    freq3[num] = freq3.get(num,0)+1

print(freq3)

most_frequent = None
max_count = 0
for num , count in freq3.items():
    if count > max_count:
        max_count = count
        most_frequent = num

print(f"This is the most frequent number {most_frequent } and its {max_count}")#This is the most frequent number 1 and its 3