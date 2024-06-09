'''
def bubble_sort(elements,key='transaction_amount'):  # it will sort the list based on the transaction
    size=len(elements)
    
    for i in range(size-1):
        for j in range(size-1):
            a=elements[j][key]
            b=elements[j+1][key]
            if a>b:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp

if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(elements,key='transaction_amount')
    print(elements)
    '''
    
def bubble_sort(elements,key='name'):  # it will sort the list based on the transaction
    size=len(elements)
    
    for i in range(size-1):
        for j in range(size-1):
            a=elements[j][key]
            b=elements[j+1][key]
            if a>b:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp

if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(elements,key='name')
    print(elements)
    