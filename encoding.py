''' Given two command line arguments will identfy the encoding of the HTML files
using the metadata from when the files were downloaded and using a package that
identifies the encoding from the text. Then encodes the files to UTF-8 and
displays the statistics of the difference between the stated metadata encoding
and the encoding infered from the text. Two command line arguments:
1) The path to the folder containing HTML files.\n
2) The filename of the database used to contain the metadata.
'''

# Standard modules
import logging
import os
import sqlite3 as lite
import sys
# Non-standard modules
from chardet.universaldetector import UniversalDetector

__author__ = "Andrew Moore"
__email__  = "a.moore@lancaster.ac.uk"

def detected_encoding(page):
    '''Given a file object will return a dictionary of encodings and confidence values.

    Reference:
    https://chardet.readthedocs.io/en/latest/usage.html
    '''

    detector = UniversalDetector()

    for line in page.readlines():
        detector.feed(line)
        if detector.done:
            break

    detector.close()
    return detector.result


def get_charset(database):
    '''Given the database filepath will return a Cursor interator that contains
    a tuple of (url_id, charset).'''

    sql = "SELECT url_id, charset from output"
    con    = lite.connect(database)
    cursor = con.cursor()
    result = cursor.execute(sql)

    return result


logging.basicConfig(format='%(asctime)s %(message)s', filename='encoding.log', level=logging.INFO)

if len(sys.argv) != 3:
    exception = """ The script takes 2 arguments:\n
    1) The path to the folder containing HTML files.\n
    2) The filename of the database used to contain the metadata.
    """
    logging.debug(exception)
    raise Exception(exception)

results_folder = sys.argv[1]
database_name  = sys.argv[2]

if not os.path.exists(results_folder):
    logging.debug("The result folder %s does not exist" %results_folder)
    raise Exception("The result folder %s does not exist" %results_folder)
results_folder = os.path.abspath(results_folder)

database_path = os.path.join(results_folder, database_name)
if not os.path.exists(database_path):
    logging.debug("The database %s does not exist" %database_path)
    raise Exception("The database %s does not exist" %database_path)

difference_stats = {}

for row in get_charset(database_path):
    url_id, charset = row
    html_file = os.path.join(results_folder, str(url_id) + ".html")

    logging.info("Processing %s file." % html_file)

    guessed_encoding = None
    with open(html_file, 'rb') as f:
        guessed_encoding = detected_encoding(f)
    if guessed_encoding == None:
        print("Could not read the following file %s." %html_file)
        continue

    guessed_confidence = guessed_encoding['confidence']
    guessed_encoding   = guessed_encoding['encoding']
    logging.info("Guessed the following encoding %s with %1.2f confidence." %  (guessed_encoding, guessed_confidence))

    html_data = None

    if charset == None:
        logging.info("Charset defined by metadata does not exist.")
    else:
        logging.info("Charset defined by metadata %s." % charset)

        with(open(html_file, mode='r', encoding=charset)) as f:
            html_data = f.read()

    charset          = charset.lower()
    guessed_encoding = guessed_encoding.lower()

    # Convert HTML to UTF-8
    with(open(html_file, encoding=guessed_encoding, mode='r')) as f:
        logging.info("Read file as %s data for re-encoding to UTF-8." % guessed_encoding)
        html_data = f.read()

    if html_data == None:
        logging.info("No HTML data was read from %s" % html_file)
        continue

    # Write the converted data back to the the same file
    with(open(html_file, encoding='utf-8', mode='w')) as f:
        logging.info("Wrote back to file with UTF-8 data.")
        f.write(html_data)

    # See if the metadata encoding statement is different to the guessed
    # encoding from the data.
    if charset.lower() != guessed_encoding.lower():
        if charset not in difference_stats:
            difference_stats[charset] = {}
        if guessed_encoding not in difference_stats[charset]:
            difference_stats[charset][guessed_encoding] = [html_file]
        else:
            difference_stats[charset][guessed_encoding].append(html_file)

# Logging the stats of number of differences between the guessed encoding
# and the encoding specified within the page metadata.
logging.info("\n")
for metadata_charset, gussed_stats in difference_stats.items():
    outer_log = """The following number of times the encodings were guessed from the data
    which according to the metadata collected from the HTML headers should be %s:
    \n
    """
    logging.info(outer_log % metadata_charset)

    for guessed_charset, file_list in gussed_stats.items():
        logging.info("\n")

        inner_log = """guessed charset: %s number of times gussed differently
        with regards to metadata charset: %d"""
        logging.info(inner_log % (guessed_charset, len(file_list)))
        logging.info("The following files had those differences: \n")
        for a_file in file_list:
            logging.info("%s" % a_file)
