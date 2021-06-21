#Declaring decimalInput for the Binary Adder
def Dec_Input(xyz):
    flag = False
    while(not flag):
        num = input("Enter the " +xyz+ "that lies between 0 and 255: ")
        if(validation(num) [0]):
            flag = True
            return int(num)
        else:
            print("Error!", validation(num) [1])

def validation(num):
    if num == "":
        return [False, "The value is empty"]
    try:
        num1 = int(num)
    except:
        return [False, "Invalid character.Please use only Decimal value"]
    if(num1 < 0):
        return [ False, "Invalid value. Please enter positive Decimal number"]
    if(num1 > 255):
        return [False, "Invalid!! The value must not exceed 255"]
    return [True]

