nums = [1, 2, 3, 1]

seen = {}

for num in nums :
    if num in seen:
        print('true')
    
    seen[num] = seen.get(num,0)+1

    print(seen)