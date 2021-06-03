# Instructions to Use CTE Certificate Generator
TexLive Package is used to run the .tex files

## Requirements
### 1. Texlive Installation

#### Linux:

```
sudo apt-get install Texlive
#incase you face any errors on missing packages
sudo apt-get install texlive-latex-extra
```

#### OSX
Install [Mac-Tex](https://tug.org/mactex/mactex-download.html)

#### Windows
Download either of 
* TexLive
* MicTex
* Lyx
(Advice: mictex and lyx may take a long while to install.)

#### Overleaf
you can also run the tex file online on the website [Overleaf](https://www.overleaf.com "Overleaf home")

### 2. Dependencies
```bash
pip install -f requirements.txt
```


## Certificate Chunk
Files Required
1. Background Template - ./cert.pdf
2. CTE Logo - ./CTE_logo.png
3. CSV - ./FinalRecords.csv
4. Signature - ./sign.pdf

### Linux
```
pdflatex --output-directory=../otherdir /path/to/myfile.tex
```
### MacOs
Follow instructions on MacTex website
### Windows
MicTex and Lyx are both GUI programs with elements to convert .tex to .pdf
### Overleaf
Compile and Download PDF




## PDF Split
```
python splitter.py
```

## Process/Changes:

1. First run the [preprocess.py](preprocess.py) script with a Records.csv file in the same directory which outputs a FinalRecords.csv file.

2. When running latex file make sure to have the CTE_logo.png, cert.pdf, sign.pdf and FinalRecords.csv in the same directory and make sure to run the TexLive command after you cd to the folder containing all these files

3. Finally run the [splitter.py](splitter.py) to split the pdf generated after step2 and go to the Certificates folder to find all certificates which are labelled as CertID_ID.pdf

4. For two signs exchange this minipage codeblock with the last minipage in certGen.tex
(line 65)

```tex
		\begin{minipage}[l]{8.8in}

		{\hspace{-0.55cm}\includegraphics[width=.1\linewidth,]{sign.pdf} \hspace{10.41cm}\includegraphics[width=0.1\linewidth]{sign.pdf}}

		  {\hspace{-0.35cm}\shortstack{\vrule width 2in height 0.2pt\\\footnotesize} 		  {\hspace{7.51cm}\shortstack{\vrule width 2in height 0.2pt\\\footnotesize}}
}


			{\hspace{-0.55cm} \textbf {\scriptsize PROF. BHARAT M DESHAPANDE (HEAD, CTE)}\hspace{1.6cm} \textbf{\scriptsize SUHRUDH S (PRESIDENT,CTE)}\\ \vspace{0.3cm}{\hspace{-0.58cm} \color{lightgrey}{\small BITS PILANI KK BIRLA GOA CAMPUS}}}
			% you can change the fontsize by using "tiny,footnotesize,small,medium,large"
		\end{minipage}}

```

**Note : To change the contents of the certificates ull need to change the text in the latex file. Also remember to change the date!**
