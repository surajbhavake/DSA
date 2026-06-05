word = "banana"

freq = {}

for ch in word:
    freq[ch] = freq.get(ch,0)+1 #we can use same code we used for number in string it will
    #automatically seperate the string

print(freq)#output {'b': 1, 'a': 3, 'n': 2}



char = ["apple","banana","apple","mango","banana","apple"]


freq2 = {}

for ch in char:
    freq2[ch]= freq2.get(ch,0)+1

print(freq2) #output {'apple': 3, 'banana': 2, 'mango': 1}

freq2['mango'] +=1 #here we add count to the mango key in hash
print(freq2)#output {'apple': 3, 'banana': 2, 'mango': 2}


