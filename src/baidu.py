# ans = 0
# s = input().strip('')
# s_len = len(s)
# next = [-1 for _ in range(s_len+1)]
# i,j = 0, -1
# while i < s_len:
#     if j == -1 or s[i] ==s[j]:
#         j += 1
#         i += 1
#         next[i] = j
#     else:
#         j = next[j]
#
# ans = s_len-next[s_len]
# print(ans) if s_len % ans==0 else print(s_len)


s = 'comeonmandontconconnect'
pattern = 'on'

#iters = int(input().strip(' '))
for l,r in [(1,5),(1,6),(1,23),(11,16),(11,23)]:
    #l,r = input().strip(' ').split(' ')
    print(len(re.findall(pattern,s[l-1:r])))
