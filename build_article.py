#!/usr/bin/env python
import os
import glob
from os.path import basename

paper_name = "Sunpy_paper_0.4"

# delete old output files
py_out_files = glob.glob("py_*.txt")
for file in py_out_files:
    try:
        os.remove(file)
    except:
        pass

py_files = glob.glob("python_code/*.py")
print(py_files)
for file in py_files:
    # the following just runs the file to create any pdfs the script may generate
    os.system('python ' + file)

    pretty_text_file = open('py_' + basename(file).split('.')[0] + ".txt", 'w')
    f = open(file)
    print("Running..." + file)
    import_statement = ['']
    for line in f.readlines():
        #    pretty_text_file.write(">>> " + content)
        #else pretty_text_file.write(content)
        print(line)
        if line[0] != '#':
            pretty_text_file.write(">>> " + line)
        else:
            pretty_text_file.write(line)
    f.close()
    pretty_text_file.close()
            
try:
    os.remove(paper_name + '.aux')
except:
    pass

try:
    os.remove(paper_name + '.bbl')
except:
    pass
    
#os.system('pdflatex -shell-escape ' + paper_name)
#os.system('pdflatex -shell-escape ' + paper_name)
#os.system('bibtex ' + paper_name)
#os.system('pdflatex -shell-escape ' + paper_name)
#os.system('pdflatex -shell-escape ' + paper_name)
