# WAP print all palidrome number from 1 to 1000 :

number = []
for z in range(1,1001) :
    number.append(z)
    
    
for i in (number):
    # store a copy of this number
    temp = i

    # calculate reverse of this number
    reverse_num=0

    while(i>0):
        # extract last digit of this number
        digit=i%10
        
        # append this digit in reveresed number
        reverse_num = reverse_num*10+digit
        
        # floor divide the number leave out
        i=i // 10

        # compare reverse to original number
        if(temp==reverse_num):
            #print("the number is palidrome!")
            #print(temp)
            print("{} : {}".format(temp,"the number is palidrome!"))

input()


