s = "listen"
t = "silent"

freq_s = {}

for ch in s:
    freq_s[ch]= freq_s.get(ch,0)+1

freq_t= {}

for ch in t:
    freq_t[ch] = freq_t.get(ch,0)+1


if freq_t == freq_s :
    print('True')
else:
    print('false')