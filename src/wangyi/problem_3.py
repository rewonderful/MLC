#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import math
alpha,lamb,epoch,N,M,L =list(map(eval,"0.1 10 100 5 10 10".strip().split(" "))) #list(map(eval,input().strip().split(" ")))


dummy = ["0.105 0.956 0.876 0.133 0.249 0",
"0.195 0.672 0.193 0.016 0.009 0",
"0.059 0.282 0.709 0.139 0.478 1",
"0.303 0.39 0.95 0.912 0.522 1",
"0.59 0.57 0.141 0.959 0.036 1",
"0.231 0.355 0.305 0.508 0.625 1",
"0.896 0.415 0.771 0.197 0.826 0",
"0.051 0.537 0.442 0.46 0.628 0",
"0.737 0.583 0.09 0.337 0.774 1",
"0.062 0.217 0.553 0.868 0.87 0",
"0.13 0.972 0.845 0.737 0.492",
"0.016 0.009 0.432 0.41 0.092",
"0.257 0.327 0.451 0.18 0.62",
"0.774 0.143 0.879 0.123 0.222",
"0.885 0.114 0.352 0.484 0.367",
"0.439 0.227 0.675 0.654 0.323",
"0.778 0.191 0.633 0.628 0.929",
"0.958 0.231 0.07 0.739 0.34",
"0.015 0.115 0.154 0.75 0.649",
"0.283 0.853 0.752 0.915 0.937",]




train_X,train_Y = [],[]
for i in range(M):
    tmp = dummy[i].strip()
    train_Y.append(int(tmp[-1]))
    train_X.append(list(map(eval, tmp[:-1].strip().split(" "))))

test_X = []
for j in range(M,M+L):
    test_X.append(list(map(eval,dummy[j].strip().split(" "))))

theta = [1] * N

def sigmoid(x):
    return 1/(1+math.exp(x))
def calculation_z(theta,x):
    z = 0
    for i in range(len(theta)):
        z += theta[i] * x[i]
    return z
def forward(theta,X):
    yhat = []
    for x in X:
        z = calculation_z(theta,x)
        yhat.append(sigmoid(z))
    return yhat
def backforward(yhat,ytrue,train_X,lamb,m,):
    delta = [0] * len(theta)
    for i in range(len(yhat)):
        label = ytrue[i]
        for j in range(len(theta)):
            delta[j] += ((label-yhat[i])*train_X[i][j] + lamb * theta[j]/m)/m
    return delta

def iteration(train_X,train_y):

    yhat = forward(theta,train_X)
    delta = backforward(yhat,train_y,train_X,lamb,M)
    for i in range(len(theta)):
        theta[i] -= alpha * delta[i]

def train(train_X,train_Y,epoch):
    for e in range(epoch):
        iteration(train_X,train_Y)

def test(test_X):
    yhat = forward(theta,test_X)
    return yhat


train(train_X,train_Y,epoch)
yhat = test(test_X)
for yy in yhat:
    if yy > 0.5:
        print(1)
    else:
        print(0)
