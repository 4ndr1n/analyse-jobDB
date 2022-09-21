from collections import Counter
import pandas as pd

class get:
    def File(x):
        file = "\C:\\" + x + ".csv"

        return file

    def Data(Kanton):
        df = pd.DataFrame()
        length = []
        holder = []

        for x in Kanton:
            file = open(get.File(x))
            t = file.readlines()
            holder.append(t)
            length.append(len(t))

        maxim = max(length)

        for x in holder:
            if len(x) == maxim:
                pass
            else:
                t = len(x)
                x.extend([0]*((maxim)-t))

        for index,x in enumerate(Kanton):
            df[x] = holder[index]

        return df

    def TwoVals(x1,x2,x):
        if x1 == 0:
            x1 = x
        elif x2 == 0:
            x2 = x
        else: 
            x1 = x2
            x2 = x
        return x1, x2

class make:
    def CleanData(df,Kantone):
        for x in Kantone:
            t =  1
            df[x+'nr'] = df[x].str.extract(r'(\d+)')
            df[x] = df[x].map(lambda x: str(x)[15:])
            df[x] = df[x].str.replace(r'(\s[A-Z]{2}-)', '',regex=True)

        df = df[['AGnr','AG','LUnr','LU','SHnr','SH','VDnr','VD','ZVnr','ZV','ZHnr','ZH','ZGnr','ZG']]

        df = df.drop([0])

        for x in Kantone:
            df[x+"nr"] = pd.to_numeric(df[x+"nr"])

        return df

# Wird nicht verwendet, gibt nur die leeren Zeilennummern aus.
    def space(df):
        x1 = 0
        x2 = 0
        numbers = []
    
        nrCol = df[df.columns[::2]]
        for x in nrCol:
            nr = df[x]
            x1,x2 = get.TwoVals(x1,x2,nr[1])
            for y in nr:
                x1,x2 = get.TwoVals(x1,x2,y)
                dif = x2-x1
                x1r = x1
                while dif > 1:    
                    x1r += 1
                    numbers.append(x1r)
                    dif = x2-x1r
        return numbers

    def lines(gap):
        lines_list = []
        count = Counter(gap)
        
        for x in count:
            if count.get(x) >= 6:
                lines_list.append(x)
        return lines_list
 
    def spaces(df):
        numbers = []
        ndf = pd.DataFrame()
        nrCol = df[df.columns[::2]]
        nCol = df[df.columns[1::2]]
        nrColIndex = 0

        
        for column in nrCol:
            x1 = 0
            x2 = 0
            outputLine=0
            sourceLine=1
            ColumnNumber = df[column]
            x1,x2 = get.TwoVals(x1,x2,ColumnNumber[1])
            length = max(df[column])

            if ColumnNumber[1] != 1001:
                x1=1001
            first = True
            for num in ColumnNumber:
                x1,x2 = get.TwoVals(x1,x2,num)
                dif = x2-x1
                
                x1cp = x1

                loopdie = False
                while dif > 1:
                    if x1 == x1cp:
                        NameValue = nCol[df.columns[nrColIndex+1]][sourceLine]
                        if ColumnNumber[1] != 1001 and first == True:
                            NameValue = ""
                            first = False
                            sourceLine-=1    
                        ndf.at[outputLine,df.columns[nrColIndex+1]] = NameValue
                        sourceLine+=1

                    ndf.at[outputLine,df.columns[nrColIndex]] = x1cp
                    x1cp += 1
                    dif = x2-x1cp
                    outputLine+=1
                    loopdie = True
                
                if loopdie == True:
                    ndf.at[outputLine,df.columns[nrColIndex]] = x1cp
                    outputLine+=1
            

                if dif == 1 and loopdie == False:
                    ndf.at[outputLine,df.columns[nrColIndex]] = x1cp
                    NameValue = nCol[df.columns[nrColIndex+1]][sourceLine]
                    ndf.at[outputLine,df.columns[nrColIndex+1]] = NameValue
                    outputLine+=1
                    sourceLine+=1

                if x2 == length:
                    ndf.at[outputLine,df.columns[nrColIndex]] = x2
                    NameValue = nCol[df.columns[nrColIndex+1]][sourceLine-1]
                    ndf.at[outputLine,df.columns[nrColIndex+1]] = NameValue
                    sourceLine+=1

                
            nrColIndex+=2
        ndf = ndf[['AGnr','AG','LUnr','LU','SHnr','SH','VDnr','VD','ZVnr','ZV','ZHnr','ZH','ZGnr','ZG']]
        ndf.to_csv("\C:\output.csv\\",sep=";")
        return numbers

def main():
    Kantone = ["AG","LU","SH","VD","ZV","ZG","ZH"]
    Data = get.Data(Kantone)
    CD = make.CleanData(Data,Kantone)
    make.spaces(CD)

if __name__ == "__main__":
    main() 