def rgb(r, g, b):
    
    def toHex(num):
        if num < 0: return "00"
        if num > 255: return "FF"
        return format(num, '02x').upper()
    return toHex(r) + toHex(g) + toHex(b)
