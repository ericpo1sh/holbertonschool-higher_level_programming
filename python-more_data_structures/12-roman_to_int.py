#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                  'XC': 90,
                  'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    result = 0
    flag = 0
    if roman_string and isinstance(roman_string, str):
        for i in range(0, len(roman_string)):
            if flag == 1:
                result += roman_dict[roman_string[i-1] + roman_string[i]]
                flag = 0
                continue
            else:
                if i == len(roman_string) - 1:
                    result += roman_dict[roman_string[i]]
                elif i < len(roman_dict) - 1:
                    if roman_string[i] + roman_string[i+1] in roman_dict:
                        flag = 1
                        continue
                    elif roman_string[i] in roman_dict:
                        result += roman_dict[roman_string[i]]
        return result
    else:
        return 0
