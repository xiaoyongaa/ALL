import re
shi="8*12+(6-(5*6-2))+(1+1)"
result=re.search(r"\(([\+\-\*\/]*\d){0,}\)",shi)
print(result.group())


#\(([\+\-\*\/]*\d){0,}\)