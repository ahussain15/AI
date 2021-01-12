# Aaliya Hussain
# 2nd Period

import sys
idx = int(sys.argv[1])-71
myRegexLst = [
    r"/(?=.*(\w)(.*\1){3})^\w{,6}$/im",
    r"/(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u)^\w{,7}$/im",
    r"/(?=^([^aeiou]*[aeiou]){5}[^aeiou]*$)^\w{17,}$/im",
    r"/^(\w)(\w)(\w)\w{7,}\3\2\1$/im",
    r"/(?=.*(\w)\1)^\w{20,}$/im",
    r"/(?=.*(\w)(.*\1){5,})^\w*$/im",
    r"/(?=.*((\w)\2.*){3})^\w{13,}$/im",
    r"",
    r"",
    r"/(?!.*(\w)(.*\1){2})^\w{18,}$/im",
    ]
print(myRegexLst[idx])