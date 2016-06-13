#! /usr/bin/env python
# encoding: utf-8

import time

X = 10000
total = 0

st = time.clock()

for i in xrange(X):
    for j in xrange(X):
        total += i * j

#[i * j for i in xrange(X) for j in xrange(X)]

et = time.clock()

print et - st
print total