import pyodbc, csv




conx = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server}; SERVER=CCISRV2125\A89ADBOPCON01; Database=OPCONCI; TRUSTED_CONNECTION=yes')
cursor = conx.cursor()



queryAG = "SELECT JOBNAME FROM OPCONCI.dbo.JMASTER WHERE SHORTNAME LIKE 'AGI1%%%000AG' OR SHORTNAME LIKE 'AGI%%%010%%';"
cursor.execute(queryAG)
dataAG = cursor.fetchall()
with open (r"C:\Users\rdju\Desktop\nichtbearbeiteteFiles\AG.csv","w") as file:
    for row in dataAG:
        csv.writer(file).writerow(row)




queryLU = "SELECT JOBNAME FROM OPCONCI.dbo.JMASTER WHERE SHORTNAME LIKE 'LUI1%%%000LU' OR SHORTNAME LIKE 'LUI1%%%010%%';"
cursor.execute(queryLU)
dataLU = cursor.fetchall()
with open (r"C:\Users\rdju\Desktop\nichtbearbeiteteFiles\LU.csv","w") as file:
    for row in dataLU:
        csv.writer(file).writerow(row)



   
querySH = " SELECT JOBNAME FROM OPCONCI.dbo.JMASTER WHERE SHORTNAME LIKE 'SHI1%%%000SH' OR SHORTNAME LIKE 'SHI1%%%010%%';"
cursor.execute(querySH)
dataSH = cursor.fetchall()
with open (r"C:\Users\rdju\Desktop\nichtbearbeiteteFiles\SH.csv","w") as file:
    for row in dataSH:
        csv.writer(file).writerow(row)




queryVD = " SELECT JOBNAME FROM OPCONCI.dbo.JMASTER WHERE SHORTNAME LIKE 'VDI1%%%000VD' OR SHORTNAME LIKE 'VDI1%%%010%%';"
cursor.execute(queryVD)
dataVD = cursor.fetchall()
with open (r"C:\Users\rdju\Desktop\nichtbearbeiteteFiles\VD.csv","w") as file:
    for row in dataVD:
        csv.writer(file).writerow(row)



queryZG = " SELECT JOBNAME FROM OPCONCI.dbo.JMASTER WHERE SHORTNAME LIKE 'ZGI1%%%000ZG' OR SHORTNAME LIKE 'ZGI1%%%010%%';"
cursor.execute(queryZG)
dataZG = cursor.fetchall()
with open (r"C:\Users\rdju\Desktop\nichtbearbeiteteFiles\ZG.csv","w") as file:
    for row in dataZG:
        csv.writer(file).writerow(row)




queryVZ = "SELECT JOBNAME FROM OPCONCI.dbo.JMASTER WHERE SHORTNAME LIKE 'VZI1%%%000%%' OR SHORTNAME LIKE 'VZI1%%%010%%';"
cursor.execute(queryVZ)
dataVZ = cursor.fetchall()
with open (r"C:\Users\rdju\Desktop\nichtbearbeiteteFiles\VZ.csv","w") as file:
    for row in dataVZ:
        csv.writer(file).writerow(row)
        
cursor.close()
conx.close()