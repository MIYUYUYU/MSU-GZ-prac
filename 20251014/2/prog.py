from math import *
import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

#获取数据
def parse_value(s):
    try:
        return float(s)
    except ValueError:
        if s.startswith('"') and s.endswith('"') or s.startswith("'") and s.endswith("'"):
            return s[1:-1]
        else:
            return s

num_func_exc = 1
inp = sys.stdin.read().splitlines()
num_line = len(inp)
#print(inp)
func_dic = {"quit": "quit {} {}"}
func_exec = []
#将函数名加入字典，函数执行加入列表
for line in inp:
    line = [x.strip() for x in line.strip().split()]
    #print(line)
    if line[0].startswith(":"):
        num_func_exc += 1
        func_dic[line[0][1:]] = line[1:]
    if line[0] in func_dic:
        #print(line)
        line = [parse_value(x) for x in line ]
        func_exec.append(line)
#print(func_exec)
#print(func_dic)


#token = ['sin', 'x', 'y', 'sin(x+y)']
#fun_exc = ['sin',1,2]
def func_exe(func_name,func_data):
    token = func_dic[func_name]
    #print(f"token:{token}")
    #print(len(token))
    #print(func_data)
    if len(token) - 1 == 1 and len(func_data) > 1:
        func_data = [' '.join(func_data)]
    if len(token) == 1:
        result = eval(token[0],globals())
    else:
        f_x = token[-1]
        vars = {}
        #print(f"func_data: {func_data}")
        for i in range(len(token) - 1):
            vars.update({token[i]:func_data[i]})
        #print(vars)
        result = eval(f_x,vars, globals())

    try:
        if int(result) and result.is_integer():
              return int(result)
        else:
            return result
    except ValueError:
        return result

#执行函数列表里的函数
for func in func_exec:
    #print(f"func:{func}")
    if func[0] == "quit":
        print(f"{num_func_exc}, {num_line}")
        break
    elif func[0] not in func_dic:
        continue
    else:
        print(func_exe(func[0],func[1:]))
