# Web Cleaning
## encoding.py
### What it does
1. Compares the stated character set encoding in the HTTP header to the
character set detected within the text using the python library chardet.
2. Then decodes with the character set detected within the text and re-encodes
into UTF-8.
3. Within the log file called encoding.txt at the bottom of the text file are
statistics on the number of difference between what the character set stated in
the HTML was and that of the detected character encoding.

### How to run
    ..\python\python.exe encoding.py ..\web-corpus-construction\output metadata.db

## boiler_removal.py
### What it does
1. Removes all the boiler plate from the given folder of HTML pages using
justext.

### How to run
Where output is the name of the folder you would like the boiler plate removed
text files to be stored. NOTE that the folder does not have to exist prior to running.

    ..\python\python.exe encoding.py ..\web-corpus-construction\output output

## export_metadata.py
### What it does
1. Exports the data from the given database file to a CSV file.

### How to run
Where output.csv is optional and by default it is output.csv but can be any
filename.

    ..\python\python.exe encoding.py ..\web-corpus-construction\output\metadata.db output.csv
