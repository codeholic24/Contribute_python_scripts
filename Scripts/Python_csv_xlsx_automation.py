'''

I have written this code for one of my YouTube Subscriber asking to automate the process

Developer : Vikas Bhaskar Vooradi
Role      : Associate Level 1 (Software engineer)
Code Type : Automation

Description
------------------

1. Check .csv or .xlsx file arrived or not
2. If .csv file arrived then process to table
   else .xlsx file otherwise end process
3. Create a method or fucntion dynamically to do above process




Implementation 
------------------
1. Mandatory checks 
2. Load file to Oracle table 


Mandatory modules 
------------------
os
time
datetime
pandas
pandasql
openxyl
sqlalchemy
cx_Oracle


File data 
------------------
NAME,SURNAME,CITY,COURSE
Ajay,Bila,Mumbai,MCA
Viraj,Hans,Delhi,MBA
Darshan,Gilat,Pune,MBA


Table structure 
------------------
NAME          VARCHAR2(255) 
SURNAME       VARCHAR2(255) 
CITY          VARCHAR2(255) 
COURSE        VARCHAR2(255) 


'''

# Importing modules
import os
import time
import datetime
import pandas as pd
import cx_Oracle
from sqlalchemy import create_engine

'''

Function 
----------

checkFileExist        - Check the file exsist at path or not 
fetchFileExtension    - Get file extension
checkExtensionMeet    - Check file extension is .csv or .xlsx or not - return True 0 or False 1
fetchFileColumnNames  - Fetching file column names 
fetchTableColumnNames - Fetch column names from table 
compareFileColumnToTabelColumn - Check file column matches table column 

'''

def checkFileExist(pathName,fileName):
    fname =  pathName + '\\' + fileName
    if os.path.isfile(fname):
        return True
    return False

def fetchFileExtension(pathName,fileName):
    fname = pathName + '\\' + fileName
    return os.path.splitext(fname)[1]

def checkExtensionMeet(pathName,fileName):
    fileExt = fetchFileExtension(pathName,fileName)
    if fileExt == '.csv' or fileExt == '.xlsx':
        return True
    return False

def fetchFileColumnNames(pathName,fileName):
    fname = pathName + '\\' + fileName
    fileExt = fetchFileExtension(pathName, fileName)

    if fileExt == '.csv':
        df = pd.read_csv(fname,nrows=2)
        col =  df.columns.to_list()
    elif fileExt == '.xlsx':
        df = pd.read_excel(fname,nrows=2)
        col = df.columns.to_list()
    else:
        pass
    return col

def fetchTableColumnNames(table_name,create_engine_con):
   engine = create_engine(create_engine_con)
   query = """ select * from """ + table_name
   df = pd.read_sql(query, engine)
   df.columns = df.columns.str.upper()
   return df.columns.to_list()

def compareFileColumnToTabelColumn(pathName,fileName,table_name,create_engine_con):
    fileColumn  = sorted(fetchFileColumnNames(pathName,fileName))
    tableColumn = sorted(fetchTableColumnNames(table_name,create_engine_con))

    if fileColumn == tableColumn:
        return True
    return False


# Parameterization
pathName = r'C:\Users\Admin\Desktop\code_for_subscriber'
fileName = 'employee.xlsx'
table_name = 'EMPLOYEE'
username = 'hr'
password = 'hr'
host     = 'localhost'
port     ='1521'
servicename = 'orclpdb'
create_engine_con = 'oracle+cx_oracle://' + username + ":" + password + '@' + host + ":" + port + '/?service_name=' + servicename
engine = create_engine(create_engine_con)


# --------------- Main calling ------------

while True:

        if checkFileExist(pathName,fileName):

            print('Start ...')
            print('File found : ' , fileName )
            print('File extension : ', fetchFileExtension(pathName,fileName))

            if checkExtensionMeet(pathName,fileName):
                print('File extension as meet : ', checkExtensionMeet(pathName,fileName))
                print('File header names      : ', fetchFileColumnNames(pathName,fileName))
                print('Table header names     : ', fetchTableColumnNames(table_name,create_engine_con))

                if compareFileColumnToTabelColumn(pathName,fileName,table_name,create_engine_con):
                    print('File column names match with Table column names')

                    fext = fetchFileExtension(pathName, fileName)
                    if fext == '.csv':
                        df = pd.read_csv(pathName + '\\' + fileName)
                        df.to_sql(table_name.lower(), engine, if_exists='append', index=False)
                        print('Csv data pushed successfully to table')
                    elif fext == '.xlsx':
                        df = pd.read_excel(pathName + '\\' + fileName)
                        df.to_sql(table_name.lower(), engine, if_exists='append', index=False)
                        print('Excel data pushed successfully to table')
                    exit(0)
                else:
                    print('File column names does not match with Table column names')
                    print('Exiting the process!!!')
                    exit(0)
            else:
                print('File extension does not meet : .csv or .xlsx -> ', fileName )
                print('Exiting the process!!!')
                exit(0)
        else:

            print('Not found any file -> Process went into sleep for 1 minute : ',datetime.datetime.now())
            time.sleep(60)
