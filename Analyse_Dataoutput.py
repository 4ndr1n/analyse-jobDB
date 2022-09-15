from collections import Counter
import pandas as pd
from pyparsing import Regex

class get:
    def File(x):
        file = "/Users/Andrin/Desktop/OpCon_data/" + x + ".csv"

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

        df.to_csv("/Users/Andrin/Desktop/Output.csv")

        return df

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

    def space2(df):
        x1 = 0
        x2 = 0
        numbers = []
        dff = pd.DataFrame()
        nrCol = df[df.columns[::2]]
        nCol = df[df.columns[1::2]]
        i = 0
        ColumnIndex=0
        for col in nrCol:
            AbsoluteLine=0
            relativeLine=0
            ColumnNumber = df[col]
            x1,x2 = get.TwoVals(x1,x2,ColumnNumber[1])
            for num in ColumnNumber:
                x1,x2 = get.TwoVals(x1,x2,num)
                dif = x2-x1
                
                x1r = x1

                if dif == 1:
                    NameValue = nCol[df.columns[ColumnIndex+1]][relativeLine+1]
                    dff.at[AbsoluteLine,df.columns[ColumnIndex+1]] = NameValue
                    dff.at[AbsoluteLine,df.columns[ColumnIndex]] = x1r
                    AbsoluteLine+=1

                    
                while dif > 1:    
                    dff.at[AbsoluteLine,df.columns[ColumnIndex]] = x1r
                    x1r += 1
                    dif = x2-x1r
                    AbsoluteLine+=1

                
                relativeLine+=1


            if i < 12:
                i+=1
                ColumnIndex+=2
                    
        dff.to_csv("/Users/Andrin/Desktop/Output_2.csv")
        return numbers

    def dummy(df): 
        nrCol = df[df.columns[::2]]
        for col in nrCol:
            nr = df[col]
            print(df.columns[0])


    def lines2(gap):
        lines_list = []
        count = Counter(gap)
        print(count)
        
        for x in count:
            if count.get(x) >= 6:
                lines_list.append(x)
        return lines_list

    def equals(CD):
        equals = []
        
        return equals
                                  
def main():
    Kantone = ["AG","LU","SH","VD","ZV","ZG","ZH"]
    Data = get.Data(Kantone)
    CD = make.CleanData(Data,Kantone)
    #make.dummy(CD)
    gap = make.space2(CD)
    #lines = make.lines2(gap)
    #equals = make.equals(CD)
    #print(lines)



if __name__ == "__main__":
    main() 