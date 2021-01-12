# Aaliya Hussain
# 2nd Period

import sys
idx = int(sys.argv[1])-30
myRegexLst = [
    r"/^0$|^10[01]$/",
    r"/^[01]*$/",
    r"/0$/",
    r"/\w*[aeiou]\w*[aeiou]\w*/i",
    r"/^0$|^1[01]*0$/",
    r"/^[01]*110[01]*$/",
    r"/^.{2,4}$/s",
    r"/^\d{3}\s*-?\s*\d{2}\s*-?\s*\d{4}$/",
    r"/^.*?d\w*/im",
    r"/^0*$|^1*$|^0+[01]*0+$|^1+[10]*1+$/"]
print(myRegexLst[idx])