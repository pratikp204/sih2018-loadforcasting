# from classes import Regression
# import threading



def prr(tem,num,id):
    print tem,num,id

def man_trainer(hper_para):
    ref = {0:'tem',1:'num',2:'id'}
    lis = [None]*3
    default = ['shivam',5,'dragon']
    for i in range(3):
        if ref[i] in hper_para:
            lis[i] = hper_para[ref[i]]
        else:
            lis[i] = default[i]

    prr(lis[0],lis[1],lis[2])






man_trainer({'num':23,'id':43})