water_tank_length = int(input())
water_tank_height = int(input())
water_tank_width = int(input())
used_percents = float(input())

water_tank_volume = water_tank_length * water_tank_height * water_tank_width
water_tank_volume_in_cubic_dm = water_tank_volume * 0.001
used_space = used_percents * 1 / 100
litters_need = water_tank_volume_in_cubic_dm * (1 - used_space)
print(litters_need)