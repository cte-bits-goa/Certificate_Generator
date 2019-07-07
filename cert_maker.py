
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from tqdm import tqdm
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    assert len(arguments) != 0
    source_img = Image.open(arguments[0])

    list_names = pd.read_csv(arguments[1])
    if arguments[3] == 'Instructor':
        names = list_names.loc[(list_names['Course'] == arguments[2]) & (list_names['Instructor/Mentor'] == arguments[4]) ,'Name']
        names = list_names.loc[(list_names['Course'] == arguments[2]),['Name','Instructor/Mentor']]
    elif arguments[3] == 'Student':
        names = list_names.loc[(list_names['Course'] == arguments[2]) & (list_names['Type'] == arguments[4]) ,'Name']
        names = list_names.loc[(list_names['Course'] == arguments[2]),['Name','Type']]
    else:
        raise Exception('Invalid Argument at position 4 please refer the docs')
    draw = ImageDraw.Draw(source_img)
    bounding_box = [300, 320, 800, 385]
    x1, y1, x2, y2 = bounding_box  # For easy reading
    font = ImageFont.truetype('PTF55F.ttf', size=30)
    names_list = list(names)
    try:
        os.mkdir(arguments[2] + ' ' + arguments[4])
    except FileExistsError:
        pass
    for elem in tqdm(names_list):
        print(elem)
        temp_img = source_img.copy()
        draw = ImageDraw.Draw(temp_img)
        w, h = draw.textsize(elem, font=font)
        x = (x2 - x1 - w)/2 + x1
        y = (y2 - y1 - h)/2 + y1
        draw.text((x, y), elem, align = 'center', fill = 'red', font = font)
        temp_img.save(arguments[2] + ' ' + arguments[4] + '/{}.png'.format(elem))


# In[ ]:





# In[ ]:





# In[ ]:




