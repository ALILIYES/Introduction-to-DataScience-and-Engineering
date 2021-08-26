def gcd(num1,num2):
    #更相减损法
    count = 0
    while num1%2==0 and num2%2==0:
        num1,num2 = num1/2,num2/2
        count+=1
    print(num1,num2)
    while num1!=num2:
        num1,num2= max(num1-num2,num2),min(num1-num2,num2)
    for i in range(count):
        num1*=2
    return num1

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print(gcd(max(num1,num2),min(num1,num2)))