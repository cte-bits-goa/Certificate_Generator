TexLive Package is used to convert the tex file into Pdf

The original tex file was created using a live online tex to pdf converter overleaf.com

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

4.  you can also run the tex file online on the website [Overleaf](https://www.overleaf.com "Overleaf home")
    The csv file is used for data entry into certGen.tex which then outputs a PDF containing all the certificates.

To run the command to convert tex to pdf

1. Linux
   try
   'pdflatex --output-directory=../otherdir /path/to/myfile.tex' in the terminal.
   ->IMPORTANT - When running this command make sure that you are in the directory containing the .tex file as well as other files which may be needed to run it (Eg: Records.csv,etc)
2. MacOs
   Follow instructions on MacTex website
3. Windows
   MicTex and Lyx are both GUI programs with elements to convert .tex to .pdf

Process:

1.First run the preprocess.py script with a Records.csv file in the same directory which outputs a FinalRecords.csv file.

2.When running latex file make sure to have the CTE_logo.png and FinalRecords.csv in the same directory and make sure to run the TexLive command after you cd to the folder containing all these files

3.Finally run the splitter.py to split the pdf generated after step2 and go to the Certificates folder to find all certificates which are labelled as CertID_ID.pdf

4 .For two signs exchange this minipage codeblock with the last minipage in certGen.tex
(line 65)

```latex
		\begin{minipage}[l]{8.8in}

		{\hspace{-0.55cm}\includegraphics[width=.1\linewidth,]{sign.pdf} \hspace{10.41cm}\includegraphics[width=0.1\linewidth]{sign.pdf}}

		  {\hspace{-0.35cm}\shortstack{\vrule width 2in height 0.2pt\\\footnotesize} 		  {\hspace{7.51cm}\shortstack{\vrule width 2in height 0.2pt\\\footnotesize}}
}


			{\hspace{-0.55cm} \textbf {\scriptsize PROF. BHARAT M DESHAPANDE (HEAD, CTE)}\hspace{1.6cm} \textbf{\scriptsize SUHRUDH S (PRESIDENT,CTE)}\\ \vspace{0.3cm}{\hspace{-0.58cm} \color{lightgrey}{\small BITS PILANI KK BIRLA GOA CAMPUS}}}
			% you can change the fontsize by using "tiny,footnotesize,small,medium,large"
		\end{minipage}}

```

Note : To change the contents of the certificates ull need to change the text in the latex file. Also remember to change the date!