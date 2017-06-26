'''Removes the boiler plate from a folder of HTML files and outputs them as
text files in a given output directory. Takes two command line arguments:
1) The path to the folder of HTML files.
2) The path or name of a folder where the text files will be stored NOTE that
the folder does not have to exist.
'''

import sys
import subprocess
import os
import re

import justext

__author__ = "Andrew Moore"
__email__  = "a.moore@lancaster.ac.uk"

if len(sys.argv) != 3:
    exception = """ The script takes 2 arguments:\n
    1) The path to the folder containing HTML files.\n
    2) The path or name of the folder you would like the boiler plate removed
    HTML files to be stored as text files (Note the folder does not have to exist)
    """
    raise Exception(exception)

results_folder = sys.argv[1]
output_directory = sys.argv[2]

if not os.path.exists(results_folder):
    raise Exception("The result folder %s does not exist" %results_folder)
results_folder = os.path.abspath(results_folder)

output_directory = os.path.abspath(output_directory)
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

for html_file in os.listdir(results_folder):

    # Has to be a HTML file
    if re.match("\w*.html", html_file) is None:
        continue

    html_file_path = os.path.join(results_folder, html_file)
    with open(html_file_path, 'rb') as fp:
        paragraphs = justext.justext(fp.read(), set())#, justext.get_stoplist("English"))

    text_file_name = html_file.split('.')[0] + '.txt'
    output_file_path = os.path.join(output_directory, text_file_name)
    with open(output_file_path, 'w', encoding='utf-8') as fp:
        for paragraph in paragraphs:
            fp.write(paragraph.text)
