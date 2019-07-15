# 1. Max
# # float 更好
# num1 = int(input('The 1st number is:'))
# num2 = int(input('The 2nd number is:'))
#
# print('The bigger one is:', num1 if num1 >= num2 else num2)
# # 2. Score
# # 有同学边界少了?
# x = float(input('Score?'))
# y = 'Error!'
# if 100 >= x >= 90:
#     y = 'A'
# elif 90 > x >= 85:
#     y = 'A-'
# elif 85 > x >= 82:
#     y = 'B+'
# elif 82 > x >= 78:
#     y = 'B'
# elif 78 > x >= 75:
#     y = 'B-'
# elif 75 > x >= 71:
#     y = 'C+'
# elif 71 > x >= 66:
#     y = 'C'
# elif 66 > x >= 62:
#     y = 'C-'
# elif 62 > x >= 60:
#     y = 'D'
# elif 60 > x >= 0:
#     y = 'F'
# print(y)
#
# # 3. 菱形
# # 以此输出的话，print（...,end=' ')，加end=' '避免换行
# n = int(input('请输入n:'))
# for i in range(n+1):
# 	print('  '*(n-i)+'* '*(2*i+1))
#
# for j in range(n):
#     print('  '*(j+1)+'* '*(-2*j+2*n-1))

# 4. 张邱建算经
# 算出鸡翁、鸡母的范围√，算是一种剪枝策略，减少循环数
# 鸡兔同笼中直接算出来，不是剪枝，是直接解方程，没有发挥计算机
# 快速进行大量计算的作用
for x in range(0,21):
    for y in range(0,34):
        z = 100-x-y
        if x*5+y*3+z/3 == 100:
             print('鸡翁数:\t', x, '鸡母数:\t', y, '鸡雏数:\t', z)

# 5. K数
# 本题中用除以10**i 来分割数字更好，这样可以将个位数直接纳入考虑
for num in range(1, 100001):
    for i in range(0, len(str(num))):
        left = num // (10**i)
        right = num % (10**i)
        if (left+right)**2 == num:
            print("%d=(%d+%d)**2" % (num, left, right))

