import math

def prime_numbers(low, high):
    Numbers = []
    try:
        # Преобразуем аргументы в числа и округляем вверх
        low, high = int(math.ceil(float(low))), int(math.ceil(float(high)))

        if low <= high and low > 0:
            # Перебираем числа в диапазоне от low до high
            for number in range(low, high + 1):
                if number > 1:
                    # Проверяем, является ли число простым
                    for i in range(2, number//2 + 1):
                        if number % i == 0:
                            break
                    else:
                        Numbers.append(number)
        return Numbers
    except (ValueError, TypeError):
        return Numbers
