#coding:utf-8
#读取xlsx文件
import xlrd
def read_excel(excelPath,sheetName):
    #要打开的excel文件
    data = xlrd.open_workbook(excelPath)
    #要打开的工作表名字
    table = data.sheet_by_name(sheetName)
    #获取第一行的值作为key值
    keys = table.row_values(0)
    #获取总行数
    rowNum = table.nrows
    #获取总列数
    colNum = table.ncols
    if rowNum <= 1:
        print "总行数小于1"
    else:
        r = []
        j = 1
        for i in range(rowNum-1):
            s ={}
            #从第二行取对应的values的值
            values = table.row_values(j)
            for x in range(colNum):
                s[keys[x]] = values[x]
            r.append(s)
            j+=1
        return r

if __name__ == '__main__':
    filepath = "F:\MfTest\TestUnittest\H5\python_6\\test.xlsx"
    sheetName = "Sheet1"
    print read_excel(filepath,sheetName)