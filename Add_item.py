sum=0
while(True):
    user_input=input("Enter the price or press q to quit:\n")
    if(user_input!='q'):

        sum=sum+int(user_input)
        print(f"Order Total so far:{sum}")
    else:
        print(f"Your bill total is{sum}.Thanks for visiting with us!")
        break

