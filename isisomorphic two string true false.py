def isisomorphic(s,t):
    if (len(s)!=len(t)):
        return False
    else:
        c,d={},{}
        for i in range(len(s)):
            a,b=s[i],t[i]
            if(a not in c):
                c[a]=b
            if(b not in d):
                d[b]=a
            if(c[a]!=b or d[b]!=a):
                return False
            return True
s=input("enter the string S=")
t=input("enter the string T=")
print(isisomorphic(s,t))
