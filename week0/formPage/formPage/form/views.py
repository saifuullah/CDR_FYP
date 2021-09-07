from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from pathlib import Path
import csv
import mysql.connector
from mysql.connector import Error
from .models import pdata


def getData():
        connection = mysql.connector.connect(host='localhost',
                                            database='cdr',
                                            user='root',
                                            password='')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * from phoneData")
            myresult = cursor.fetchall()
            return myresult


def show(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['files']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        saveFileInDB(uploaded_file.name)
        data = getData()
        lst = []
        for row in data:
            p = pdata(row)
            lst.append(p)
            context = {
                'data' : lst
            }
            print(lst[0])
        return render(request, 'table.html', context)
    return render(request, 'index.html')


def saveFileInDB(name):
    x = 0
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = os.path.join(BASE_DIR, 'media')
    with open('media/'+name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if x == 0:
                x+=1
            else:
                insert(row)
                



def insert(row):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='cdr',
                                            user='root',
                                            password='')
        if connection.is_connected():
            cursor = connection.cursor()
            sql = "INSERT INTO phoneData (MSISDN,CALL_ORIG_NUM,CALL_DIALED_NUM,IMSI,IMEI,CALL_START_DT_TM,CALL_END_DT_TM,INBOUND_OUTBOUND_IND,Call_Network_Volume,Cell_Lac_Id,Cell_Site_Id,LAT,LONGITUDE,CALL_TYPE,Location) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            val = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
            #print(row)

            cursor.execute(sql,val)
            connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
                    
