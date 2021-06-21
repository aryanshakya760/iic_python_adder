#Declaring binaryInput for the Binary Adder
def Bin_Input(xyz):
    flag = False
    while(not flag):
        num = input("Enter the " +xyz+ "that lies between 00000000 and 11111111: ")
        if(validation(num) [0]):
            flag = True
            a = 8 - len(num)
            return "0" *a+num
        else:
            print("Error!", validation(num) [1])

def validation(num):
    if num == "":
        return [False, "The value is empty"]
    try:
        num1 = int(num)
    except:
        return [False, "Invalid character! Please use Binary value"]
    if(num1 < 0):
        return[False,"Invalid value! Please enter Positive Binary Value!!"]
    while (num1 >0):
        r = num1%10
        if r not in [0,1]:
            return [False, "Invalid! Please enter correct number having digits between 0 and 1"]
        num1 = int(num1/10)
    return [True]


    
        
