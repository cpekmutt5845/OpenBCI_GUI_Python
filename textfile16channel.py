# textfile16channel.py use for cyton+daisy (16-channels)
# please note that you should streaming on OpenBCI_GUI with 16 channels, if stream 8 channels please use textfile.py instead

import csv
import shutil

txtFilePath = 'C:/Program Files/OpenBCI_GUI/SavedData/'
# =============================================================================
# timeMeasure = int(input("How long you want to streaming(min)?:"))
# print("You will streaming "+str(timeMeasure)+" mins")
# =============================================================================

howLine = int(input("How many lines you want to stream?:"))
print("You will streaming "+str(howLine)+" lines")

choice = int(input("select txt file name(use 1 in this case):"))
if choice == 1:
    txtname = "OpenBCI-RAW-2017-12-15_18-42-47.txt"
    print("your txt file name: ",txtname)
elif choice == 2:
    txtname = "OpenBCI-RAW-BrainStreaming.txt"
    print("your txt file name: ",txtname)    
elif choice == 3:
    txtname = "whatever.txt"
    print("your txt file name: ",txtname)

#   OpenBCI-RAW-BrainStreaming.txt
#    OpenBCI-RAW-2017-12-15_18-42-47.txt

while True:

    outputCondition = False
    restrict = False
    validateDataset = False
    count = 0
    count2 = 0
    countLine = 0

        
    shutil.copyfile(txtFilePath+txtname, txtFilePath+'cloneFile.txt')
    txtstream = open(txtFilePath+'cloneFile.txt', 'r')
    csvReader = csv.reader(txtstream)
    row_count = sum(1 for a in csvReader)
    print("count: "+str(row_count))
    txtstream.close()
    
    txtstream = open(txtFilePath+'cloneFile.txt', 'r')
    csvReader = csv.reader(txtstream)
    line1 = next(csvReader)
    line2 = next(csvReader)
    line3 = next(csvReader)
    line4 = next(csvReader)
    line5 = next(csvReader)
    line6 = next(csvReader)

    head = next(csvReader)

    coordList = []
    outputList = []

    for row in csvReader:
        if countLine < row_count-7-1:
#            print("row count:"+str(row_count)+"countLinee:"+str(countLine))
            sampleIndex = row[0]
            channel_1 = row[1]
            channel_2 = row[2]
            channel_3 = row[3]
            channel_4 = row[4]
            channel_5 = row[5]
            channel_6 = row[6]
            channel_7 = row[7]
            channel_8 = row[8]
            channel_9 = row[9]
            channel_10 = row[10]
            channel_11 = row[11]
            channel_12 = row[12]
            channel_13 = row[13]
            channel_14 = row[14]
            channel_15 = row[15]
            channel_16 = row[16]
            aux_1 = row[17]
            aux_2 = row[18]
            aux_3 = row[19]
            timestamp = row[20]
            
            coordList.append([sampleIndex, channel_1, channel_2, channel_3, channel_4, channel_5, channel_6, channel_7, channel_8, channel_9, channel_10, channel_11, channel_12, channel_13, channel_14, channel_15, channel_16, aux_1, aux_2, aux_3, timestamp])
            float_channel_1 = float(coordList[count][1].replace(" ", ""))
            float_channel_2 = float(coordList[count][2].replace(" ", ""))
            float_channel_3 = float(coordList[count][3].replace(" ", ""))
            float_channel_4 = float(coordList[count][4].replace(" ", ""))
            float_channel_5 = float(coordList[count][5].replace(" ", ""))
            float_channel_6 = float(coordList[count][6].replace(" ", ""))
            float_channel_7 = float(coordList[count][7].replace(" ", ""))
            float_channel_8 = float(coordList[count][8].replace(" ", ""))
            float_channel_9 = float(coordList[count][9].replace(" ", ""))
            float_channel_10 = float(coordList[count][10].replace(" ", ""))
            float_channel_11 = float(coordList[count][11].replace(" ", ""))
            float_channel_12 = float(coordList[count][12].replace(" ", ""))
            float_channel_13 = float(coordList[count][13].replace(" ", ""))
            float_channel_14 = float(coordList[count][14].replace(" ", ""))
            float_channel_15 = float(coordList[count][15].replace(" ", ""))
            float_channel_16 = float(coordList[count][16].replace(" ", ""))

            if (howLine>0 and outputCondition) or (restrict == False and float_channel_1>0 and float_channel_2>0 and float_channel_3>0 and float_channel_4>0 and float_channel_5>0 and float_channel_6>0 and float_channel_7>0 and float_channel_8>0 and float_channel_9>0 and float_channel_10>0 and float_channel_11>0 and float_channel_12>0 and float_channel_13>0 and float_channel_14>0 and float_channel_15>0 and float_channel_16>0):
                outputCondition = True
                outputList.append([sampleIndex, channel_1, channel_2, channel_3, channel_4, channel_5, channel_6, channel_7, channel_8, channel_9, channel_10, channel_11, channel_12, channel_13, channel_14, channel_15, channel_16, aux_1, aux_2, aux_3, timestamp])
#                print("row:"+row[0]+"  howline"+str(howLine) + "time" + row[12])
                howLine = howLine - 1
                if howLine == 0:
                    restrict = True # we restict because we don't want to append anymore

            count = count + 1
        
            if restrict == True and howLine == 0:
                print("Trigger!")
                break
            
            countLine = countLine + 1
        

    txtstream.close()
    csvReader = 0
        
    if restrict == True:
        break

#next, write output file before bring this one to model

f = open(txtFilePath+'out.txt','w',encoding='utf-8')

#write header first
f.write(str(line1)+'\n')
f.write(str(line2)+'\n')
f.write(str(line3)+'\n')
f.write(str(line4)+'\n')
f.write(str(line5)+'\n')
f.write(str(line6)+'\n')

for a in outputList:
    a[1] = str(a[1].replace(" ", ", "))
    a[2] = str(a[2].replace(" ", ", "))
    a[3] = str(a[3].replace(" ", ", "))
    a[4] = str(a[4].replace(" ", ", "))
    a[5] = str(a[5].replace(" ", ", "))
    a[6] = str(a[6].replace(" ", ", "))
    a[7] = str(a[7].replace(" ", ", "))
    a[8] = str(a[8].replace(" ", ", "))
    a[9] = str(a[9].replace(" ", ", "))
    a[10] = str(a[10].replace(" ", ", "))
    a[11] = str(a[11].replace(" ", ", "))
    a[12] = str(a[12].replace(" ", ", "))
    a[13] = str(a[13].replace(" ", ", "))
    a[14] = str(a[14].replace(" ", ", "))
    a[15] = str(a[15].replace(" ", ", "))
    a[16] = str(a[16].replace(" ", ", "))
    a[17] = str(a[17].replace(" ", ", "))
    a[18] = str(a[18].replace(" ", ", "))
    a[19] = str(a[19].replace(" ", ", "))
    a[20] = str(a[20].replace(" ", ", "))

    f.write(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]+'\n')
    count2 = count2 + 1
f.close()
