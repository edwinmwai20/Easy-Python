# Python Pizza Order Cost Calculator


def Pizza_cost():

    print("n\ Welcome to the pizza Place")
    print('n\Small pizza - $8')
    print("n\Large pizza - $12")
    print("n\Topping 1$ for each additional topping")
    print("n\Delivery fee $2 for first 5 miles")
    print('n\ $1 for each additional mile')
    

    piz_size = input(("Enter your preferred pizz size: "))
    topping = input("Enter number of toppings(1-3): ")
    del_dis = input("Whats the distance for delivery: ")

    if (piz_size == small):
        base_price = 8
    elif(piz_size == large):
        base_price = 12
    else:
        print('Invalid reponse')

    
    topping_cost = topping * 1


    if (del_dis == 0):
        delivery_fee = 0
    elif(del_dis <=5):
        delivery_fee = 2
    else:
        delivery_fee = delivery_fee + (del_dis -5)*1


    final_cost = base_price + topping_cost + delivery_fee  


Pizza_cost()