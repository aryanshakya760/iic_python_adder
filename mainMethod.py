from adder import *
from conversion import *
from binaryInput import Bin_Input
from decimalInput import Dec_Input

def validation3(num1,num2):
    if num1+num2 > 255:
        return False
    else:
        return True

flag = False
while(not flag):
    status = False
    while(not status):
        print("!!_-_-_-_-_-_-_Welcome To Byte Adder_-_-_-_-_-_!!")
        choice = input(" What do you want to choose b or d: ")
        if choice.lower() in ['b','d']:
            if choice == 'b':
                print("!!! Welcome to Binary Adder !!!")
                BinNum1 = Bin_Input("First Binary number")
                BinNum2 = Bin_Input("Second Binary number")
                DecNum1 = Bin_To_Dec(int(BinNum1))
                DecNum2 = Bin_To_Dec(int(BinNum2))
                if validation3(DecNum1,DecNum2):
                    rp = Bin_Adder(BinNum1,BinNum2)
                    status = True
                    print("Your first Binary number is: ",BinNum1,"whereas it decimal value is", DecNum1)
                    print("Your Second Binary number is: ",BinNum2, "whereas its decimal value is",DecNum2)
                    print("The sum of these numbers in binary value are: ",rp,"while the sum in decimal value is",(DecNum1+DecNum2))
                    break
                else:
                    print("The sum lies between 00000000 to 11111111")      
            else:
                print("!!! Welcome to Decimal Adder !!!")
                DecNum1 = Dec_Input("First Decimal Number: ")
                DecNum2 = Dec_Input("Second Decimal Number: ")
                BinNum1 = Dec_To_Bin(DecNum1)
                BinNum2 = Dec_To_Bin(DecNum2)
                if validation3(DecNum1,DecNum2):
                    rp = Bin_Adder(BinNum1,BinNum2)
                    status = True
                    print("Your first Decimal number is: ",DecNum1,"whereas it binary value is", BinNum1)
                    print("Your second Decimal number is: ",DecNum2,"whereas it binary value is", BinNum2)
                    print("The sum of these numbers in decimal values is: ",(DecNum1+DecNum2),"while the sum in binary value is", rp)
                    break
                else:
                    print("The sum must not exceed 255")
        else:
            print("Error!! Enter b for binary and d for decimal")
    status = False
    while(not status):
        question = input("Do you want to continue? Type 0 to continue and 1 to quit: ")
        if question.lower() in ['0','1']:
            if question.lower() == '0':
                status = True
            else:
                status = True
                flag = True
        else:
            print("Enter either 0 to continue or 1 to quit")
            break
    else:
        print("Thank you for using byte adder!! ")
        
        
        
            
                
            
                
                
        
        
