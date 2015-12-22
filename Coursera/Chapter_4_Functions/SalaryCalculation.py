def calcute_salary(hour,rate):
    if hour <= 40:
        return 40 * rate
    else:
        return  40 * rate + ( hour - 40 )*rate*1.5

print calcute_salary(45,10)