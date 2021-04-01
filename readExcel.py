#! -*-coding:utf-8 -*-

import xlrd,os,shutil,json,copy

def readxls(kaishi,jiesshu):
    xl=xlrd.open_workbook('./data/啊啊啊.xlsx')  #打开Excel表格
    st = xl.sheet_by_index(2)  #指定表1
    listdata = []  # 定义空列表，用来存放读取出来的每行数据
    for i in range(1,st.nrows):  # 循环1~5(不包含5)，即循环4次
        j = st.row_values(i, kaishi, jiesshu)  # 读取第几列的数据（不含第2列）
        listdata.append(tuple(j))  # 读一行追加一行存入listdata中z
    print(listdata)
    return listdata

def readxls_new():
    xl=xlrd.open_workbook('./data/啊啊啊.xlsx')  #打开Excel表格
    st = xl.sheet_by_index(2)  #指定表1
    listdata = []  # 定义空列表，用来存放读取出来的每行数据
    for i in range(1,st.nrows):  # 循环1~5(不包含5)，即循环4次
        j = st.row_values(i)  # 读取第几列的数据（不含第2列）
        listdata.append(tuple(j))

    return listdata

def creat_report(path):
    if os.path.isdir(path):
        shutil.rmtree(path,True)
        os.system('pytest --alluredir=./myreport')
        os.system('allure serve ./myreport')
    else:
        print("file not find")

if __name__ == '__main__':
    # readxls(0,4)
    readxls_new()
#@pytest.mark.parametrize("user,pwd",[("18221124104",111111),("18200000000",111111)])





