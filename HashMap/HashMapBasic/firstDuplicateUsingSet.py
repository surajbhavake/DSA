nums = [2,1,3,5,3,2]

seen = set()

for num in nums :
    if num in seen:
        print('true')
        break
    
    seen.add(num)

    print(seen)