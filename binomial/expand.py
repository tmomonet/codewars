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

    def var_pow(var, p):
        if not var or p == 0:
            return ""
        if p == 1:
            return var
        return f"{var}^{p}"

    def term_to_str(coeff, a_var, i, b_var, j, is_first=False):
        # Build variable part
        vp = var_pow(a_var, i) + var_pow(b_var, j)

        if vp:
            if coeff == 1:
                core = vp
            elif coeff == -1:
                core = "-" + vp
            else:
                core = f"{abs(coeff)}{vp}" if coeff < 0 else f"{coeff}{vp}"
        else:
            core = str(abs(coeff)) if coeff < 0 else str(coeff)

        if is_first:
            return core if coeff >= 0 else "-" + core.lstrip("-") 
        else:
            return ("+" if coeff >= 0 else "-") + core.lstrip("-")

    for i in range(exponent, -1, -1):
        j = exponent - i

        sign_a = -1 if is_negative(m.group(1), i) else 1
        sign_b = -1 if is_negative(m.group(4), j) else 1

        coeff = pascal_coeff(triangle, j) * (coef_a ** i) * (coef_b ** j) * sign_a * sign_b

        a_var = m.group(3) or ""
        b_var = m.group(6) or ""

        if j == exponent:
            if sign_a * sign_b == -1:
                output += "-" + str(coef_b ** j)
            else:
                output += "+" + str(coef_b ** j)
        else:
            output += term_to_str(coeff, a_var, i, b_var, j, is_first=(i == exponent))

    return output

import re


# Community Solution
# P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')

# def expand(expr):
#     a,v,b,e = P.findall(expr)[0]
    
#     if e=='0': return '1'
    
#     o   = [int(a!='-' and a or a and '-1' or '1'), int(b)]
#     e,p = int(e), o[:]
    
#     for _ in range(e-1):
#         p.append(0)
#         p = [o[0] * coef + p[i-1]*o[1] for i,coef in enumerate(p)]
    
#     res = '+'.join(f'{coef}{v}^{e-i}' if i!=e else str(coef) for i,coef in enumerate(p) if coef)
    
#     return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-','-')
