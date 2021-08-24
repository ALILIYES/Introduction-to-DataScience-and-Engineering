import math
def tentotwo(num):
    if(num==0):return "0"
    small,big = math.modf(num)
    big = int(big) #浮点乱码
    res = ""
    while big!=0:
        res=str(big%2)+res
        big//=2
    if(small!=0):
        res+='.'
        while small>1e-6:
            small*=2
            if(small>=1):
                res = res+'1'
                small-=1
            else:
                res = res+'0'
    return res
if __name__ == "__main__":
    print(tentotwo(12.1))