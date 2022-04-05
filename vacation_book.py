number_of_pages = int(input())
pages_per_hour = int(input())
days_need = int(input())

time_reading_all_book = number_of_pages / pages_per_hour

hours_per_day = time_reading_all_book / days_need

print(int(hours_per_day))