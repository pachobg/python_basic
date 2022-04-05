nylon = int(input())
paint = int(input())
thinner = int(input())
price_per_hour = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint + paint * 0.1) * 14.50
thinner_price = thinner * 5
shopp_bill = nylon_price + paint_price + thinner_price + 0.40
work_salary = (shopp_bill * 0.3) * price_per_hour
total_bill = shopp_bill + work_salary
print(total_bill)
