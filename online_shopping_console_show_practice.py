# add remove search show clear

basket=['apple','peach']

while True:
    inquire=input('enter command >>>').strip().lower()
    if inquire=='add':
        product=input('enter your product name you want to add to basket>>>')
        if product in basket:
            product_count=basket.count([product])
            while True:
                confirmation=input(f'there is a {product} in your basket! do you still want to add it to your basket? (y/n)').strip().lower()
                if confirmation=='y':
                    basket.append(product)
                    print(f'{product} has been added to your basket')
                    break
                elif confirmation=='n':
                    print(f'request has beeen canceled')
                    break
                else:
                    print('Please enter (y,n)!')
        else:
            basket.append(product)
            print(f'{product.capitalize()} has been added to your basket')
    elif inquire=='remove':
        product=input(f'Please write a product name you want to delete >>>')
        if product in basket:
            while True:
                confirmation=input(f'Are you sure you want to remove {product} from your basket? (y/n)')
                if confirmation=='y':
                    basket.remove(product)
                    print(f'{product} has been removed from your basket')
                    break
                elif confirmation=='n':
                    print(f'{product} has been remaining in your basket')
                    break
                else:
                    print('Please enter only y/n!!')
        else:
            basket.remove(product)
            print('{product} has been removed from your basket')


    elif inquire=='show':
        product_count=len(basket)+1
       
        if product_count>1:
            print(f'there are {product_count} products in your basket')
            print(basket)
        elif product_count==1:
            print(f'There is only one product')
            print(basket)
        else:
             print('There is no product in your basket')
             print(basket)
        
    elif inquire=='exit':
        break
        
    else:
        print('Please check your command!')

