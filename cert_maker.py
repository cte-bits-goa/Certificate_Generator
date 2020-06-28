import numpy as np
import pandas as pd
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import sys
import textwrap
import logging
import os
from tqdm import tqdm
from swd_wrapper import get_swd

if __name__ == "__main__":
    
    '''
    A new SWD scrapper has been added which is integrated with the same file
    '''


    #Take args from command line
    arguments = sys.argv[1:]

    #Take Three inputs, The src image or template, CSV which consists of User Data and The common message to be printed
    assert len(arguments) == 3, 'Arguments not provided Properly'     

    #source img
    source_img = Image.open(arguments[0])

    #CSV Modify these variables for columns of CSV if required, Otherwise stick to the notation
    #csv = pd.read_csv(arguments[1])
    csv = get_swd(arguments[1])
    names=csv['Name']
    courses=csv['Course']
    positions=csv['Position']
    ids=csv['ID']

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


    pwd = os.getcwd()
    pwd.replace('\\', '/') #takes care of windows format
    filename = pwd + '/info.log' 

    logging.basicConfig(level=logging.INFO, filename=filename, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


    #zip and iterate through all lists/columns in the csv
    for name,id,position,course in tqdm(zip(names,ids,positions,courses)):
        
        #Create a temporary image
        temp_img = source_img.copy()

        #Replace your variables with assigned tokens in text
        if position.lower() == "instructor":
            position = "an " + position
        elif position.lower() == "mentor":
            position = "a " + position
        message=temp.replace('[1]',position)
        message=message.replace('[2]',course)
        name = name.title()
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
        
        #Save the certificates to ID_CourseName.png, make sure you use ID and Course Name both to avoid duplication.
        temp_img.save('certs/{}_{}.png'.format(id,course))

        #Logger to keep track
        logging.info("{} {} - Completed".format(id, name))

        '''
        import time
        time.sleep(0.1) #DNS server block

        #Go to Mailer script for documnetation github - @someshsingh22
        mailer.mail(id,name,message_email)

        This pipeline feature has been removed since certificates are sent through websites, For mass mailing use automailer from the parent directory
        '''
    logging.critical('Completed!')
