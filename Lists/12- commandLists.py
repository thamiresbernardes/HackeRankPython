if __name__ == '__main__':
    N = input(int('Enter with numbers: '))
    l = []
    while i > N:
        i += 1
        l.append[i]
    print(l)
'''
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l
'''