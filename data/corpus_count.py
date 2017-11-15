# -*-coding:utf-8-*-
# Author: alphadl
# corpus_count.py 2017/9/13 10:36
'''
Average length of student answer
'''
# with open('/Users/alphadl/PycharmProjects/bi-lstm_yuejuan/data/answer/23.3.txt','r') as r_op:
#     lines_raw=r_op.readlines()
#     lines=[line.strip().split('\t')[0] for line in lines_raw]
#     len_list=[]
#     for i,term in enumerate(lines):
#         print term
#         len_list.append(len(term.decode('utf-8')))
#     print float(sum(len_list))/len(len_list)
'''
Average length of reference answer
'''
with open('/Users/alphadl/PycharmProjects/bi-lstm_yuejuan/data/question/23.3.txt','r') as r_op:
    lines_raw=r_op.readlines()
    lines=[line.strip().split('\t')[0] for line in lines_raw]
    len_list=[]
    for i,term in enumerate(lines):
        print term
        len_list.append(len(term.decode('utf-8')))
    print float(sum(len_list))/len(len_list)