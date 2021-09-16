f1 = open(r"C:\Users\01531377\Desktop\对比门店号脚本\1.txt", "r")
txt1 = f1.read()
f1.close()
i = str()
i = "|"
n = 0

for i in txt1:
    if i == "|":
        n = n+1

print(n)