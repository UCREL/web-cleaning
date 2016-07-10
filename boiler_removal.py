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

if not os.path.exists(output_directory):
    os.mkdir(output_directory)
output_directory = os.path.abspath(output_directory)

command = "python -m justext -s English -o"
arguments = command.split()

for html_file in os.listdir(results_folder):
    # Has to be a HTML file
    if re.match("\w*.html", html_file) == None:
        continue
    file_name = html_file.split(".")[0]
    output_file = output_directory + os.sep + file_name + ".txt"
    html_file = results_folder + os.sep + html_file

    arguments.append(output_file)
    arguments.append(html_file)

    subprocess.run(arguments)

    arguments = arguments[:len(arguments)-2]
