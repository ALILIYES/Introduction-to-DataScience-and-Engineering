def wordcount(data):
    re = {}
    for i in data:
        re[i] = re.get(i,0)+1
    return re
if __name__=="__main__":
    data = ["ab","cd","ab","d","d"]
    print("结果为%s"%wordcount(data))