# This function reads .xls file from Ledalab and convert it to an array
# str -- is te string of the file's path
def from_Ledalab(str):
    df2 = pandas.read_excel(open(str,'rb'))
    df2 = np.array(df2)
    #list(df2.values.flatten())
    #df2= df2.values.tolist()
    return df2

# Reconstruct the signal from phasic and tonic components generated from Ledalab
def reconstruct(phasic, tonic):
    rec = []
    for i in range(len(phasic)):
        rec.append((phasic[i] + tonic[i]))
    rec = filtering(rec,20)
    return rec