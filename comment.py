import re
result = ''
with open('./comment.txt','r') as f:
    lines = f.readlines()
    lines=''.join(line for line in lines)
    matches = re.findall('(\/\/.*)|(\/\*(?:.*\n)*.*\*\/)', lines)
    for match in matches:
        if match[0]:
            result+=match[0] +'\n'
        if match[1]:
            result+=match[1] + '\n'
if result:
    print(result[:-1])
