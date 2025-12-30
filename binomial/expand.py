import re


def expand(expr):
    output = ""

    def pascal(n):
        mat = []
        for row in range(n):
            arr = []
            for i in range(row + 1):
                if row == i or i == 0:
                    arr.append(1)
                else:
                    arr.append(mat[row - 1][i - 1] + mat[row - 1][i])
            mat.append(arr)
        return mat

    pattern = re.compile("\((-)?([0-9]*)?([a-z])?\s*([-+])+\s*([0-9]*)?([a-z])?\)\s*\^\s*([0-9]+)")
    m = re.search(pattern, expr)
    if m:
        print("MATCH:", m.groups())
    else:
        print("NO MATCH")

    exponent = (int(m.group(7)))

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
    print(triangle)

    def is_negative(match_obj, power):
        return match_obj and (power % 2 != 0)

    def pascal_coeff(triangle, iteration, constant, power):
        if power > 1:
            const = str((triangle[-1][iteration] * int(constant)) ^ int(power))
            return const
        if power == 1:
            const = str((triangle[-1][iteration] * int(constant)))

    for i in range(exponent, -1, -1):
        j = exponent - i
        print(i, j)
        if is_negative(m.group(1), i) == True:
            if m.group(2) == "":
                output += "-" + m.group(3) + "^" + str(i)
            else:
                if i != exponent:
                    output += " + " + m.group(3) + "^" + str(i)
                else:
                    output += m.group(3) + "^" + str(i)


        else:
            if m.group(2) == "":
                if i != exponent:
                    output += " + " + m.group(3) + "^" + str(i)
                else:
                    output += m.group(3) + "^" + str(i)
            else:
                if i != exponent:
                    output += " + " + m.group(3) + "^" + str(i)
                else:
                    output += m.group(3) + "^" + str(i)

    #     if first_neg:
    #         output += "-"

    print(output)
    return output
