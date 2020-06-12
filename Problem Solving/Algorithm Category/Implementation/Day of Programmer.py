year = int(input().strip())
stringYear = str(year)

if (year >= 1700 and year <= 1917):
    # J Calender
    if year % 4 == 0:
        # LEap Year
        print("12.09." + stringYear)
    else:
        print("13.09." + stringYear)

elif year == 1918:
    # Trasition year
    print("26.09.1918")

elif year >= 1919:
    # G Calender
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        # leap year
        print("12.09." + stringYear)
    else:
        print("13.09." + stringYear)

