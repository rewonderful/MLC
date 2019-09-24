#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import math
alpha,lamb,epoch,N,M,L =list(map(eval,input().strip().split(" ")))

train_X,train_Y = [],[]
for _ in range(M):
    tmp = input().strip()
    train_Y.append(int(tmp[-1]))
    train_X.append(list(map(eval, tmp[:-1].strip().split(" "))))

test_X = []
for j in range(L):
    test_X.append(list(map(eval,input().strip().split(" "))))

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
