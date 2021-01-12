# Aaliya Hussain
# 2nd Period

import sys
idx = int(sys.argv[1])-40
myRegexLst = [
    r"/^[x.o]{64}$/i",
    r"/^[xo]*\.[xo]*$/i",
    r"/^(x+o*)?\.|\.(o*x+)?$/i",
    r"/^.(..)*$/s",
    r"/^(0([01]{2})*|(1[01]([01]{2})*))$/", # /^(1?0|11)([01]{2})*$/
    r"/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
    r"/^(10|0)*1*$/", #as many 0s, 1 with 0s, and 1s (not followed by 0) /^(1?0)*1*$/
    r"/^([bc]+|[bc]*a[bc]*)$/",
    r"/^([bc]|([bc]*a){2})+$/", # /^(a[bc]*a|b|c)+$/
    r"/^([02]|((1[02]*1|2)(([02]*1){2}|[02]*)+))$/"] # /^((1[02]*1|2)0*)$/
print(myRegexLst[idx])