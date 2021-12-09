def knapsackBruteForce(w,price,weight,idx,currPrice,currKnap):
    if weight==0:
        print("Current Knapsack- ",currKnap)
        print("Current Price- "+str(currPrice))
        return 0
    if idx==-1:
        print("Current Knapsack- ",currKnap)
        print("Current Price- "+str(currPrice))
        return 0
    op1=0
    op2=0
    if (weight>=w[idx]):
        currKnap.append(w[idx])
        op1+=knapsackBruteForce(w,price,weight-w[idx],idx-1,currPrice+price[idx],currKnap)+price[idx]
        currKnap.pop()
    op2+=knapsackBruteForce(w,price,weight,idx-1,currPrice,currKnap)
    return max(op1,op2)

n=int(input("Enter number of Items: "))
w=[]
price=[]

for i in range(0,n):
    w.append(int(input("Enter weight of item no- "+str(i+1)+" ")))
    price.append(int(input("Enter price of item no- "+str(i+1)+" ")))

weight= int(input("Enter capacity of the knapsack - "))
currKnap=[]
print("Maximum Profit- " +str(knapsackBruteForce(w,price,weight,n-1,0,currKnap)))
