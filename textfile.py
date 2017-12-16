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

# =============================================================================
#     while True:
#         shutil.copyfile(txtFilePath+txtname, txtFilePath+'cloneFile.txt')
#         txtstream = open(txtFilePath+'cloneFile.txt', 'r')
#         csv1stReader = csv.reader(txtstream)
#         p_line1 = next(csv1stReader)
#         p_line2 = next(csv1stReader)
#         p_line3 = next(csv1stReader)
#         p_line4 = next(csv1stReader)
#         p_line5 = next(csv1stReader)
#         p_line6 = next(csv1stReader)
#         p_head = next(csv1stReader)
#         
#         for row in csv1stReader:
#             if row[0]!="" and row[1]!="" and row[2]!="" and row[3]!="" and row[4]!="" and row[5]!="":
#                 validateDataset = True
#         
#         if validateDataset == True:
#             break
# =============================================================================
        
    shutil.copyfile(txtFilePath+txtname, txtFilePath+'cloneFile.txt')
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
        sampleIndex = row[0]
        channel_1 = row[1]
        channel_2 = row[2]
        channel_3 = row[3]
        channel_4 = row[4]
        channel_5 = row[5]
        channel_6 = row[6]
        channel_7 = row[7]
        channel_8 = row[8]
        aux_1 = row[9]
        aux_2 = row[10]
        aux_3 = row[11]
        timestamp = row[12]
            
        coordList.append([sampleIndex, channel_1, channel_2, channel_3, channel_4, channel_5, channel_6, channel_7, channel_8, aux_1, aux_2, aux_3, timestamp])
        float_channel_1 = float(coordList[count][1].replace(" ", ""))
        float_channel_2 = float(coordList[count][2].replace(" ", ""))
        float_channel_3 = float(coordList[count][3].replace(" ", ""))
        float_channel_4 = float(coordList[count][4].replace(" ", ""))
        float_channel_5 = float(coordList[count][5].replace(" ", ""))
        float_channel_6 = float(coordList[count][6].replace(" ", ""))
        float_channel_7 = float(coordList[count][7].replace(" ", ""))
        float_channel_8 = float(coordList[count][8].replace(" ", ""))

        if (howLine>0 and outputCondition) or (restrict == False and float_channel_1>0 and float_channel_2>0 and float_channel_3>0 and float_channel_4>0 and float_channel_5>0 and float_channel_6>0 and float_channel_7>0 and float_channel_8>0):
            outputCondition = True
            outputList.append([sampleIndex, channel_1, channel_2, channel_3, channel_4, channel_5, channel_6, channel_7, channel_8, aux_1, aux_2, aux_3, timestamp])
            print("row:"+row[0]+"  howline"+str(howLine) + "time" + row[12])
            howLine = howLine - 1
            if howLine == 0:
                restrict = True # we restict because we don't want to append anymore

        count = count + 1
        
        if restrict == True and howLine == 0:
            print("Trigger!")
            break
        
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

    f.write(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]+'\n')
    count2 = count2 + 1
f.close()
