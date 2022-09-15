import re

n = int(input())
result =""
for i in range(n):
    line = input()
    matches = re.findall('([a-zA-Z0-9\_]+(?:\.[a-z-A-Z0-9\_]*)*\@(?:[a-zA-Z0-9\_]+)(?:\.[a-z-A-Z0-9\_]*)*(?:\.[a-zA-Z0-9]{1,4}))',line)
    #print(matches)
    for match in matches:
        result+=match
        result+=';'
if result:
    print(result[:-1])
        