import os
import numpy
from sklearn.preprocessing import MinMaxScaler

"""
Introduction:
Set configuration
"""
def Config():
    file = open("Configuration.txt","w")
    configuration = input("please input Set of active variables:")
    file.write(configuration + '\n')
    configuration = input("please input Set of passive variables:")
    file.write(configuration + '\n')
    configuration = input("please input Epsilon:")
    file.write(configuration + '\n')
    configuration = input("please input NumDeviecs:")
    file.write(configuration + '\n')
    configuration = input("please input MinCells:")
    file.write(configuration + '\n')
    configuration = input("please input MinForce:")
    file.write(configuration)
    file.close()
    
"""
Introduction:
Open file and read data
------------------------------
Data:
attribute:all data attribaute,type is "apple cat dog"
data:all data,type is [[0,1],[0,2]]
"""
def FileOpen():
    filename = input("please input your file name:")
    file = open(os.path.abspath(os.getcwd())+"\Data\\"+filename,'r')
    attribute = file.readline()
    data = file.readlines()
    file.close()
    return [attribute,data]

"""
Introduction:
the column number of what passive value persent by data column
------------------------------
Data:
seg:the column number of what passive value persent by data column,type is [0,1] 
"""
def ClassNumber(attribute):
    attribute = attribute.split()
    file = open("Configuration.txt",'r')
    check = file.readline()
    check = file.readline()
    file.close()
    check = check.split()
    check_size = numpy.size(check)
    seg = [None]*check_size
    k = 0
    n = 0
    for i in attribute:
        for j in check:
            if i ==j:
                seg[k] = n
                k = k+1
        n = n+1
    return seg

"""
Introduction:
describe every segment how to segment dat
------------------------------
Data:
segfilter:describe every segment how to segment data,type is ["0 1","2 3"]
"""                      
def InputFilter():
    file = open("Configuration.txt",'r')
    passvalue = file.readline()
    passvalue = file.readline()
    file.close()
    passvalue = passvalue.split()
    segfilter = []
    for i in passvalue:
        infilter = input("please input "+i+" segment description:")
        segfilter.append(infilter)
    return segfilter
        
"""
Introduction:
Determine whether the data belongs to this group
------------------------------
Data:
checkseg:Determine whether the data belongs to this group,type is True
"""
def CheckSegment(record,seg,segfilter):
    k = 0
    checkseg = True
    record = record.split(',')
    for i in seg:
        checkfilter = segfilter[k].split()
        k = k+1
        check = False
        for j in checkfilter:
            if (record[i] == j):
                check = True
                break
        if(check == False):
            checkseg = False
            break
    return checkseg

"""
Introduction:
Copy active variables
------------------------------
Data:
actvalue:Copy active variables,type is [0,1]
"""
def CopyActvalue(record,attribute):
    file = open("Configuration.txt",'r')
    actattribute = file.readline()
    file.close()
    actattribute = actattribute.split()
    attribute = attribute.split()
    record = record.split(',')
    actvalue=[]
    k = 0
    for i in attribute:
        for j in actattribute:
            if(i == j):
                actvalue.append(float(record[k]))
                break
        k = k+1
    return actvalue

def CopyLabel(record):
    file = open("Configuration.txt",'r')
    actattribute = file.readline()
    pasattribute = file.readline()
    file.close()
    actattribute = actattribute.split()
    pasattribute = pasattribute.split()
    allattrsize = numpy.size(actattribute) + numpy.size(pasattribute)
    record = record.split(',')
    label = record[allattrsize]
    return label
    
"""
Introduction:
Calculate all integrated data
------------------------------
Data:
attribute:all data attribaute,type is "apple cat dog"
data:all data,type is [[0,1],[0,2]]
seg:the column number of what passive value persent by data column,type is [0,1] 
segfilter:describe every segment how to segment data,type is ["0 1","2 3"]
all_actvalue:all data active value,type is [[0,1],[0,2]]
checkseg:Determine whether the data belongs to this group,type is True
actvalue:Copy active variables,type is [0,1]
"""
def Sum():
    [attribute,data] = FileOpen()
    seg = ClassNumber(attribute)
    segfilter = InputFilter()
    all_actvalue = []
    all_label = []
    for record in data:
        checkseg = CheckSegment(record,seg,segfilter)
        if (checkseg == True):
            actvalue = CopyActvalue(record,attribute)
            all_actvalue.append(actvalue)
            label = CopyLabel(record)
            all_label.append(label)
    return [all_actvalue,all_label]
    

# ----------------------------------------------------------------------------

def min_max_normalization(data):
    scaler = MinMaxScaler().fit(data)
    scaled = scaler.transform(data)
    return scaled

# # 找出各個attribute的最大值和最小值
# def find_range(data):
#     min_value = []
#     max_value = []
#     activate_variable_number = get_activate_variable_number()
#     for i in range(activate_variable_number):
#         value = min(data, key=lambda item: item[i])
#         min_value.append(value[i])
#         value = max(data, key=lambda item: item[i])
#         max_value.append(value[i])
#     return [min_value, max_value]
# # min_value[0]就是第一個attribute的最小值，max_value[1]就是第二個attribute的最大值，以此類推


def get_activate_variable_number():
    file = open("Configuration.txt",'r')
    str1 = file.readline()
    str2 = str1.split()
    # print (str2)
    z = len(str2)
    file.close()
    return z


def get_epsilon():
    file = open("Configuration.txt",'r')
    active_variable = file.readline()
    pass_variable = file.readline()
    Epsilon = file.readline()
    E = int(Epsilon)
    return E
    

def get_data_size(data):
    data_size, active_variables_size = numpy.shape(data)
    data_size = int(data_size)
    return data_size


def calcCell(E, data, data_size):
    element = 3
    # 宣告epsilon*epsilon格cell，每個cell裡面有3個element (u1, u2, t)
    cell = numpy.zeros((E, E, element))
    
    data_normalization = min_max_normalization(data)

    # 開一個列表來存每筆原始資料屬於哪個cell
    data_cell = numpy.zeros((data_size, get_activate_variable_number()))
    
    # print (data_normalization)
    for i in range(data_size):
        c1 = data_normalization[i][0] // (1/E)
        if(c1 == E):
            c1 = c1 - 1
        c1 = int(c1)
        c2 = data_normalization[i][1] // (1/E)
        if(c2 == E):
            c2 = c2 -1
        c2 = int(c2)
        data_normalization[i][0] =  data_normalization[i][0]
        cell[c1][c2][0] = ( (cell[c1][c2][0]*cell[c1][c2][2] + data_normalization[i][0]) / (cell[c1][c2][2] + 1) )
        cell[c1][c2][1] = ( (cell[c1][c2][1]*cell[c1][c2][2] + data_normalization[i][1]) / (cell[c1][c2][2] + 1) )
        cell[c1][c2][2] += 1 
        #第i筆原始資料存在cell c1,c2
        data_cell[i][0] = c1
        data_cell[i][1] = c2
    return [cell, data_cell]


# 將H的資料寫入txt檔，格式為c1,c2,u1,u2,t
def write_H_data(E, cell):
    path = 'H_data.txt'
    f = open(path, 'w')
    print('c1   c2   u1   u2   t', file=f)
    for i in range(E):
        for j in range(E):
            if(cell[i][j][2] != 0):
                print(i, ',', j, ',', round(cell[i][j][0],5), ',', round(cell[i][j][1],5), ',', int(cell[i][j][2]), file=f)
    f.close()
    

# 原始資料屬於哪個cell，寫入txt檔，格式為x1,x2,c1,c2,label
def write_ori_data(original_data, original_label, data_belong_cell, number_of_data):
    path = 'original_data.txt'
    f = open(path, 'w')
    print('x1   x2   c1   c2   label', file=f)
    for i in range(number_of_data):
        print(original_data[i][0], ',', original_data[i][1], ',', data_belong_cell[i][0], ',', data_belong_cell[i][1], ',', original_label[i], end= '', file=f)
    f.close()
