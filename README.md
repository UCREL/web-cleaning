# Web Cleaning
This repository links to data that is collected with the following [spider](https://github.com/UCREL/web-corpus-construction)
however it will work with any spider that stores HTML files into a directory
and contains a SQlite database (called metadata.db below). The database has to contain two columns
*url_id* and *charset* where url_id corresponds to the HTML file names and the
charset being the encoding found in the HTTP headers when gathering the web
pages e.g. utf-8.

## Slides that support the code
### [Main presentation slides](slides/UCREL_NLP_S2_Web_creation_cleaning_Intro.pdf)
Within the slides one of the practical tasks requires
[sqliteman](http://sourceforge.net/projects/sqliteman/files/).

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
    ..\..\python\python.exe encoding.py PATH_TO_THE_DB_DIR metadata.db

## boiler_removal.py
### What it does
1. Removes all the boiler plate from the given folder of HTML pages using
justext.

### How to run
Where output is the name of the folder you would like the boiler plate removed
text files to be stored. NOTE that the folder does not have to exist prior to running.

    ..\..\python\python.exe boiler_removal.py PATH_TO_THE_DB_DIR output

## export_metadata.py
### What it does
1. Exports the data from the given database file to a CSV file.

### How to run
Where output.csv is optional and by default it is output.csv but can be any
filename.

    ..\..\python\python.exe export_metadata.py PATH_TO_THE_DB_DIR\metadata.db output.csv

## [Dependencies](dependencies.md)
