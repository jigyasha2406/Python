s="abcabcbb"
max_len=0
for i in range(len(s)):
    substring=[]
    current_sum=0
    for j in range(i,len(s)):
        if s[j] in substring:
            break
        substring.append(s[j])
        current_sum+=1
    if current_sum>max_len:
        max_len=current_sum
print(max_len)