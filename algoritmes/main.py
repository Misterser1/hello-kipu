your_money = 100000

if your_money <= 10000:
    result = your_money * 0.13
    print("Налог равен:", result)
elif your_money >= 10000 and your_money <= 50000:
    result = your_money * 0.2
    print("Налог равен:", result)
else:
    result = your_money * 0.3
    print("Налог равен:", result)