appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entres = ['Burrito', 'Pizza', 'Shark Fin Soup']
desserts = ['Pie', 'Ice Cream', 'Candy']
beverages = ['Ginger Beer', 'Root Beer', 'Beer']

diner = input('What\'s your name? ')
MENU = f"""
***********************************
**  Welcome {diner}              **
**  To the Snakes Cafe!          **
**                               **
**  Please see our menu below:   **
**  (to quit, enter 'quit')      **
***********************************

Appetizers
----------
{appetizers[0]}
{appetizers[1]}
{appetizers[2]}

Entres
------
{entres[0]}
{entres[1]}
{entres[2]}

Desserts
--------
{desserts[0]}
{desserts[1]}
{desserts[2]}

Beverages
---------
{beverages[0]}
{beverages[1]}
{beverages[2]}

"""
order_prompt = "What would you like to order? "

print(MENU)

item = ''
customer_order = {}
while item != 'quit':
  item = input(order_prompt)
  if item not in appetizers and item not in entres and item not in desserts and item not in beverages:
    print("I'm sorry, we don't serve " + item + " here. Please enter something else.")
  else:
    if item not in customer_order.keys():
      customer_order[item] = 0
    customer_order[item] += 1
  print("Your order so far:")
  for key, val in customer_order.items():
    print(key, val)