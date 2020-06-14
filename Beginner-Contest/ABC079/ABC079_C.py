a, b, c, d = list(input())
sign = "+-"
for i in range(2):  # 1つ目の記号
    for j in range(2):  # 2つ目の記号
        for k in range(2):  # 3つ目の記号
            if eval(a+sign[i]+b+sign[j]+c+sign[k]+d) == 7:
                print(str(a+sign[i]+b+sign[j]+c+sign[k]+d)+"=7")
