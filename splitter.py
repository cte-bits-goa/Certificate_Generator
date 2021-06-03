from PyPDF2 import PdfFileWriter, PdfFileReader
import pandas as pd
import os

# This is a program to split the pdf generated after running latex into individual single page certificates
inputpdf = PdfFileReader(open("certGen.pdf", "rb"))
# We use the csv file before pre process since we had changed the
data = pd.read_csv("Records.csv", header=0)
ID = data["ID"]
CertID = data["CertID"]
for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    # we add the ID of student and CertID for a unique naming pattern for each certificate
    with open(
        "{}/{}_{}.pdf".format("Certificates", CertID[i], ID[i]), "wb+"
    ) as outputStream:
        output.write(outputStream)
