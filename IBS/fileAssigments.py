import os
import datetime

'''"Assign13: File Size(s)
Write code to print size of multiple filename(s) entered by users. Use functions to meaningfully break down code

(Deadline: Feb 8)"'''

def fileExistsOrNot(filename:str, parent_dir_loaction:str =".")-> bool:
    fileLoc = f"{parent_dir_loaction}/{filename}"
    # print(fileLoc)
    return os.path.exists(fileLoc),fileLoc

def fileSizeOf(filename:str, parent_dir_loaction:str =".")->int:
    sizeInBytes = 0
    isExists,fileLoc = fileExistsOrNot(filename, parent_dir_loaction)
    if isExists:
        with open(fileLoc,"rb") as f:

            sizeInBytes = sizeInBytes + len(f.read())
    else:
        raise FileNotFoundError("no such file or directory")
    return sizeInBytes


'''"Assign14: File Truncator

Write a program to accept two filenames - input and output.

Truncate output file if exists, and write all the Odd numberd lines of 'input' into 'output'. Discard the Even numbered lines

(Deadline: Feb 8)"'''

def writeOddLinesInputToOutput(inputFileName:str, outputFileNAme:str=None, inputFileDir:str=".",outputFileDir:str=".")->str:

    ## checking for existance of input the files
    inputIsExists,inputFileLoc = fileExistsOrNot(inputFileName, inputFileDir)
    outputISExists, outputFileLoc = fileExistsOrNot(outputFileNAme, outputFileDir)
    if not inputIsExists: 
        raise FileNotFoundError("No such file or directory")
    else:
        odd_content_list = []
        with open(inputFileLoc,"r") as f :
            content_list = f.readlines()
            odd_content_list = odd_content_list + [content for i , content in enumerate(content_list) if i%2!=0 ]
        if outputISExists:
            with open(outputFileLoc,"w") as f :
                f.writelines(odd_content_list)
            return outputFileLoc
        else :
            newOutputFile = f"output_{datetime.datetime.now()}.txt"
            with open(newOutputFile,"w") as f:
                f.writelines(odd_content_list)
            return newOutputFile
            

        

if __name__=="__main__":
    parent_dir_loaction="./IBS"
    inputFileName = "abc.txt"
    sizeofFile = fileSizeOf(inputFileName,parent_dir_loaction)
    print(sizeofFile)

    outploc = writeOddLinesInputToOutput(inputFileName,inputFileDir=parent_dir_loaction)
    print(outploc)
