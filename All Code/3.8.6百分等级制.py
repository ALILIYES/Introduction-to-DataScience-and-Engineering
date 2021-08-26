def gradelevel():
    num = int(input("输入考试成绩"))
    if num < 60:print("不及格")
    elif num >= 60 and num <= 74:print("合格")
    elif num >= 75 and num <= 89:print("良好")
    else:print("优秀")
    gradelevel()

if __name__ == "__main__":
    gradelevel()