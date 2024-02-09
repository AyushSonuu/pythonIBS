'''"Assign17:

Improve manual csvreader, dictreader logics when some rows of lesser fields (or missing fields). Assign a default value in missing field case

Make it into function

Lesser fields: number of commas in less
Missing fields: abc,,def : middle field is missing"'''
import os
def fileExistsOrNot(filename:str, parent_dir_loaction:str =".")-> bool:
    fileLoc = f"{parent_dir_loaction}/{filename}"
    # print(fileLoc)
    return os.path.exists(fileLoc),fileLoc

def ManualcsvReader(filename:str, parent_dir_loaction:str =".",header=True,columns:list|None=None):
    csvExists, fileLoc =fileExistsOrNot(filename,parent_dir_loaction)
    if csvExists:
        with open(fileLoc,"r") as f :
            # list_rows = [ [i for i in range(len(row.split(",")))] if i==0 and not header else row.strip().split(",") for i,row in enumerate(f)   ]
            list_rows = []
            max_len_row = max([len(row.split(",")) for row in f])
            print(max_len_row)
            f.seek(0)
            for i, row in enumerate(f):
                if not header and i==0 :
                    if columns is None:
                        list_rows.append([i for i in range(max_len_row)])
                    elif len(columns)==max_len_row:
                        list_rows.append(columns)
                    else:
                        raise Exception(f"total of {max_len_row} columns but only provided with {len(columns)} columns")
                         
                else:
                    #handling missing values
                    rowData = (["NaN" if len(val)==0 else val for val in row.strip().split(",")])

                    #code for handling less columns
                    if (len(rowData)<max_len_row):
                        for i in range(len(rowData),max_len_row):
                            rowData.append("NaN")
                    list_rows.append(rowData)
        return list_rows
    else:
        raise FileNotFoundError("File not found in the location")

def manualDictReader(filename:str, parent_dir_loaction:str =".",header=True,columns:list|None=None):
    listOfLists = ManualcsvReader(filename, parent_dir_loaction,header,columns)
    header = listOfLists[0]
    return [{key: val for key,val in zip(header,row)} for row in listOfLists[1:]]




if __name__ == "__main__":
    dataList = ManualcsvReader("IBS/abc.csv",header=False,columns=['a','b','c','d'])
    print(dataList)
    datadict = manualDictReader("IBS/abc.csv",header=False,columns=['a','b','c','d'])

    print(datadict)

'''"Assign18:

Improve csv.reader and csv.DictReader csvreader, dictreader logics when some rows of lesser fields (or missing fields). Assign a default value in missing field case


Make it into function"'''