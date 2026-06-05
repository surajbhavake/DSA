nums = [1, 1, 2, 3, 3, 3]


freq  = {} #here we created a empty dictionary

for num in nums : #num will take each number from nums array one by one 
    if num in freq : #here we are asking is the num is there in freq
        freq[num] += 1 # if yes then increase the count by 1 to that number
    else:
        freq[num] = 1 # else if the num is not there in freq then we will create that num with its count
    

print(freq) #output : {1: 2, 2: 1, 3: 3}

#Easier version 

nums2 = [1, 1, 2, 3, 3, 3,4]

freq2 = {}

for num in nums2 :
    freq2[num] = freq2.get(num,0)+1 #here this code means in if num = 3 then .get will
    #check in the freq2 for key = 3 and will take the value =3 here in .get(num,0) +1 means
    #if num here mean value, if it has any value then return value +1 if not then return 0+1
    #from .get(,) we get true and false condition 

print(freq2)#output {1: 2, 2: 1, 3: 3, 4: 1}



