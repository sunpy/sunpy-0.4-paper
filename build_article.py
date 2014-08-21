#!/usr/bin/env python
import os

paper_name = "Sunpy_paper_0.4"
            
try:
    os.remove(paper_name + '.aux')
except:
    pass

try:
    os.remove(paper_name + '.bbl')
except:
    pass
    
os.system('pdflatex -shell-escape ' + paper_name)
os.system('pdflatex -shell-escape ' + paper_name)
os.system('bibtex ' + paper_name)
os.system('pdflatex -shell-escape ' + paper_name)
os.system('pdflatex -shell-escape ' + paper_name)
