#!/usr/bin/env python
# _*_ coding:utf-8 _*_
transform_dict ={'零':0,
                           '一':1,
                           '二':2,
                           '两':2,
                           '三':3,
                           '四':4,
                           '五':5,
                           '六':6,
                           '七':7,
                           '八':8,
                           '九':9,
                           '十':10,
                           '百':100,
                           '千':1000,
                           '万':10000,
                           '亿':100000000}
# common_used_numerals= dict(zip(common_used_numerals_tmp.values(), common_used_numerals_tmp.keys())) #反转
#print(common_used_numerals)
def chinese2digits(uchars_chinese):
      total = 0
      r = 1              #表示单位：个十百千...
      for i in range(len(uchars_chinese) - 1, -1, -1):
        #print(uchars_chinese[i])
        val = transform_dict.get(uchars_chinese[i])
        if val >= 10 and i == 0:  #应对 十三 十四 十*之类
          if val > r:
            r = val
            total = total + val
          else:
            r = r * val
            #total =total + r * x
        elif val >= 10:
          if val > r:
            r = val
          else:
            r = r * val
        else:
          total = total + r * val
      return total
def chn2numbers(chinese):
    total = 0
    r = 1
    for i in range(len(chinese)-1,-1,-1):
        val = transform_dict[chinese[i]]
        if val >= 10 and i == 0:
            r = val
            total += val
        elif val >= 10:
            if val > r:
                r = val     #换底
            else:
                r = r * val #处理十万，百万，这种，相当于10*10000,....
        else:
            total = total + r * val
    return total
if __name__ == '__main__':
    print (chinese2digits('五百二十') )
    print(chn2numbers('五百二十'))
    print ( "-------------------------" )
    print (  chinese2digits('十八') )
    print(chn2numbers('十八'))
    print ( "-------------------------" )
    print ( chinese2digits('一亿零一千二百八十二'))
    print(chn2numbers('一亿零一千二百八十二'))
    print(chinese2digits('二十三万零三十'))
    print(chn2numbers('二十三万零三十'))
