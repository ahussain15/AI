import sys
idx = int(sys.argv[1])-60
myRegexLst = [
    r"/(?!.*010)^[01]*$/",
    r"/(?!.*(101|010))^[01]*$/",
    r"",
    r"",
    r"",
    r"",
    r"",
    r"",
    r"",
    r"",
    ]
print(myRegexLst[idx])