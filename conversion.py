## conversion of Decimal number into Binary Number

def Bin_To_Dec(Numb):
    i = 0
    desc = 0
    while(Numb>0):
        r = Numb%10
        desc = desc + r*(2**i)
        i = i + 1
        Numb = int(Numb/10)
    return desc


def Dec_To_Bin(Numb):
    p = ["0","0","0","0","0","0","0","0"]
    i = 7
    while (Numb>0):
        r = Numb%2
        p[i] = str(r)
        Numb = int(Numb/2)
        i = i-1
    return "".join(p)
