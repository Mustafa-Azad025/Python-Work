print('''         ---------------------------
         |BY:-                     |
         |      MUSTAFA AZAD       |
         |                         |
         -------------------------- ''')
     
cho='y'
while cho==("y" or "Y"):
    ch=int(input('''which pattern do you want to print:
             1.To print the pattern of 1 2 3 . . .
             2.To print the pattern of right angle triangle
             3.To print the pattern of equilatral upside-down triangle :
             4.To print the pattern of triangle 1 : '''))
    if ch==1:
        print("enter the number to print the pattern of 1 2 3 . . .: ")
        n=int(input())
        for i in range(1,n+1):
            print(i,end="");
    elif ch==2:
        a=int(input("enter the number to print the pattern of right angle triangle:"));
        for i in range(1,a+1) :
              for j in range(1,i+1) :
                  print("*",end="")
              print(" ")
    elif ch==3:
        a=int(input("enter the number to print the pattern of equilatral upside-down triangle:"));
        for i in range(a,0,-1):
            print(" "*(a-i),end="")
            for j in range(1,i+1):
                print(j,end=" ")
            print(" ")
    elif ch==4:
        a=int(input("enter the number to print the pattern of triangle 1 : "))
        for i in range(1,a+1):
            for j in range(1,a+1):
                if i==j:
                    print(i,end=" ")
                else:
                     print("0 ",end="")
            print("")
    elif ch==5:
        a=int(input("enter the number to print the pattern of triangle 2 : "))
        for i in range(1,a+1):
            print("1 "*(a-i)+(str(i)+" ")*(i))
    elif ch==6:
        a=int(input("enter the number to print the pattern of triangle 3 : "))
        for i in range(1,a+1):
            print(" "*(a-i),end="")
            if i%2!=0:
                print("* "*i)
            else:
                for j in range(1,i+1):
                    print(j,end=" ")
                print(" ")
    elif ch==7:
         a=int(input("enter the number to print the pattern of triangle 4 : "))
         for i in range(a,0,-1):
             for j in range(i,0,-1):
                 print(j,end=" ")
             print(" ")
         for i in range(1,a+1):
             for j in range(i,0,-1):
                 print(j,end=" ")
             print(" ")    
         for i in range(a,0,-1):
            for j in range(1,i+1):
                print(i,end=" ")
            print(" ")    
            
    else:
        print("You has entered a wrong input please try again")
    cho=input("if you want to print another pattern : enter Y or N")
else:
        print("THANK YOU FOR USING PROGRAM")
    
