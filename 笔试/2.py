def check_braces(sample):
    result = []
    for w in sample:
        stack = [] #存储左括号
        record = [' '] * len(w) #为检查括号做标记
        #检查左括号的数量是否和右括号匹配
        for i, char in enumerate(w):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    record[i] = '?' #右括号多出来了
        while stack:
            record[stack.pop()] = 'x'#左括号多出来了
        result.append(w)
        result.append(''.join(record))
    return result
