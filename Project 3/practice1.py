sum=0
while(True):
    number= input("Eneter your price\n") 
    if(number!='q'):
        sum=sum+int(number)
        print(f"order total so far{sum}")

    else:
        print("thanx for using our calculator")
        print(f"your bill total is {sum}")
        break