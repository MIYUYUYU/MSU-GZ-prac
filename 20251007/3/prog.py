from fractions import Fraction

from prompt_toolkit.key_binding.bindings.named_commands import end_of_file

inp = []
try:
    while True:
        line = input().strip()
        if not line:  # 空行则停止
            break
        inp.append(line)
except EOFError:
    pass

w = len(inp)
h = len(inp[0])
layer_gas = 0
layer_liquid = 0
for i in range(1, w):
    if inp[i][1] == '.':
        layer_gas += 1
    if inp[i][1] == '~':
        layer_liquid += 1
#print(f"layer_gas: {layer_gas} layer_liquid: {layer_liquid}")
amount_gas = layer_gas*(len(inp[0])-2)
amount_liquid = layer_liquid*(len(inp[0])-2)
if amount_liquid % (w-2) == 0:
    layer_out_liquid = amount_liquid // (w-2)
else:
    layer_out_liquid = int(amount_liquid/(w-2))+1
layer_out_gas = h-2-layer_out_liquid
bottle = ''.join(['#'] * w)
#print(round(amount_liquid/(w-2)))
#print(f"layer_out_gas: {layer_out_gas} layer_out_liquid: {layer_out_liquid}")

output = []
output.append(bottle)
for _ in range(layer_out_gas):
    output.append(''.join(['#']+['.']*(w-2)+['#']))
for _ in range(layer_out_liquid):
    output.append(''.join(['#']+['~']*(w-2)+['#']))
output.append(bottle)

print('\n'.join(output))
if layer_out_gas > layer_out_liquid:
    partion_liquid = round(20*Fraction(amount_liquid,amount_gas))
    str_gas = f"{amount_gas}/{amount_liquid + amount_gas}"
    str_liquid = f"{amount_liquid}/{amount_liquid + amount_gas}"
    max_len = max(len(str_gas), len(str_liquid))
    print(f"{'.' * 20} "+ str_gas.rjust(max_len))
    print(f"{'~' * partion_liquid +' '*(20-partion_liquid)} "+str_liquid.rjust(max_len))
elif layer_out_gas < layer_out_liquid:
    partion_gas = round(20*Fraction(amount_gas,amount_liquid))
    #print(20*Fraction(amount_gas,amount_liquid))
    str_gas = f"{amount_gas}/{amount_liquid + amount_gas}"
    str_liquid = f"{amount_liquid}/{amount_liquid + amount_gas}"
    max_len = max(len(str_gas), len(str_liquid))
    print(f"{'.' * partion_gas + ' ' * (20 - partion_gas)} " + str_gas.rjust(max_len))
    print(f"{'~' * 20} "+str_liquid.rjust(max_len))
else:
    str_gas=f"{amount_gas}/{amount_liquid + amount_gas}"
    str_liquid=f"{amount_gas}/{amount_liquid + amount_gas}"
    max_len = max(len(str_gas), len(str_liquid))
    print(f"{'.' * 20} "+str_gas.rjust(max_len))
    print(f"{'.' * 20} "+str_liquid.rjust(max_len))




#print(bottle)
#print(f"layer_gas = {layer_gas}, layer_liquid = {layer_liquid}, amount_gas = {amount_gas}, amount_liquid = {amount_liquid}")
#print(inp)
