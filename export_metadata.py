'''Given a sqlite database file, will convert the database to a CSV file.
Takes two command line arguments:
1) The path to the database file (Mandatory argument).
2) The path or name of a CSV file (optional).
'''

# Standard modules
import sys
import sqlite3

# Non-standard modules
import pandas.io.sql as sql

__author__ = "Andrew Moore"
__email__  = "a.moore@lancaster.ac.uk"

# Reference:
# http://stackoverflow.com/questions/17556450/sqlite3-python-export-from-sqlite-to-csv-text-file-does-not-exceed-20k

if (len(sys.argv) != 2 or len(sys.argv) != 3):
    exception = """ The script takes 2 or 3 arguments:\n
    1) The path to the database file (Mandatory argument)\n
    2) The path or name of a CSV file (optional)
    """
    raise Exception(exception)

database_name = sys.argv[1]
csv_file = sys.argv[2] if len(sys.argv) > 2 else 'output.csv'
con = sqlite3.connect(database_name)
table = sql.read_frame('select * from output', con)
table.to_csv(csv_file)
