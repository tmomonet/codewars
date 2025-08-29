# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3

class VigenereCipher(object):
2
    def __init__(self, key, alphabet):
3
        self.key = key
4
        self.alphabet = alphabet
5
        
6
        
7
    def encode(self, text):
8
        txt = list(text)
9
        output = ""
10
        for i, ch in enumerate(txt):
11
            if ch not in self.alphabet:
12
                output += ch
13
                continue
14
            idx = self.alphabet.index(ch)
15
            key_ch = self.key[i % len(self.key)]
16
            shift = self.alphabet.index(key_ch)
17
            output += self.alphabet[(idx + shift) % len(self.alphabet)]   
18
        return output
19
    
20
    def decode(self, text):
21
        txt = list(text)
22
        output = ""
23
        for  i, ch in enumerate(text):
24
            if ch not in self.alphabet:
25
                output += ch
26
                continue
27
            idx = self.alphabet.index(ch)
28
            key_ch = self.key[i % len(self.key)]
29
            shift = self.alphabet.index(key_ch)
30
            output += self.alphabet[(idx - shift) % len(self.alphabet)]
31
        return output
32
# ​
# Community Solution
# class VigenereCipher(object):
#     def __init__(self, key: str, alphabet: str):
#         self.alphabet = list(alphabet)
#         self.key = [alphabet.index(i) for i in key]

#     def encode(self, text):
#         return "".join([self.alphabet[(self.alphabet.index(text[i]) + self.key[i % len(self.key)]) % len(self.alphabet)]
#                         if text[i] in self.alphabet else text[i] for i in range(len(text))])

#     def decode(self, text):
#         return "".join([self.alphabet[(self.alphabet.index(text[i]) - self.key[i % len(self.key)]) % len(self.alphabet)]
#                         if text[i] in self.alphabet else text[i] for i in range(len(text))])
