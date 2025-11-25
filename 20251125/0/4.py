def asm_interpreter(s):
    words = s.split()
    match words:
        case ["mov", r1, r2]:
            print(f"moving {r2} to {r1}")
        case [cmd, *reglist] if cmd in ["push", "pop"]:
            regs = ' '.join(reglist)
            print(f"{cmd}ing {regs}")
        case [cmd, r1]:
            print(f"making {cmd} with {r1}")
        case _:
            print("Parse error")

asm_interpreter("mov ax bx")
asm_interpreter("push esr1 esr2 esr112")
asm_interpreter("pop esr1")
asm_interpreter("add ax")
asm_interpreter("invalid")