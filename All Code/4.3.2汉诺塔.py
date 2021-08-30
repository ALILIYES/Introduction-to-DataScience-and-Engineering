def hannuota(n,A,B,C):
    if n==1:
        print('Move',n,"from",A,"to",B,"by",C)
    else:
        hannuota(n-1,A,C,B)
        hannuota(1,A,C,B)
        hannuota(n-1,B,C,A)

if __name__ == "__main__":
    n = int(input("输入汉诺塔的层数"))
    hannuota(n,'A','B','C')
