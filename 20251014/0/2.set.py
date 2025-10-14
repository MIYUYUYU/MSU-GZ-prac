from string import ascii_letters
wov = set("aouie")
con = set(ascii_letters) - wov
se = set(input())
print(len(se & wov), len(se & con))