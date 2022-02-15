
import time
from openpyxl import workbook
import pandas as pd

No=int (input("enter no of employess : "))
data={}
for i in range(No):
    name=input("enter employee name : ")
    des=input("\t enter employee designation : ")
    id=int(input("\t enter employee ID : "))
    sal=int(input('\t enter salary : '))
    data[name]={'designation':des,'ID':id,'Salary':sal}
df=pd.DataFrame(data)
print('creating excel filee')
time.sleep(3)
df.to_excel(excel_writer='heeee.xlsx')
print(df)
print('excel file created')