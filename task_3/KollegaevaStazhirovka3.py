def roman_numerals_to_int(roman_numeral):
    # Словарь сопоставления римских чисел и их десятичных значений
    roman_numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    try:
        dec_num = 0
        pred_val = roman_numerals["M"] + 1
        while roman_numeral:
            # Если первые два символа образуют допустимый римский символ
            if len(roman_numeral) >= 2 and roman_numeral[:2] in roman_numerals:
                if roman_numerals[roman_numeral[:2]] > pred_val:
                    return None
                dec_num += roman_numerals[roman_numeral[:2]]
                pred_val = roman_numerals[roman_numeral[:2]]
                # Убираем первые два символа из строки
                roman_numeral = roman_numeral[2:]
            # Если только первый символ образует допустимый римский символ
            elif roman_numeral[0] in roman_numerals:
                if roman_numerals[roman_numeral[0]] > pred_val:
                    return None
                dec_num += roman_numerals[roman_numeral[0]]
                pred_val = roman_numerals[roman_numeral[0]]
                # Убираем первый символ из строки
                roman_numeral = roman_numeral[1:]
            else:
                return None
        return dec_num
    except Exception:
        return None
