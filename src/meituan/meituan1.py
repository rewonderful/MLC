def change_deep(n, List):
    if len(List) == 1:
        return List
    output, temp, last = [], [], []
    for each in List:
        if n >= len(each):
            last.append(each)
        else:
            temp.append(each)
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[j][n] < temp[i][n]:
                temp[i], temp[j] = temp[j], temp[i]
    i = 0
    while i < len(temp):
        j = i + 1
        while j < len(temp):
            if temp[j][n] != temp[i][n]:
                break
            j += 1
        right = change_deep(n + 1, temp[i: j])
        output += right
        i = j
    return output + last


def change(s):
    s_list = s.split(',')
    ans = change_deep(0, s_list)
    ans = reversed(ans)
    output = ','.join(ans)
    return output


if __name__ == '__main__':
    string = input()
    print(change(string))