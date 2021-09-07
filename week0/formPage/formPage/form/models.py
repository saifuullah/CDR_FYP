from django.db import models

# Create your models here.


class CDRdata(models.Model):
    MSISDN = models.IntegerField(max_length=100)
    CALL_ORIG_NUM = models.IntegerField(max_length=100)
    CALL_DIALED_NUM = models.IntegerField(max_length=100)
    IMSI = models.IntegerField(max_length=100)
    IMEI = models.IntegerField(max_length=100) 
    CALL_START_DT_TM = models.DateTimeField(max_length=100)
    CALL_END_DT_TM = models.DateTimeField(max_length=100)
    INBOUND_OUTBOUND_IND = models.CharField(max_length=100)
    Call_Network_Volume = models.CharField(max_length=100)
    Cell_Lac_Id = models.CharField(max_length=100)
    Cell_Site_Id = models.CharField(max_length=100)
    LAT = models.CharField(max_length=100)
    LONGITUDE = models.CharField(max_length=100)
    CALL_TYPE = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)



class pdata:
    def __init__(self, row):
        self.MSISDN = row[0]
        self.CALL_ORIG_NUM =row[1]
        self.CALL_DIALED_NUM = row[2]
        self.IMSI = row[3]
        self.IMEI =row[4]
        self.CALL_START_DT_TM = row[5]
        self.CALL_END_DT_TM = row[6]
        self.INBOUND_OUTBOUND_IND = row[7]
        self.Call_Network_Volume = row[8]
        self.Cell_Lac_Id = row[9]
        self.Cell_Site_Id = row[10]
        self.LAT = row[11]
        self.LONGITUDE = row[12]
        self.CALL_TYPE = row[13]
        self.Location = row[14]

    


