import pandas as pd

def getFile(x):
    file = "/Users/Andrin/Desktop/OpCon_data/" + x + ".csv"

    return file

def getData(Kantone):
    Kantone = ["AG","LU","SH","VD","ZV","ZG","ZH"]
    df = pd.DataFrame()
    length = []
    holder = []

    for x in Kantone:
        file = open(getFile(x))
        t = file.readlines()
        holder.append(t)
        length.append(len(t))

    maxim = max(length)

    for x in holder:
        if len(x) == maxim:
            pass
        else:
            t = len(x)
            x.extend(['']*((maxim)-t))

    for index,x in enumerate(Kantone):
        df[x] = holder[index]

    return df

def cleanData(df,Kantone):

    for i,x in enumerate(Kantone):
        uneven = i*2-1
        print(uneven)
        df.insert(uneven,x+'nr',df[x].str.extract(r'(\d+_\d+)'))
        df[x] = df[x].map(lambda x: str(x)[15:])

    df.to_csv("/Users/Andrin/Desktop/Output.csv")
    return df

def main():
    Kantone = ["AG","LU","SH","VD","ZV","ZG","ZH"]
    Data = getData(Kantone)
    CD = cleanData(Data,Kantone)


if __name__ == "__main__":
    main()