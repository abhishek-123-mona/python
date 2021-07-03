f=open('poems.txt')
t=f.read()
if 'twinkle' in t:
     print("twinkle is present")
else:
    print("not ppresent")
f.close()