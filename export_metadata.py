# Reference:
# http://stackoverflow.com/questions/17556450/sqlite3-python-export-from-sqlite-to-csv-text-file-does-not-exceed-20k

# Standard modules
import sys
import sqlite3
# Non-standard modules
import pandas.io.sql as sql

database_name = sys.argv[1]
csv_file = sys.argv[2] if len(sys.argv) > 2 else 'output.csv'
con = sqlite3.connect(database_name)
table = sql.read_frame('select * from output', con)
table.to_csv(csv_file)
