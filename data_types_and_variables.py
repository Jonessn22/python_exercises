#DATA TYPES AND VARIABLES

#1
movie_1 = 'Little Mermaid'
movie_2 = 'Brother Bear'
movie_3 = 'Hercules'

days_one = 3
days_two = 5
days_three = 1

price = 3.00

price_1 = price * days_one
price_2 = price * days_two
price_3 = price * days_three

print(movie_1 + ' costs $' + str(price_1))
print(movie_2 + ' costs $' + str(price_2))
print(movie_3 + ' costs $' + str(price_3))

#2
#companies
co_1 = 'Google'
co_2 = 'Amazon'
co_3 = 'Facebook'

#pay per hour
pph_1 = 400.00
pph_2 = 380.00
pph_3 = 350.00

#hours worked
h1 = 6
h2 = 4
h3 = 10

#total pay
p1 = pph_1 * h1
p2 = pph_2 * h2
p3 = pph_3 * h3
pay = p1 + p2 + p3

print('Total pay for for this week is $' + str(pay))

#3
class_full = False
schedule_conflict = False
can_enroll = not class_full and not schedule_conflict

print(can_enroll)

#4
min_purchase = 2 + 1
offer_expired = False 
premium_member = True

prod_offer = (min_purchase > 2 and not offer_expired) or premium_member
print(prod_offer)

#5
username = 'codeup'
password = 'notastrongpassword'

pw_min_length = 5
un_max_length = 20
same = username == password

valid_pw = pw_min_length >= 5 and un_max_length <= 20 and not same
print(valid_pw)


