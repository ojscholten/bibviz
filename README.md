# Bib File Visualizer (BibViz) Script
This script creates a basic bar chart style image based on the number of citations per year in a given bib file. This is useful for literature reviews and other literature work to quickly get an impression of the spread and relative timing of publications you are citing.

# Using This Script
This script uses Python 3.7.0 and requires the pybtex, pillow, and matplotlib packages installed using the command below;

pip install pybtex pillow matplotlib

## Call Command
To call this script use the command format below where the only argument is the name of the bib file in the same directory as the script;

python bibviz.py test.bib

# Notes
This project uses SaxMono, a 100% free font available here: https://www.dafont.com/saxmono.font

Other fonts can be added by changing the directory of the .ttf file.



Last tested & working: 20/10/2018
