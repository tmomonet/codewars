import re

def expand(expr):
    output = ""

    def pascal(n):
        mat = []
        for row in range(n+1):
            arr = []
            for i in range(row + 1):
                if row == i or i == 0:
                    arr.append(1)
                else:
                    arr.append(mat[row - 1][i - 1] + mat[row - 1][i])
            mat.append(arr)
        return mat

    pattern = re.compile(r"\((-)?([0-9]*)?([a-z])?\s*([-+])+\s*([0-9]*)?([a-z])?\)\s*\^\s*([0-9]+)")
    m = re.search(pattern, expr)
    
    exponent = (int(m.group(7)))

    coef_a = m.group(2)
    coef_a = int(coef_a) if coef_a else 1

    coef_b = m.group(5)
    coef_b = int(coef_b) if coef_b else 1

    # base case of "^0"
    if exponent == 0:
        return "1"

    # base case of "^1"
    if exponent == 1:
        if m.group(1):
            return (m.group(1) + m.group(2) + m.group(3) + m.group(4) + m.group(5))
        else:
            return (m.group(2) + m.group(3) + m.group(4) + m.group(5))

    triangle = pascal(exponent)
    print(expr)

    def is_negative(match_obj, power):
        if match_obj:
            return match_obj == "-" and (power % 2 != 0)
        else:
            return False

    def pascal_coeff(triangle, index):
        print(triangle[-1], index)
        return triangle[-1][index]

    for i in range(exponent, -1, -1):
        j = exponent - i
        sign_a = -1 if is_negative(m.group(1), i) else 1
        sign_b = -1 if is_negative(m.group(4), j) else 1
        a_term = pascal_coeff(triangle, j) * (coef_a ** i) * sign_a
        b_term = (coef_b ** j) * sign_b
        final_term = (a_term * b_term)
        a_var = m.group(3)
        b_var = m.group(5)
        if i == exponent:
            if is_negative(m.group(1), i):
                #consider logic for variables in second term
                if coef_a == 1:
                    output += ("-" + a_var + "^" + str(i))
                else:
                    output += ("-" + str((int(coef_a)) ** i) + a_var + "^" + str(i))
            else:
                output += (str((int(coef_a)) ** i) + a_var + "^" + str(i))
        elif j == exponent:
            if is_negative(m.group(4), j):
                output += ("-" + str((int(coef_b)) ** j))
            else:
                output += ("+" + str((int(coef_b)) ** j))
        else:
            if final_term < 0:
                if i == 1:
                    output += ("-" + str((int(coef_b)) ** i))
                else:
                    output += ("-" + str((abs(final_term))) + a_var + "^" + str(i))
            else:
                if i == 1:
                    output += ("-" + str((int(coef_b)) ** i))
                else:
                    output += ("+" + str(((final_term)) ** i) + a_var + "^" + str(i))
    return output


print(expand("(x+1)^0"), "1")
print(expand("(x+1)^1"), "x+1")
# print(expand("(x+1)^2"), "x^2+2x+1")

print(expand("(x-1)^0"), "1")
print(expand("(x-1)^1"), "x-1")
# print(expand("(x-1)^2"), "x^2-2x+1")

print(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
print(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
print(expand("(7x-7)^0"), "1")

print(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")
print(expand("(-2k-3)^3"), "")
