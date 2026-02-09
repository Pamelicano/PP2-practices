
def convert_to_number(s):
    mapping = {
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOU': 4,
        'FIV': 5,
        'SIX': 6,
        'SEV': 7,
        'EIG': 8,
        'NIN': 9,
        'ZER': 0
    }
    num_str = ''
    for i in range(0, len(s), 3):
        triplet = s[i:i+3]
        num_str += str(mapping[triplet])
    return int(num_str)

def convert_to_string(num):
    mapping = {
        1: 'ONE',
        2: 'TWO',
        3: 'THR',
        4: 'FOU',
        5: 'FIV',
        6: 'SIX',
        7: 'SEV',
        8: 'EIG',
        9: 'NIN',
        0: 'ZER'
    }
    num_str = str(num)
    result = ''
    for digit in num_str:
        result += mapping[int(digit)]
    return result

s = input()
s1 = ""
op = "" 
s2 = "" 
for i in range(len(s)):
    if (s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/"): 
        s1 = s[:i]
        op = s[i]
        s2 = s[i+1:]
        break
num1 = convert_to_number(s1)
operation = op
num2 = convert_to_number(s2)

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
print(convert_to_string(result))