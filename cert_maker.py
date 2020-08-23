import numpy as np
import pandas as pd
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import sys
import textwrap
from fpdf import FPDF
import PyPDF2
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader, PdfFileWriter
if __name__ == "__main__":

    '''
    SWD WebScraper for names has been removed in this version due to its revamp.
    The name correction from SWD will be incorporated later
    '''


    #Take args from command line
    arguments = sys.argv[1:]

    #Take Three inputs, The src image or template, CSV which consists of User Data and The common message to be printed
    assert len(arguments) == 3

    #source img
    source_img = Image.open(arguments[0])

    #CSV Modify these variables for columns of CSV if required, Otherwise stick to the notation
    csv = pd.read_csv(arguments[1])
    names=csv['Name']
    ids=csv['ID']
    positions=csv['Position']
    courses=csv['Course']
    courseids=csv['CourseId']
    certids=csv['CertID']


    #Message, for each arguement to be available in text replace it with tokens
    #e.g. Look in the loop, [1] and [2] are used for the instructor / mentor status and the course name respectively
    temp=open(arguments[2]).read()

    #Create a PILLOW image
    draw = ImageDraw.Draw(source_img)

    #Create a bounding box for the coordinates based on pixel offset
    bounding_box = [300, 320, 800, 385]
    x1, y1, x2, y2 = bounding_box  # For easy reading

    #Import fonts as available in the directory
    font = ImageFont.truetype('PTF55F.ttf', size=30)
    font_ = ImageFont.truetype('arial.ttf', size=30)

    #zip and iterate through all lists/columns in the csv
    for name,id,position,course,courseid,certid in zip(names,ids,positions,courses,courseids,certids) :

                #Create a temporary image
                temp_img = source_img.copy()

                #Replace your variables with assigned tokens in text
                message=temp.replace('[1]',position)
                message=message.replace('[2]',course)

                #Copy the temp img to a PIL draw board
                draw = ImageDraw.Draw(temp_img)
                w, h = draw.textsize(name, font=font)

                #Adjust these coordinates to fix the text, this is under dev due to non constant templates you will have to ecperiment on a small batch
                #X and Y here represent the center coords for name of the cert reciever.
                ## CUSTOM ##
                x = (x2 - x1 - w)/2 + x1 - 20
                y = (y2 - y1 - h)/2 + y1

                #Draw the name over, color for text can be changed with fill, custom hex value can also be passed
                draw.text((x, y), name, align = 'center', fill = 'red', font = font)

                #Iterate adjustable coordinates down to print the message
                ## CUSTOM ##
                x=x1/3
                y=y+45

                #Wrap the text in different lines color for text can be changed with fill, custom hex value can also be passed
                ## CUSTOM ##
                message = '\n'.join(textwrap.wrap(message, 65, break_long_words=False))

                #Print the message on the certificate.
                draw.text((x, y), message, align = 'center', fill = (80,163,180), font = font)

                dir = os.path.join("certs",courseid)
                if not os.path.exists(dir):
                        os.mkdir(dir)

                #Save the certificates to ID_CourseName.png, make sure you use ID and Course Name both to avoid duplication.
                temp_img.save('certs/{}/{}.pdf'.format(courseid,id))

                #Logger to keep track
                #print("{} {}".format(id, name))

                '''
                import time
                time.sleep(0.1) #DNS server block

                #Go to Mailer script for documnetation github - @someshsingh22
                mailer.mail(id,name,message_email)

                This pipeline feature has been removed since certificates are sent through websites, For mass mailing use automailer from the parent directory
                '''




                '''
                The following code generates a pdf with cert id hyperlink and save it in urltemp folder
                '''

                #for name,id,position,course,courseid,certid in zip(names,ids,positions,courses,courseids,certids):
                class PDF(FPDF):
                    # Page footer
                    def footer(self):
                        # Position at 3 cm from bottom
                        self.set_y(-30)
                        # Arial italic 16
                        self.set_font('Arial', 'I', 16)
                        # print cert id
                        self.cell(0, 10, "Certificate ID: {}".format(certid), 0, 0, 'C',False,'http://legacy-cert.bpgc-cte.org/certs/{}.html'.format(certid))

                # Instantiation of inherited class
                pdf = PDF('L','mm',(287.87,372.53))
                pdf.add_page()
                dir = os.path.join("urltemp",courseid)
                if not os.path.exists(dir):
                    os.mkdir(dir)

                pdf.output('urltemp/{}/{}.pdf'.format(courseid,id), 'F')


                '''

                The following code merges the pdfs
                '''


                #for name,id,position,course,courseid,certid in zip(names,ids,positions,courses,courseids,certids):
                output = PdfFileWriter()

                ipdf = PdfFileReader(open('certs/{}/{}.pdf'.format(courseid,id), 'rb'))
                wpdf = PdfFileReader(open('urltemp/{}/{}.pdf'.format(courseid,id), 'rb'))

                watermark = wpdf.getPage(0)
                page = ipdf.getPage(0)
                page.mergePage(watermark)
                output.addPage(page)

                dir = os.path.join("final",courseid)
                if not os.path.exists(dir):
                    os.mkdir(dir)

                with open('final/{}/{}.pdf'.format(courseid,id), 'wb') as f:
                   output.write(f)

                #logger
                print("{} {}".format(courseid,id))
