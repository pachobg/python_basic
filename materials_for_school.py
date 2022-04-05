pens = int(input())
markers = int(input())
cleaner = int(input())
percent_bonus = int(input())

pen_price = pens * 5.80
markers_price = markers * 7.20
cleaner_price = cleaner * 1.20

total_sum = pen_price + markers_price + cleaner_price

bonus = total_sum * percent_bonus / 100

bill = total_sum - bonus
print(bill)
