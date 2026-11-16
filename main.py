print("menu")
menu={"burger":120,"pizza":250,"coke":40,"fries":80} 
for k,v in menu.items():
    print(k,v)
def console_food(menu):
    total=0
    subtotal=0
    discount=0
    prize=0
    cart={}
    while True:
      try:
        var= int(input("enter total variety of food you want:"))
        break
      except ValueError:
          print("only whole no. are valid input")
          
    if str(var) not in "1234":
          print("invalid input only 4 varieties available")
          return console_food(menu)
      
    for i in range(var):
        item=input("enter food you want: ").strip()
        food=item.lower()
        if food not in menu:
            print('food not available,menu : burger,pizza,coke,fries')
            return console_food(menu)
        for j in menu:
            if j==food:
                prize=menu[j]
        while True:
            try:
               quantity=int(input('enter your desired quantity of food : '))
               break
            except ValueError:
                 print("invalid input only whole numbers are valid")
        if quantity<1:
            print("quantity should be greater than 0")
        cart[item]=[quantity,prize]
    for k in cart:
        subtotal+=cart[k][1]
    coupon_availability=input('enter yes if you have coupon ').lower()
    if quantity<1:
        print("add atleast 1")
    if coupon_availability=="yes":
            coupon_code= input("enter valid coupon code : ")
            if coupon_code=="SAVE10":
                   discount = subtotal*10/100
                   subtotal-=discount
            else:
                    print("invalid coupon only SAVE10 is available")
                    
    if subtotal<300:
        subtotal+=40 #delivery charge
        print("40 rupees added as a delivery charge")
    gst_charge=subtotal*5/100
    total=subtotal+gst_charge
    
    checkout=input('enter yes if you want to checkout bill ').lower()
    if checkout=="yes":
        def checkout():
            print(cart)
            print("subtotal=",subtotal)
            print("discount=",discount)
            print("gst_charge=",gst_charge)
            print('total amount',total)
            print("thanks for visiting\nhave a nice day.")
        checkout()  
console_food(menu)


