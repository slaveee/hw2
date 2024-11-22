start = int(input("введите начало: "))
end = int(input("введите конец: "))

if start > end:
    print("напиши так что бы было больше первого")
else:
    sum_ev = 0
    sum_o = 0
    sum_9 = 0
    count_ev = 0
    count_o = 0
    count_9 = 0
    
    current = start
    while current <= end:
        if current % 2 == 0:
            sum_ev += current
            count_ev += 1
        else:
            sum_o += current
            count_o += 1
        
        if current % 9 == 0:
            sum_9 += current
            count_9 += 1
            
        current += 1

    avg_ev = sum_ev / count_ev if count_ev > 0 else 0
    avg_o = sum_o / count_o if count_o > 0 else 0
    avg_9 = sum_9 / count_9 if count_9 > 0 else 0

    print("сумма четных чисел:", sum_ev, "среднее арифметическое четных чисел:", avg_ev)
    print("сумма нечетных чисел:", sum_o, "среднее арифметическое нечетных чисел:", avg_o)
    print("сумма чисел, кратных 9:", sum_9, "среднее арифметическое чисел, кратных 9:", avg_9)