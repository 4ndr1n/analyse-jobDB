import pandas as pd

def getFile(x):
    file = "/Users/Andrin/Desktop/OpCon_data/" + x + ".csv"

    return file

def getData():
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

    df.to_csv("/Users/Andrin/Desktop/Output.csv")
    return df

def cleanData(df):

    df['result'] = df['result'].map(lambda x: x.lstrip('').rstrip('aAbBcC'))

def main():
    getData()


if __name__ == "__main__":
    main()