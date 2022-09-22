#An ecommerce program in python using dictionaries
#products={
#    "1": {"name":"Laptop","price":15000.0,"quantity":10},
 #   "2":{"name":"Phones", "price": 400.0,"quantity":300}
#}
#while True:
#    print("1. Add a product \n2. Delete a product\n3. List Products\n4.")
 #   option=input("Enter your choice:")
  #  if option == "1":
   #     product_id = input("Enter product ID:")
    #    product_name=input("Enter product name")
     #   Product_price=("Enter prodduct price")
      #  product_quantity=("Enter product quantity")
      #  if product_id in productd:
       #     print("Sorry, product ID already exists")
        #    break
        #products[product_id]={
         #   "name":product_name,
          #  "price":Product_price,
          #  "quatity": product_quantity
        #}
        #elif option=="2":
         #   product_id=input("Enter procuct ID:")
          #  if product_id in products:
           #     del products[product_id]
            #    else:
             #       print(f"Product not found)")

              #  option =="3"
               # for product_id, ptoduct_details in products.items():
                #    print(f"Product ID:" {product_id}, \ Product name: {pro})
D = dict() 
for x in enumerate(range(2)): 
    D[x[0]] = x[1] 
    D[x[1]+7] = x[0] 
print(D)

