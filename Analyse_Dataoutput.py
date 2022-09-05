from numpy import number
import pandas as pd

class get:
    def File(x):
        file = "/Users/Andrin/Desktop/OpCon_data/" + x + ".csv"

        return file

    def Data(Kanton):
        Kantone = ["AG","LU","SH","VD","ZV","ZG","ZH"]
        df = pd.DataFrame()
        length = []
        holder = []

        for x in Kantone:
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

        for index,x in enumerate(Kantone):
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

        df = df[['AGnr','AG','LUnr','LU','SHnr','SH','VDnr','VD','ZVnr','ZV','ZGnr','ZG','ZHnr','ZH']]

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
                
                while dif > 1:
                    x1 += 1
                    numbers.append(x1)
                    dif = x2-x1
                print(y,x1)

        return numbers
                
                    
                    
def main():
    Kantone = ["AG","LU","SH","VD","ZV","ZG","ZH"]
    Data = get.Data(Kantone)
    CD = make.CleanData(Data,Kantone)
    gap = make.space(CD)
    print(gap)

if __name__ == "__main__":
    main()