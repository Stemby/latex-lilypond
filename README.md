This project provides:
* a LaTeX package (`lilypond.sty`) to include lilypond-typeset music into a
  LaTeX document
* a Python script (`lilytex.py`) to get the music images
* the test files (`test.tex` and `testlily.ly`)

How to build the example
========================

Case 1 (pdfLaTeX)
-----------------
1. `$ pdflatex test.tex`
2. `$ python3 lilytex.py test.lil`
3. `$ pdflatex test.tex`

Case 2 (LaTeX)
--------------
1. `$ latex test.tex`
2. `$ python3 lilytex.py test.lil`
3. `$ latex test.tex`
