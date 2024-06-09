'''num=0
def sum(num):
    total=0
    for i in range(num+1):
        total+=i
    return total
result=sum(5)
print(result)'''

# Calculate sum of N natural numbers with the formula in fraction of second
def calculate_sum(num):
    sum=num*(num+1)//2
    return sum
print(calculate_sum(5))

