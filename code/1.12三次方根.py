def three_time(l,r):
    while(abs(r-l)>=0.000001):
        mid = (l+r)/2
        if(mid*mid*mid>num):r=mid
        else:l=mid
    return l


if __name__ == "__main__":
    num = float(input())
    print(round(three_time(-10000.0,10000.0),6))
