BMI=0
height = int (input("請輸入身高(cm):"))
weight = int (input("請輸入體重(kg):"))

BMI = (weight) / ((height/100)*(height/100))
print("BMI = %f\n" %(BMI))

if BMI < 18.5:
    print("多吃一點！")
if BMI >= 180.5 and BMI < 24:
    print("保持得很好呦！")
if BMI >= 24:
    print("該減肥囉！")