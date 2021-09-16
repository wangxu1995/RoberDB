f1 = open(r"C:\Users\01531377\Desktop\对比门店号脚本\1.txt", "r")
f2 = open(r"C:\Users\01531377\Desktop\对比门店号脚本\2.txt", "r")
txt1 = f1.read()
txt2 = f2.read()
f1.close()
f2.close()
q = txt1.split('|')
p = txt2.split('|')
outfile = open(r"C:\Users\01531377\Desktop\对比门店号脚本\3.txt", "w")

for i in q:
    if i not in txt2:
        outfile.write(i)
        outfile.write("\n")
outfile.write("above content in 1, but not in 2\n")

for j in p:
    if j not in txt1:
        outfile.write(j)
        outfile.write("\n")
outfile.write("above content in 2, but not in 1\n")

print("end")