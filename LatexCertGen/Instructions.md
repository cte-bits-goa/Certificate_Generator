TexLive Package is used to convert the tex file into Pdf

The original tex file was created using a live online tex to pdf converter overleaf.com

    The template used on overleaf.com was cert.pdf

To install TexLive

1.  on linux:

    sudo apt-get install Texlive

    (incase you face any errors on some packages not being installed also type :
    sudo apt-get install texlive-latex-extra)

2.  for MacOS you could use a similar program called
    Mactex
    https://tug.org/mactex/mactex-download.html

3.  for Windows users try
    TexLive
    MicTex
    Lyx
    (Advice: mictex and lyx may take a long while to install.)

The csv file is used for data entry into certGen.tex which then outputs a PDF containing all the certificates.

To run the command to convert tex to pdf

1. Linux
   try
   'pdflatex --output-directory=../otherdir /path/to/myfile.tex' in the terminal.
   ->IMPORTANT - When running this command make sure that you are in the directory containing the .tex file as well as other files which may be needed to run it (Eg: Records.csv,etc)
2. MacOs
   Follow instructions on MacTex website
3. Windows
   MicTex and Lyx are both Gui programs with elements to convert .tex to .pdf

Process:

1. First run the preprocess.py script with a Records.csv file in the same directory

2.When running latex file make sure to have the CTE_logo.png and FinalRecords.csv in the same directory and make sure to run the TexLive command after you cd to the folder containing all these files

3.Finally run the splitter.py to split the pdf generated after step2 and go to the Certificates folder to find all certificates which are labelled as CertID_ID.pdf
