#!/usr/bin/env python
# _*_ coding:utf-8 _*_
position = [0] * 1000
dummy_pos = [0,499,249,749,124,624,374,874,62,562,186,686,311,811,436,536,561,61,60,60]
server_pos = dict()
server_cout = 0
def token_hash(token):
    ha = 0
    for char in token:
        ha += ord(char)
    ha %= 999
    return ha
def get_hit(token):
    ha = token_hash(token)
    hit = False
    pos = ha
    while not hit:
        if position[pos] == 1:
            hit =  True
            break
        else:
            if pos == 999:
                pos = 0
            else:
                pos += 1
    return pos

def kill_server(server_name):
    pos = server_pos[server_name]
    position[pos] = -1
def get_server_pos(server_name):
    return server_pos[server_name]

def add_server(server_list):
    pass



if __name__ == '__main__':

    import sys
    for line in sys.stdin:
        command = input().strip()
        key = int(command[0])
        content = command[1:]
        if key == 1:
            server_name = content
            print(get_server_pos(server_name))
        if key == 2:
            token = content
            print(get_hit(token))
        if key == 3:
            down_server,token = content.split(";")
            down_server = down_server.split(",")
            for server_name in down_server:
                kill_server(server_name)
            print(get_hit(token))
        if key == 4:
            no = int(content[-2:])
            for i in range(1,no + 1):
                index = i - 1
                position[dummy_pos[index]] = 1
                #server_pos[]
            print(dummy_pos[no-1])
        if key == 5:
            last_add_server, token = content.split(";")
            no = int(last_add_server[-2:])
            for i in range(1, no + 1):
                index = i - 1
                position[dummy_pos[index]] = 1
                # server_pos[]
            print(get_hit(token))


