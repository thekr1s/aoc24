
line="TCTNTNTNTTNTHETCTCTTCTNTCTU_NOCECELNHUN_NEENTETUUN_ONETNTTNIETIU"
mapping = {
    'H':'[',
    'O':']',
    'L':',',
    'I':'.',
    
    'C':'C',

    'T':'T',
    'N':'N',
    'E':'>',
    'U':'<',
    '_':'_',
    
}

# t 20
# n 14
# e 8
# c 7
# u 5
# h 2
# o 2
# l 1

for key in mapping:
    line=line.replace(key, mapping[key])
print(line)