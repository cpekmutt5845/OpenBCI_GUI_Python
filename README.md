# OpenBCI_GUI_Python

Dependencies:
- Python 3.6
- OpenBCI GUI
- ULTRACORTEX MARK IV

I collect dataset from OpenBCI_GUI or you can get it on this link >> http://docs.openbci.com/OpenBCI%20Software/01-OpenBCI_GUI

For more infomation about ULTRACORTEX MARK IV is on >> http://docs.openbci.com/Headware/01-Ultracortex-Mark-IV

NOTE:

- This code is compatible with Cyton (8-channels): textfile.py and Cyton+Daisy (16-channels): textfile16channel.py

- Please change txtFilePath = 'C:/Program Files/OpenBCI_GUI/SavedData/' to 'SavedData/' or path of your 'OpenBCI_GUI/SavedData/'

- "How many lines you want to stream?:" is a number of lines of out.txt

- Make sure you change the name of streaming text file on OpenBCI GUI to "BrainStreaming" before streaming device, in that case you'll can go to case choice==2

- I haven't delete " [''] " in header of output yet!

- out.txt will locate in the same directory ("SavedData" in this case) but you can merge my code to save out.txt in somewhere else

![alt text](https://www.picz.in.th/images/2017/12/18/555020d43cf849c83c5.png)


HOW TO RUN:
1. Following OpenBCI GUI instruction on link above
2. Stream data on OpenBCI GUI first (and change name to "BrainStreaming")
3. Press "START SYSTEM"
4. Press spacebar to initial streaming
5. run textfile.py if use 8 channels, textfile16channel.py if use 16 channels
6. input your prefer of a number of lines for out.txt (output text and we will use this to model)
7. program will loop until triggered (ex. wearing ULTRACORTEX MARK IV)
8. out.txt will be created


** If you found any problems in my code please don't hesitate to issues **
