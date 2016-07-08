import sys
import subprocess
import os
import re

results_folder = sys.argv[1]
if not os.path.exists(results_folder):
    raise Exception("The result folder %s does not exist" %results_folder)
results_folder = os.path.abspath(results_folder)
output_directory = sys.argv[2]
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
