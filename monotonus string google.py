s = input()
n= len(s)-1
sol = 0
idx=0
while(idx!=n):
    
    sol+=1
    
    inc = idx
    dec = idx

    while(inc + 1<n and s[inc]==s[inc+1]):
        inc+=1
    while(dec+1<n and s[dec]==s[dec+1]):
        dec+=1

    if (max(inc,dec)+1==n):
        break;

    idx = max(inc,dec)+1
    print(inc)


print(sol)    
    
