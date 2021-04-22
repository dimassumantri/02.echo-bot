import mysql.connector
from mysql.connector import Error
from mysql.connector.locales.eng import client_error
import os
import datetime
import pandas as pd
import SQLdict
import numpy as np
import bisect

dirname, filename = os.path.split(os.path.abspath(__file__))

def test_con(ipheidi,userheidi,passwodheidi):
    try:
       mySQLconnection = mysql.connector.connect(host=ipheidi,
                                 database='isat_cm',
                                 user=userheidi,
                                 password=passwodheidi)
       cursor = mySQLconnection .cursor()
       return "ok"
    except Error as e :
        return "SQL Connection fail"
def query_command(SqlScript,feedback,DBname,IP,userheidi,passwordheidy):
    field_names=[]
    try:
       mySQLconnection = mysql.connector.connect(host=IP,
                                 database=DBname,
                                 user=userheidi,
                                 password=passwordheidy)
       sql_select_Query = SqlScript
       cursor = mySQLconnection .cursor()
       cursor.execute(sql_select_Query)
       if feedback != "nofeedback":
           records = cursor.fetchall()
           field_names = [i[0] for i in cursor.description]
       cursor.close()
    except Error as e :
        currentDate = datetime.datetime.today()
        if os.path.exists(dirname +'/loging/SQL.txt'):
            outputfileHistory = open(dirname + "/loging/SQL.txt", "a")
        else:
            outputfileHistory = open("SQL.txt", "w")
        outputfileHistory.write('Error while connecting to MySQL\n' + currentDate.strftime("%Y-%m-%d"))
        outputfileHistory.write('\n'  + SqlScript + '\n' )
        outputfileHistory.close()
        records = "error"
    if feedback != "nofeedback":
        return(records,field_names)
#notification 2G
def count_redflag(row):
    remark = str(row['remark'])
    if 'red flag' in remark:
        return 1
    else:
        return 0
def remark_2g(row):
    threshold = -3
    CSSR = float(row['CSSR'])
    CSSR_compare = float(row['CSSR_compare'])
    consecutive_below_90 = str(row['consecutive_below_90'])
    BH_below80 = str(row['BH_below80'])
    if CSSR_compare == 0 :
        CSSR_compare = float('nan')
    CSSR_MC = float(row['CSSR_MC'])
    if CSSR_MC == 0 :
        CSSR_MC = float('nan')
    Spike_hourly = float(row['Spike_hourly'])
    if consecutive_below_90== "CSSR_below_90" :
        result = "daily_consecutive_below_90|"
    else:
        result = ""
    if BH_below80== "BH_below80" :
        result = result + "BH_below80|"
    else:
        result = result
    if np.isnan(CSSR_compare) == False and np.isnan(CSSR_MC)== False:

        degradasibackdate = ((CSSR-CSSR_compare)/CSSR_compare)*100
        degradasiMC = ((CSSR-CSSR_MC)/CSSR_MC)*100
        if degradasibackdate <= threshold and degradasiMC <= threshold and Spike_hourly == False:
            result = result + "red flag"
    elif np.isnan(CSSR_compare) == False and np.isnan(CSSR_MC)== True:

        degradasibackdate = ((CSSR-CSSR_compare)/CSSR_compare)*100
        if degradasibackdate <= threshold and Spike_hourly == False:
            result = result + "red flag"
    elif np.isnan(CSSR_compare) == True and np.isnan(CSSR_MC)== False:

        degradasiMC = ((CSSR-CSSR_MC)/CSSR_MC)*100
        if  degradasiMC <= threshold and Spike_hourly == False:
            result = result + "red flag"

    return result
def consecutive_below_90(row):
    remark = str(row['remark'])
    if 'consecutive_below_90' in remark:
        return 1
    else:
        return 0
def BH_below80(row):
    remark = str(row['remark'])
    if 'BH_below80' in remark:
        return 1
    else:
        return 0
def idpivot(row):
    #name = str(row['name_Sufix'])
    region = str(row['REGION'])
    return region
def alarm_mapto_resume(row,dfalarm):
    OBJ = str(row['OBJ'])
    temp=OBJ.split(":")
    filtersite= dfalarm.loc[dfalarm['concatBSC_BCF'] == str(temp[0]) + "_" + str(temp[1])]
    alarm_severity_1= filtersite.loc[filtersite['SEVERITY'] == 1]
    lenalarm_severity_1 = len(alarm_severity_1)
    alarm_severity_2= filtersite.loc[filtersite['SEVERITY'] == 2]
    lenalarm_severity_2 = len(alarm_severity_2)
    alarm_severity_3= filtersite.loc[filtersite['SEVERITY'] == 3]
    lenalarm_severity_3 = len(alarm_severity_3)
    alarm_severity_4= filtersite.loc[filtersite['SEVERITY'] == 4]
    lenalarm_severity_4 = len(alarm_severity_4)

    return lenalarm_severity_1,lenalarm_severity_2,lenalarm_severity_3,lenalarm_severity_4
def getbscbcf(row):
    dn = str(row['DN'])
    temp = dn.split("/")
    bsc = temp[1].split("-")[1]
    bcf = temp[2].split("-")[1]
    return bsc,bcf
def CSSRMC(row,dfmc):
    siteid= str(row['site_id'])
    MCcell = str(row['MICRO_CLUSTER'])
    filtermc = dfmc.loc[dfmc['MICRO_CLUSTER'] == MCcell]
    filterexcludesite = filtermc.loc[filtermc['site_id'] != siteid]
    if len(filterexcludesite) == 0 :
        cssrnum =0
        cssrdenum = 0
    else:
        MICRO_CLUSTER_CSSR = filterexcludesite.groupby(['MICRO_CLUSTER'],sort=False).agg({'MICRO_CLUSTER':lambda x: x.iloc[-1],'CSSR_NUM':sum,'CSSR_DEN':sum	})
        MICRO_CLUSTER_CSSR.set_index('MICRO_CLUSTER',inplace = True)
        cssrnum = MICRO_CLUSTER_CSSR.loc[MCcell, 'CSSR_NUM']
        cssrdenum= MICRO_CLUSTER_CSSR.loc[MCcell, 'CSSR_DEN']
    return cssrnum,cssrdenum
def spikedetection(row,colomname):
    threshold = -3
    CSSRbackdate = float(row['CSSR_compare'])
    if CSSRbackdate == 0 :
        CSSRbackdate = float('nan')
    CSSRMC = float(row['CSSR_MC'])
    if CSSRMC == 0 :
        CSSRMC = float('nan')
    countofhour = len(colomname)
    defaultresult = True
    jumlahcssrmemenuhisarat = 0
    xx=""
    for cssrH in colomname:

        CSSR_H = float(row[cssrH])
        if CSSR_H != "" :
            if np.isnan(CSSRbackdate) == False and np.isnan(CSSRMC)== False:
                degradasibackdate = ((CSSR_H-CSSRbackdate)/CSSRbackdate)*100
                degradasiMC = ((CSSR_H-CSSRMC)/CSSRMC)*100
                if degradasibackdate < threshold and degradasiMC < threshold:
                    jumlahcssrmemenuhisarat = jumlahcssrmemenuhisarat +1
            elif np.isnan(CSSRbackdate) == False and np.isnan(CSSRMC)== True:
                degradasibackdate = ((CSSR_H-CSSRbackdate)/CSSRbackdate)*100
                if degradasibackdate < threshold :
                    jumlahcssrmemenuhisarat = jumlahcssrmemenuhisarat +1
            elif np.isnan(CSSRbackdate) == True and np.isnan(CSSRMC)== False:
                degradasiMC = ((CSSR_H-CSSRMC)/CSSRMC)*100
                if  degradasiMC < threshold:
                    jumlahcssrmemenuhisarat = jumlahcssrmemenuhisarat +1
    percenspike =np.ceil((jumlahcssrmemenuhisarat / countofhour)*100)
    if percenspike >= 50 :
        defaultresult = False
    return defaultresult
#notification 3G
def consecutive_below_90CS(row):
    remark = str(row['remark'])
    if 'consecutive_below_95_CS' in remark:
        return 1
    else:
        return 0
def BH_below80CS(row):
    remark = str(row['remark'])
    if 'BH_CSbelow90' in remark:
        return 1
    else:
        return 0
def consecutive_below_90PS(row):
    remark = str(row['remark'])
    if 'consecutive_below_95_PS' in remark:
        return 1
    else:
        return 0
def BH_below80PS(row):
    remark = str(row['remark'])
    if 'BH_PSbelow90' in remark:
        return 1
    else:
        return 0
def getrncwbts(row):
    dn = str(row['DN'])
    temp = dn.split("/")
    rnc = temp[1].split("-")[1]
    wbts = temp[2].split("-")[1]
    return rnc,wbts
def remark_3g(row,type):
    threshold = -3
    result = ""
    if type == "CS":

        consecutive_below_90 = str(row['consecutive_below_95_CS'])
        BH_below80 = str(row['BH_CSbelow90'])

        if consecutive_below_90== "consecutive_below_95_CS" :
            result = "consecutive_below_95_CS|"
        if BH_below80== "BH_CSbelow90" :
            result = result + "BH_CSbelow90|"
        else:
            result = result

    else:

        consecutive_below_90 = str(row['consecutive_below_95_PS'])
        BH_below80 = str(row['BH_PSbelow90'])

        if consecutive_below_90== "consecutive_below_95_PS" :
            result = "consecutive_below_95_PS|"
        if BH_below80== "BH_PSbelow90" :
            result = result + "BH_PSbelow90|"
        else:
            result = result

    return result

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return("ok")
    except ValueError:
        return("nok")#validate date text
def sectorIDsub(row):
    aldid = row['ald']
    sector = row['sectorID']
    resumeRemark = str(sector) + ' ald_' + str(aldid)
    return resumeRemark;

def getlastmeas(tech,ipheidi,userheidi,passwodjeidi):

    kemaren = datetime.datetime.today()- datetime.timedelta(hours =24)
    today = datetime.datetime.today()- datetime.timedelta(hours =4)
    if tech == "4G":
        sqlscript_query = "SELECT  xdate,xhour FROM isat_report.susy_4gperfcell_2 WHERE xdate >= '" + kemaren.strftime("%Y-%m-%d") + "' ORDER BY xdate DESC LIMIT 1"
    elif tech == "3G":
        sqlscript_query = "SELECT  xdate,xhour FROM isat_report.susy_3gperfcell WHERE xdate >= '" + kemaren.strftime("%Y-%m-%d") + "' ORDER BY xdate DESC LIMIT 1"
    elif tech == "2G":
        sqlscript_query = "SELECT  xdate,xhour FROM isat_report.susy_2gperfcell WHERE xdate >= '" + kemaren.strftime("%Y-%m-%d") + "' ORDER BY xdate DESC LIMIT 1"
    queryresult,fieldnames = query_command(sqlscript_query,"feedback","isat_report",ipheidi,userheidi,passwodjeidi)
    df = pd.DataFrame(queryresult,columns=fieldnames)
    datevalue = df.loc[0, 'xdate']#.astype(str)
    hourvalue = df.loc[0, 'xhour']#.astype(str)
    result = "last measurement date: " + str(datevalue) + " hour : " + str(hourvalue)



    return (result)

def get_interval(x,rangeList):
    beg = bisect.bisect_right(rangeList,x)
    if rangeList[beg-1] == x: #Handle Perfect Hit Edge Case
        return [x]
    elif not beg: #Left Edge Case
        return [rangeList[0]]
    elif beg == len(rangeList): #Right Edge Case
        return [rangeList[-1]]
    else:
        return [rangeList[beg]]
