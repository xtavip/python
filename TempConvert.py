# TempConvert.py
TempStr = input("Please enter a temperature value with a symbol(e.g. 25.3c or 38.9f):")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("The converted temperature is {:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("The converted temperature is {:.2f}F".format(F))
else:
    print("Input format error.")

