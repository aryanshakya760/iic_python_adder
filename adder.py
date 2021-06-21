from gates import *

#Declaring the given inputs in Bin_Adder
def Bin_Adder(Num_1,Num_2):
    carry = 0
    result = ['0','0','0','0','0','0','0','0']
    for i in range (7,-1,-1):
        Bit0 = int(Num_1[i])
        Bit1 = int(Num_2[i])

        xor1 = xor_Gate(Bit0,Bit1)
        sum_ = xor_Gate(xor1,carry)

        and1 = and_Gate(Bit0,Bit1)
        and2 = and_Gate(xor1,carry)
        carry = or_Gate(and1,and2)

        result[i] = str(sum_)
    return "".join(result)

        
    






