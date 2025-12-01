import sys
import math


def interpret_assembly(program):
    # 第一阶段：解析和标签收集
    lines = program.strip().split('\n')
    instructions = []
    labels = {}
    line_map = []  # 存储原始行号到指令索引的映射

    for line_num, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        # 分离标签和指令部分
        parts = line.split(maxsplit=1)

        # 检查是否有标签
        label = None
        if parts[0].endswith(':'):
            label = parts[0][:-1]
            if len(parts) > 1:
                instruction_part = parts[1]
            else:
                instruction_part = ""
        else:
            instruction_part = line

        # 处理标签
        if label is not None:
            labels[label] = len(instructions)

        # 解析指令（如果有）
        if instruction_part:
            instruction = parse_instruction(instruction_part)
            if instruction is not None:
                instructions.append(instruction)
                line_map.append(line_num)

    # 第二阶段：执行指令
    variables = {}
    pc = 0  # 程序计数器

    while 0 <= pc < len(instructions):
        instr = instructions[pc]
        op = instr[0]

        if op == 'stop':
            break

        elif op == 'store':
            _, value_str, dest = instr
            try:
                value = float(value_str)
            except ValueError:
                value = 0.0
            variables[dest] = value
            pc += 1

        elif op in ('add', 'sub', 'mul', 'div'):
            _, src1, src2, dest = instr
            val1 = variables.get(src1, 0.0)
            val2 = variables.get(src2, 0.0)

            if op == 'add':
                result = val1 + val2
            elif op == 'sub':
                result = val1 - val2
            elif op == 'mul':
                result = val1 * val2
            elif op == 'div':
                if val2 == 0:
                    result = math.inf
                else:
                    result = val1 / val2

            variables[dest] = result
            pc += 1

        elif op in ('ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'):
            _, src1, src2, label = instr
            val1 = variables.get(src1, 0.0)
            val2 = variables.get(src2, 0.0)

            condition_met = False
            if op == 'ifeq':
                condition_met = (val1 == val2)
            elif op == 'ifne':
                condition_met = (val1 != val2)
            elif op == 'ifgt':
                condition_met = (val1 > val2)
            elif op == 'ifge':
                condition_met = (val1 >= val2)
            elif op == 'iflt':
                condition_met = (val1 < val2)
            elif op == 'ifle':
                condition_met = (val1 <= val2)

            if condition_met:
                if label in labels:
                    pc = labels[label]
                else:
                    # 未定义标签，程序不执行
                    return
            else:
                pc += 1

        elif op == 'out':
            _, src = instr
            value = variables.get(src, 0.0)
            print(value)
            pc += 1


def parse_instruction(line):
    """解析单行指令，返回指令元组或None（如果无效）"""
    parts = line.split()
    if not parts:
        return None

    op = parts[0]

    # 检查指令和参数个数
    if op == 'stop' and len(parts) == 1:
        return ('stop',)
    elif op == 'store' and len(parts) == 3:
        return ('store', parts[1], parts[2])
    elif op in ('add', 'sub', 'mul', 'div') and len(parts) == 4:
        return (op, parts[1], parts[2], parts[3])
    elif op in ('ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle') and len(parts) == 4:
        return (op, parts[1], parts[2], parts[3])
    elif op == 'out' and len(parts) == 2:
        return ('out', parts[1])
    else:
        return None



# 从标准输入读取程序
program = sys.stdin.read()

# 第一遍扫描：收集所有标签
lines = program.strip().split('\n')
labels = {}
current_pos = 0

for line in lines:
    line = line.strip()
    if not line:
        continue

    # 检查是否有标签
    parts = line.split(maxsplit=1)
    if parts[0].endswith(':'):
        label = parts[0][:-1]
        labels[label] = current_pos

    # 如果是有效指令，增加指令位置
    if parse_instruction(line.split(':', 1)[-1].strip() if ':' in line else line):
        current_pos += 1

# 检查所有跳转指令中的标签是否都存在
has_undefined_label = False
for line in lines:
    line = line.strip()
    if not line:
        continue

    # 移除可能的标签
    if ':' in line:
        line = line.split(':', 1)[-1].strip()

    instr = parse_instruction(line)
    if instr and instr[0] in ('ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'):
        label = instr[3]
        if label not in labels:
            has_undefined_label = True
            break

# 如果没有未定义的标签，执行程序
if not has_undefined_label:
    interpret_assembly(program)