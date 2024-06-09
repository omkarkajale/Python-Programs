cost=int(input("Enter the cost price"))
selling=int(input("Enter the selling price"))
if(selling>cost):
    print('profit of',selling-cost,'on',cost)
elif(cost>selling):
    print('loss of',selling)