13.
# def main():
#     num_z = 0
#     num_f = 0
#     sum = 0
#     data = 1
#     while data != 0:
#         data = int(input('请输入数字：'))
#         if data > 0:
#             num_z += 1
#         elif data < 0:
#             num_f +=1
#         sum += data
#     print('正数个数为:%d'%num_z)
#     print('负数个数为:%d'%num_f)
#     aver = sum / (num_z + num_f)
#     print('平均值为：%2f'%aver)
# main()


# 14.
# def main():
#     money = [1000]
#     for i in range(10):
#         x = money[i] * 1.05
#         money.append(x)
#     print('十年后的学费：%.2f'%money[10])
#     print('现在及十年后的学费：%.2f'%sum(money))   
# main() 


# 15.
# def main():
#     count = 0
#     for i in range(100,1000):
#         if i % 5 == 0 and i % 6 == 0:
#             print(i,end = ' ')
#             count += 1
#             if count % 10 ==0:
#                 print("\n")
#         else:
#             continue           
# main()


# 16.
# def main():
#     n2 = 0
#     n3 = 0
#     while n2 ** 2 < 12000:
#         n2 += 1
#     #最小的n满足n^2 > 12000的数字
#     print(n2)#110
#     while n3 ** 3 < 12000:
#         n3 += 1
#     #最小的n满足n^3 < 12000的数字
#     print(n3-1)#22
# main()


# 17.
# def main():
#     sum = 0
#     for i in range(1,50001):
#         sum += 1/i
#     print(sum)
# main()


# 18.
# def main():
#     sum = 0
#     for i in range(1,98,2):
#         sum += i/(i + 2)
#     print(sum)
# main()


# 19.
# def main():
#     sum = 0
#     for i in range(1,100000):
#         sum += 4 * (-1) ** (i + 1) / (2 * i - 1)
#     print(sum)
# main()


# 20.
# def main():
#     for i in range(1,10000):
#         sum = 0
#         for j in range(1,i):
#             if i % j ==0:
#                 sum += j
#         if i ==sum:
#             print(i)
# main()


# 21.
# def main():
#     count = 0
#     for i in range(1,8,2):
#         for j in range(2,8):
#             if i != j:
#                 print(i,j)
#                 count += 1
#     print(count)
# main()


# 22.
# number = []
# he = 0
# for i in range(10):
#     data = float(input('请输入10个数字：'))
#     number.append(data)
# average = sum(number) / len(number)
# for x in number:
#     cha = (average - x) ** 2
#     he += cha
# st = (he / (len(number)-1)) ** 0.5
# print('The mean is %f'%average)
# print('The Standard deviation is %f'%st)


#######################################################
# 1.
# def getPentagonalNumber(n):
# 	    sum = 0
# 	    for i in range(1,n+1):
# 	        num = i*(3*i-1)/2
# 	        print(int(num),end=' ')
# 	        sum += 1
# 	        if sum % 10 == 0:
# 	            print("\n")
# getPentagonalNumber(100)


# 2.
# def sumDigits(n):
# 	    gewei = int(n) % 10
# 	    c = 0
# 	    for i in range(len(str(n))):
# 	        baiwei = int(n) // (10 * (10**i)) % 10
# 	        c += baiwei
# 	    sum = c+gewei
# 	    print("这个整数所有数字的和%d"%sum)
# sumDigits(234)


# 3.
# def displaySortedNumbers(num1,num2,num3):
# 	    list = [num1,num2,num3]
# 	    num = sorted(list)
# 	    print("the sorted numbers are {}".format(num))
# if __name__ == "__main__":
# 	    a,b,c = map(int,input("enter three number:").split(","))
# 	    displaySortedNumbers(a,b,c)


# 4.
# from prettytable import PrettyTable
# list = []
# def futureInvestmentValue(inAmount,rate,years):
# 	    for i in range(1,years + 1):
# 	        futureInvestment = inAmount + ((1 +rate) ** (12 * i))
# 	        list.append([i,futureInvestment])
# 	    table = PrettyTable(['year','Future Value'])
# 	    for row in list:
# 	        table.add_row(row)
# 	        print(table)
# if __name__ == "__main__":
# 	    inAmount = int(input("请输入投资额："))
# 	    rate = float(input("请输入百分比格式的年利率：")) / 12
# 	    futureInvestmentValue(inAmount,rate,years = 30)


# 5.
# def printChars():
# 	    for i in range(73,91):
# 	        print(chr(i),end=" ")
# 	        if i%9==0:
# 	            print("\n")
# printChars()


# 6.
# def numberOfDaysInAYear(year):
# 	    for count in range(year,year+11):
# 	        if count % 4 == 0 and count % 100 != 0 or count % 400 == 0:
# 	            print("{}年有366天".format(count))
# 	        else:
# 	            print("{}年有365天".format(count))
# numberOfDaysInAYear(2010)


# 7.
# def distance(x1,y1,x2,y2):
# 	    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
# 	    print ("这两点间的距离是：%f"%distance)
# distance(1,4,4,2)


# 8.
# from prettytable import PrettyTable
# def mei(p):
# 	    c = []
# 	    b = []
# 	    for p in range(2,32):
# 	        if p>1:
# 	            for i in range(2,p):
# 	                if (p % i) == 0:
# 	                #print(p,"不是质数")
# 	                #print(i,"乘于"，p//i,"是"，p)
# 	                    break
# 	                else:
# 	                    #print(p,"是质数")
# 	                    d = 2**(p-1)
# 	                    c.append([p,d])
# 	    for x in c:
# 	        if x not in b:
# 	            b.append(x)
# 	            table = PrettyTable(['p','2**(p-1)'])
# 	    for row in b:
# 	        table.add_row(row)
# 	    print(table)
# mei(5)


# 9.
# import time
# localtime = time.asctime(time.localtime(time.time()))
# print("本地时间为 :", localtime)


# 10.
# import random
# def shaizi():
# 	      a=random.choice([1,2,3,4,5,6])
# 	      b=random.choice([1,2,3,4,5,6])
# 	      if a+b==2 or  a+b==3 or a+b==12:
# 	            print('%d + %d = %d' %(a,b,a+b))
# 	            print('你输了')
# 	      elif a+b==7 or a+b==11:
# 	            print('%d + %d = %d' %(a,b,a+b))
# 	            print('你赢了')
# 	      else:
# 	            print('%d + %d = %d' %(a,b,a+b))
# 	            c=random.choice([1,2,3,4,5,6])
# 	            d=random.choice([1,2,3,4,5,6])
# 	            if c+d==7:
# 	                  print('%d + %d = %d' %(c,d,c+d))
# 	                  print('你输了')
# 	            elif c+d==a+b:
# 	                  print('%d + %d = %d' %(c,d,c+d))
# 	                  print('你赢了')
# shaizi()


