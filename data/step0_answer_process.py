# -*-coding:utf-8-*-
# Author: alphadl
# step0_answer_process.py 2017/9/10 17:31
'''
Put the answers separately into the answer folder and generate the /answer/*
'''
import re
with open('任务7-试卷2 钱学程.txt','r') as r_op:
    raw_lines=r_op.readlines()
    lines=[line.strip().split('###')[2:] for line in raw_lines]
    #Regular substitution fraction
    for i in range(len(lines)):
        if len(lines[i])>2:
            lines[i][1]=re.findall(r"(\d+)分",lines[i][1])[0]
        else:
            print 'error',' '.join(lines[i])

    #Add the title number to the appropriate file
    for i,term in enumerate(lines):
        print term[0],term[0]=='19.1',term[0]=='19.2',term[0]=='19.3',term[0]=='20.1',term[0]=='20.2',term[0]=='20.3'
        if term[0]=='19.1':
            with open('/Users/alphadl/PycharmProjects/bi-lstm_yuejuan/data/answer/19.1.txt','a') as w_op:
                w_op.write(term[1]+'\t'+term[2]+'\n')
        if term[0]=='19.2':
            with open('/Users/alphadl/PycharmProjects/bi-lstm_yuejuan/data/answer/19.2.txt','a') as w_op:
                w_op.write(term[1]+'\t'+term[2]+'\n')
        if term[0]=='19.3':
            with open('/Users/alphadl/PycharmProjects/bi-lstm_yuejuan/data/answer/19.3.txt','a') as w_op:
                w_op.write(term[1]+'\t'+term[2]+'\n')
        if term[0]=='20.1':
            with open('/Users/alphadl/PycharmProjects/bi-lstm_yuejuan/data/answer/20.1.txt','a') as w_op:
                w_op.write(term[1]+'\t'+term[2]+'\n')
        if term[0]=='20.2':
            with open('/Users/alphadl/PycharmProjects/bi-lstm_yuejuan/data/answer/20.2.txt','a') as w_op:
                w_op.write(term[1]+'\t'+term[2]+'\n')
        if term[0]=='20.3':
            with open('/Users/alphadl/PycharmProjects/bi-lstm_yuejuan/data/answer/20.3.txt','a') as w_op:
                w_op.write(term[1]+'\t'+term[2]+'\n')

    print "all load finished"


