num=int(input("eneter the no:\n"))
prime=True 
for i in range(2,num):
    if (num%i==0):
        prime=False
        break
if prime:
        print("This no. prime")
else  :
        print("This no. not prime")