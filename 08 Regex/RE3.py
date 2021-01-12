# Aaliya Hussain
# 2nd Period

import sys
idx = int(sys.argv[1])-50
myRegexLst = [
    r"/\w*(\w)\w*\1\w*/i",
    r"/\w*(\w)(\w*\1){3}\w*/i",
    r"/^(0|1)([01]*\1)?$/",
    r"/(?=\w*cat)\b\w{6}\b/i",
    r"/(?=\w*ing)(?=\w*bri)\b\w{5,9}\b/i",
    r"/(?=\b\w{6}\b)(?!\w*cat)\w*/i", # /\b((?!cat)\w){6}\b/i
    r"/\b((\w)(?!\w*\2))+\b/i",
    r"/^(?!\w*10011)[01]*$/",
    r"/\w*([aeiou])(?!\1)[aeiou]\w*/i", # /\w*((?!.\1)[aeiou]{2}\w*/i
    r"/^(?!\w*(101|111))[01]*$/"]
print(myRegexLst[idx])