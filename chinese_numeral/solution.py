from preloaded import numerals


def to_chinese_numeral(n):
    output =""
    n_str = (str(n).split("."))
    # Split string into chars
    digit_parts = [[ch for ch in part] for part in n_str]
    # Flag for when to place zero
    zero_flag = True
    
    negative_flag = False

    # Check for negative and remove
    if digit_parts[0][0] == "-":
        negative_flag = True
        digit_parts[0].remove("-")
    # Reverse to prevent OutOfBoundsExceptions
    digit_parts[0].reverse()
    for i, v in enumerate(digit_parts[0]):
        # Convert keys to ints to access dict
        key = int(v) if v.isdigit() else v
        # Single Zero
        if ((len(digit_parts[0]) == 1)):
            output += numerals.get(key)
            break
        # Handle zer0 in decimals
        if (len(digit_parts) == 2) and len(digit_parts[0]) == 1:
            output += numerals.get(key)
            break
        #Increment through and handle place value
        if key != 0:
            if i == 0:
                output += numerals.get(key)
            if i == 1:
                output += numerals.get(10)    # 十
                if n > 9 and n < 20 or (n < -9 and n > -20):
                    pass
                else:
                    output += numerals.get(key)
            elif i == 2:
                output += numerals.get(100)   # 百
                output += numerals.get(key)
            elif i == 3:
                output += numerals.get(1000)  # 千
                output += numerals.get(key)
            elif i == 4:
                output += numerals.get(10000) # 万
                output += numerals.get(key)
            zero_flag = False
        # Decide whether to place a zero and the flag to true
        if zero_flag == False and key == 0:
            output += numerals.get(key)
            zero_flag = True

    # Convert to list, add negatives if necessary, and reverse to original order
    output = list(output)
    if negative_flag:
        output.append(numerals.get("-"))
    output.reverse()
    
    output = "".join(output)
    if len(digit_parts) == 2:
        output += numerals.get(".")
        for i, v in enumerate(digit_parts[1]):
            key = int(v) if v.isdigit() else v
            output += numerals.get(key)
    return output

# Community Solution
# def to_chinese_numeral(n, keep_ten=False, trailing_zero=False):
#     if trailing_zero: return numerals[0] + to_chinese_numeral(n, keep_ten)
#     if n < 0: return numerals['-'] + to_chinese_numeral(-n)
#     if n % 1: return to_chinese_numeral(n // 1) + numerals['.'] + ''.join(numerals[int(d)] for d in str(n).split('.')[1])
#     if n >= 10000: return to_chinese_numeral(n // 10000) + numerals[10000] + bool(n % 10000) * to_chinese_numeral(n % 10000, True, n % 10000 < 10000 // 10)
#     if n >= 1000: return numerals[n // 1000] + numerals[1000] + bool(n % 1000) * to_chinese_numeral(n % 1000, True, n % 1000 < 1000 // 10)
#     if n >= 100: return numerals[n // 100] + numerals[100] + bool(n % 100) * to_chinese_numeral(n % 100, True, n % 100 < 100 // 10)
#     if n >= 10: return bool(keep_ten or n // 10 > 1) * numerals[n // 10] + numerals[10] + bool(n % 10) * to_chinese_numeral(n % 10, True)
#     return numerals[n]
