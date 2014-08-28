SunPy v 0.5 Paper
=================

This is the attempt to write a SunPy paper for submission, firstly, if we get a
talk at SciPy 2013, and failing that at a later date.

The proceedings of SciPy 2013 are being submitted to [Computational Science and
Discovery](http://iopscience.iop.org/1749-4699), which is what this LaTeX template is taken from.

## SciPy proceedings:
* The talk - https://github.com/Cadair/scipy2013_talks/tree/master/talks/stuart_mumford
* The paper - https://github.com/Cadair/scipy_proceedings/tree/2013/papers/stuart_mumford
* The (rendered) paper - http://conference.scipy.org/proceedings/scipy2013/pdfs/mumford.pdf

##References:
Add all refs to this group, Stuart will maintain the bib file.
https://www.zotero.org/groups/sunpy_-_python_for_solar_physicists/items/collectionKey/MNC7JEAA

## Typesetting Python Code
To make Python code look pretty use the [minted package](http://code.google.com/p/minted/) to 
use this you need to append `-shell-escape` to whereever you call pdflatex.

## Building
To build the paper run the python script `build_article.py'