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


** If you found any problems in my code please don't hesitate to issues **
