print ("Welcome to the RS \n")
print("Please read instructions before using")

def main():
    list0 = [ ]
    for rank0 in range(0, 84):
        rank0+=1
        list0.append(rank0)
        
        
    list = [ ]
    maxLength = (15*10^23)
    while len(list) <= maxLength:
        intro = input("Total or Record: ")
        if (intro == "Total"):
            deduction001 = int(input("Enter # of Deductions: "))
            preResult = 340 - deduction001
            if any([preResult == preResult for rank0 in list0]):
                
                print("Bronze")
            return main()
main()