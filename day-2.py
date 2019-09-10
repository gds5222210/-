
# 作业一
# import math
# a = float(input('输入a的值'))
# b = float(input('输入b的值'))
# c = float(input('输入c的值'))        
# if b**2-4*a*c>0:        
#     x1=(-b+math.sqrt(b**2-4*a*c))/2*a        
#     x2=(-b-math.sqrt(b**2-4*a*c))/2*a 
#     print(x1,x2)   
# elif b**2-4*a*c==0:        
#     x1=x2 =(-b+math.sqrt(b**2-4*a*c))/2*a
#     print(x1)    
# else:        
#     print('很抱歉，方程无解')      

# 作业二

# import random
# correctCount = 0
# count = 0
# number1 = random.randint(0,100)
# number2 = random.randint(0,100)
# if number1 < number2:
#     number1,number2 = number2,number1
# answer = eval(input('计算'+str(number1)+"-"+str(number2)+"="))
# if answer == number1 - number2:
#    print('😀恭喜你，小可爱，你赢了!')
#    correctCount += 1
# else:
#    print('😟小智障，你算错了.\n',number1,"-",number2,'is',number1 - number2)

# 作业三：

# num = float(input('输入今天是一周中的哪一天的数字'))
# day = float(input('输入今天之后到未来某天的天数'))
# num_ = (num + day)%7
# if num_ == 0:
#     print('周日')
# elif num_ == 1:
#     print('周一')
# elif num_ == 2:
#     print('周二')
# elif num_ == 3:
#     print('周三')
# elif num_ == 4:
#     print('周四')
# elif num_ == 5:
#     print('周五')
# else:
#     print('周六')

# 作业四
# num1,num2,num3=map(int,input('请输入三个整数：').split())
# min = min(num1,num2,num3)
# max = max(num1,num2,num3)
# print('升序为：%d %d %d' %(min,num1+num2+num3-min-max,max))

# 作业五
# weight1= float(input("Enter weight package 1 :"))
# price1 = float(input("Enter price for package 1 :"))
# weight2= float(input("Enter weight for package 2 :"))
# price2 =  float(input("Enter price for package 2 :"))
# permj1 = float(price1 / weight1)
# permj2 = float(price2 / weight2)
# if permj1 > permj2:
#     print("package 2  has the better price ")
# else:
#     print("package 1  has the better price ")

# 作业六
# month = eval(input('输入月份'))
# year = eval(input('输入年份'))
# leapyear = float(year % 4)
# if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
#     month1 = 31
# elif month == 4 or month ==6 or month ==9 or month ==11:
#     month = 30
# elif leapyear == 0 and month == 2:
#     month = 29
# else:
#     month =28
# print(year,'年',month,'月','有',month1,'天')

# 作业七
# import random
# a = input('猜测硬币正反面：')
# b = random.randint(0,1)
# if b == 1:
#   print('正面')
# else:
#   print('反面')
# if a == b:
#   print('猜对了')
# else:
#   print('猜错了')

# 作业八
# import numpy as np
# res = np.random.choice(['0','1','2'])
# user = input("请输入你的选择['0'，'1'，'2']")
# if res == user:
#     print('平局')
# elif res == '1' and user == '0':
#     print("😟很遗憾，你输了")
# elif res == '0' and user == '2':
#     print("😟你输了")
# elif res == '2 'and user == '1':
#     print("😟你输了")
# else:
#     print('💪恭喜你，再来一局')

#  作业九
# month = 0  
# cent = 0  
# year = 0   
# Q = 0      
# H = 0
# yearFlug = 1
# monthFlug = 1
# dayFlug = 1
# while(yearFlug):
#         yearTemp = int(input("Please Enter Year :(eg:2008):"))
#         if yearTemp > 0 :
#                 yearFlug = 0
#         else:
#                 print("Sorry, Enter Wrong  Year,try again Please")
# cent = yearTemp //100
# year = yearTemp % 100
# while(monthFlug):
#         monthTemp = int(input("Please Enter month:(eg:10):"))
#         if monthTemp > 0 and monthTemp <= 12:
#                 monthFlug = 0
#         else:
#                 print("Sorry, Enter Wrong month ,Try again Please")
# if monthTemp ==1 or monthTemp ==2:
#         year -= 1
#         month = monthTemp + 12
# else:month = monthTemp 
# while(dayFlug):
#         dayTemp = int(input("Please Enter day:(eg:21):"))
#         if dayTemp > 0 and dayTemp <= 28:
#                 dayFlug = 0
#         elif (monthTemp == 1 or monthTemp == 3 or monthTemp == 5 \
#                 or monthTemp == 7 or monthTemp == 8 or monthTemp == 10 \
#                 or monthTemp == 12) \
#         and (dayTemp >28 and dayTemp <= 31):
#                 dayFlug = 0
#         elif (monthTemp == 4 or monthTemp == 6 or monthTemp == 9 or monthTemp == 11)\
#         and (dayTemp >28 and dayTemp <= 30):
#             dayFlug = 0
#         elif (monthTemp == 2) and (yearTemp %4 ==0 and yearTemp%100 != 0) and(dayTemp == 29):
#                 dayFlug = 0
#         else:
#                 print("Sorry ,Enter Wrong day,Try again Please")
# Q = dayTemp
# H = (Q + ((26 * ( month + 1 ) / 10 ) // 1 ) \
#      + (( year / 4 ) // 1) + year \
#      + (( cent / 4 ) // 1) \
#      + ( 5 * cent) )\
#      % 7
# if H == 0:
#         weekDay = "Sat"
#         print('今天是星期六')
# elif H == 1:
#         weekDay = "Sun"
#         print('今天是星期日')
# elif H == 2:
#         weekDay = "Mon"
#         print('今天是星期一')
# elif H == 3:
#         weekDay = "Tue"
#         print('今天是星期二')
# elif H == 4:
#         weekDay = "Wed"
#         print('今天是星期三')
# elif H == 5:
#         weekDay = "Thu"
#         print('今天是星期四')
# elif H == 6:
#         weekDay = "Fri"
#         print('今天是星期五')

# # 作业十：
# import numpy as np

# print('扑克牌的大小分别是：1（Area）、2、3、4、5、6、7、8、9、10、11（Jack）、12（Queen）、13（King）')
# print('扑克牌的花色：1：梅花、2：红桃、3：方块、4：黑桃')

# number = int(input('输入你选择的牌的大小:'))

# number1 = np.random.randint(1,14)
# if number == 1:
#     print('你选择的是:Area')
# number2 = np.random.randint(1,5)
# if number2 ==1:
#     print('梅花')
# elif number2 ==2:
#     print('红桃')
# elif number2 ==3:
#     print('方块')
# else:
#     print('黑桃')
# print('你选择的是:2')
# if number2 ==1:
#     print('梅花')
# elif number2 ==2:
#     print('红桃')
# elif number2 ==3:
#     print('方块')
# else:
#     print('黑桃')
# print('你选择的是:Jack')
# number2 = np.random.randint(1,5)
# if number2 ==1:
#     print('梅花')

# 作业十一：

# num = float(input('判断是否是回文数，请输入一个三位整数:'))
# num1 = num//100
# num2 = num%100
# if num1 == num2:
#     print('是一个回文数')
# else:
#     print('不是回文数')

# 作业十二：
# a = float(input('请输入第一条边长:'))
# b = float(input('请输入第一条边长:'))
# c = float(input('请输入第一条边长:'))
# if a+b>c and a+c>b and b+c>a:
#     l=a+b+c
#     print('周长为%d' %(a+b+c))
# else:
#     print('非法输入，请重新输入')

# 作业十三：
# def main():
#     num_z = 0
#     num_f = 0
#     sum = 0
#     data = 1
#     while data != 0:
#         data = int(input("请输入数字："))
#         if data > 0:
#             num_z += 1
#         elif data < 0:
#             num_f +=1
#         sum += data
#     print("正数个数为:%d"%num_z)
#     print("负数个数为:%d"%num_f)
#     aver = sum / (num_z + num_f)
#     print("平均值为：%2f"%aver)
# main()

# 作业十四：
#money = [1000]
#    for i in range(10):
#         x = money[i] * 1.05
#         money.append(x)
#     print("十年后的学费：%.2f"%money[10])
#     print("现在及十年后的学费：%.2f"%sum(money))   


# 作业十五：
# count = 0
# for i in range(100,1000):
#         if i % 5 == 0 and i % 6 == 0:
#                 print(i,end = ' ')
#                 count += 1
#                 if count % 10 ==0:
#                         print("\n")
#         else:
#                  continue           

# 作业十六：
# n2 = 0
# n3 = 0
# while n2 ** 2 < 12000:
#     n2 += 1
#     print(n2)#110
#     while n3 ** 3 < 12000:
#         n3 += 1
#     print(n3-1)

#  作业十七：
# def main():
#     sum = 0
#     for i in range(1,50001):
#         sum += 1/i
#     print(sum)
# main()

#  作业十八：
# def main():
#     sum = 0
#     for i in range(1,98,2):
#        sum += i / (i + 2)
#     print(sum)
# main()

#  作业十九：
# def main():
#     sum = 0
#     for i in range(1,100000):
#         sum += 4 * (-1) ** (i + 1) / (2 * i - 1)
#     print(sum)
# main()

#  作业二十：
# def main():
#     for i in range(1,10000):
#         sum = 0
#         for j in range(1,i):
#             if i % j ==0:
#                 sum += j
#         if i ==sum:
#             print(i)
# main()

#  作业二十一：

# def main():
#     count = 0
#     for i in range(1,8,2):
#         for j in range(2,8):
#             if i != j:
#                 print(i,j)
#                 count += 1
#     print(count)
# main()

# 作业二十二：
# number = []
# he = 0
# for i in range(10):
#     data = float(input("请输入10个数字："))
#     number.append(data)
# average = sum(number) / len(number)
# for x in number:
#     cha = (average - x) ** 2
#     he += cha
# st = (he / (len(number)-1)) ** 0.5
# print("The mean is %f"%average)
# print("The Standard deviation is %f"%st)











   






 






























