import openpyxl
import Xtudylogin

propertydict = {}
testcase_list = []
with open(r'C:\Users\Bablu\PycharmProjects\seleniumpychrm\property.txt') as propertyfile:
    for line in propertyfile:
        line = line.strip()
        x = line.split('==')
        a = x[0]
        b = x[1]
        propertydict[a] = b

propertyfile.close()






test_case_path = r"D:\xstudy\Test_Cases_Xtudy.xlsx"
test_data_path=r"D:\xstudy\Test_Data.xlsx"

workbook = openpyxl.load_workbook(test_case_path)
test_data_workbook=openpyxl.load_workbook(test_data_path)

sheet = workbook.active

rows = sheet.max_row
cols = sheet.max_column


for row in sheet.iter_rows(min_row=2, max_col=cols, max_row=rows):
    for cell in row:
        testcase_list.append(cell.value)

    if testcase_list[2] == 'Y' and testcase_list[3] == 'LOGIN':
        print testcase_list
        print Xtudylogin.applogin(propertydict['APPURL'], propertydict['LOGINID'], propertydict['PASSWORD'],propertydict['XUSERINPUT'],
                                    propertydict['XUSERPASS'], propertydict['XLOGINBUTT'])

        del testcase_list[:]
    elif testcase_list[2] == 'Y' and testcase_list[3] == 'LOGOUT':
        print testcase_list
        Xtudylogin.logout()
        del testcase_list[:]
    elif testcase_list[2] == 'Y' and testcase_list[3] == 'ADD_STUDENT':
        test_data_sheet = test_data_workbook('ADD_STUDENT')
        for row in sheet.iter_rows(min_row=2, max_col=cols, max_row=rows):
            for cell in row:
                print (cell)

        print testcase_list
    else:
        print testcase_list
        print("work on it")
        del testcase_list[:]
