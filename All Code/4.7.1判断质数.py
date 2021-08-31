def isprime(num) -> None:
    if num==1 or num==2:return True
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):return False
    return True
if __name__ == "__main__":
    print(isprime(7))