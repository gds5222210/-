# a = int(input('输入一个年份'))
# if (a % 4 ==0 and a % 100 !=0) or (a % 400 ==0):
#     print ('%d 是闰年'%a ) 
# else:
#     print ('%d 不是闰年'%a )





# 1
# celsius = float(input('请输入摄氏温度'))
# fahrenheit = 1.8 * celsius + 32
# print('%.1f摄氏度 = %.1f华氏度' % (celsius,fahrenheit))




# 2
# import math 
# π = math.pi 
# radius = float(input('请输入半径：'))
# high = float(input('请输入高：'))
# area = radius * radius * π
# volume = area * high
# print('底面积：%f'%area)
# print('体积：%f'%volume)





# 3
# feet = float(input('请输入英尺数：'))
# maters = feet/0.305
# print ('%.1ffeet is %.4f methers'%(feet,maters))






# 4
# M=float(input('输入水量'))
# f=float(input('输入最终温度'))
# i=float(input('输入开始温度'))
# Q= M*(f-i)*4184
# print('输出你所需要的能量%.1f'%Q)





# 5
# c=float(input('输入差额'))
# n=float(input('输入年利率'))
# l=c*(n/1200)
# print('输出利息为%.6f'%l)






# 6
# v0=float(input('输入v0'))
# v1=float(input('输入v1'))
# t=float(input('输入时间t'))
# a=(v1-v0)/t
# print('输出平均加速度a%.4f'%a)






# 7
# total = 0
# for x in range(0,6):
#     total = (total+100)*(1+0.00417)
# print (total)


# money = float(input('请输入每个月存款数'))
# a = money * ( 1 + 0.00417)
# b = ( a + money) * ( 1 + 0.00417)
# c = ( b + money) * ( 1 + 0.00417)
# d = ( c + money) * ( 1 + 0.00417)
# e = ( d + money) * ( 1 + 0.00417)
# f = ( e + money) * ( 1 + 0.00417)
# print('六个月后账户余额为',f)



# 8
# number = int (input('请输入0到1000的数字：'))
# bai = number//100
# shi = number//10%10
# ge = number%10
# sum_ = bai + shi + ge
# print('the sum of the digits is:%d'%sum_)


# 9 
# import math
# π = math.pi
# tan = math.tan
# sin = math.sin
# r = float(input('输入五边形定点到中心的距离：'))
# s = 2 * r *sin (π /5)
# area = 5 * s * s /(4*tan(π/5))
# print('五边形的面积：%f'%area)


