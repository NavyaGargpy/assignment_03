#QUESTION 5

H_w = 1.00794
C_w = 12.0107
O_w = 15.9994

H = int(input("Enter number of hydrogen atoms: "))
C = int(input("Enter number of carbon atoms: "))
O = int(input("Enter number of oxygen atoms: "))
         
weight = H*H_w + C*C_w + O*O_w

print("The molecular weight of the compound is", weight)