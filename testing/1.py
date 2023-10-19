dick = {
    "I": 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def romanToInt(str: str):
    str = str.replace("IV", "IIII")
    str = str.replace("IX", "VIIII")
    str = str.replace("XL", "XXXX")
    str = str.replace("XC", "LXXXX")
    str = str.replace("CM", "DCCCC")

    num = 0
    count = 0
    for i in range(len(str)):
        num += dick.get(str[i])
    return num


if __name__ == '__main__':
    roman = "LIX"
    print(f'Output: {romanToInt(roman)}')
