from PIL import Image
import math


#Функция возвращает средний цвет картинки
def avr_color(file_name):
    try:
        im = Image.open(file_name)
    except:
        print("No such file")
        return file_name
    im = im.convert('RGB')
    w, h = im.size
    pixel = []
 
    for x in range(w):
        for y in range(h):
            r, g, b = im.getpixel((x, y))
            pixel.append([r, g, b])
 
    avr = [sum(x)//len(x) for x in zip(*pixel)]
    return avr

def dif(col1, col2):
    return math.sqrt( (col1[0]-col2[0])**2 + (col1[1]-col2[1])**2 + (col1[2]-col2[2])**2 )
          
 
def typle_color(pixel):
    colors = {
        'white_wool'      : [(221, 221, 221), 35, 0],
        'orange_wool'     : [(219, 125, 62) , 35, 1],  
        'magenta_wool'    : [(179, 80, 188), 35, 2],
        'light_blue_wool' : [(106, 138, 201), 35, 3],
        'yellow_wool'     : [(177, 166, 39),  35, 4],
        'lime_wool'       : [(65, 174, 56),   35, 5],
        'pink_wool'       : [(208, 132, 153), 35, 6],
        'gray_wool'       : [(64, 64, 64),    35, 7],
        'silver_wool'     : [(154, 161, 161), 35, 8],
        'cyan_wool'       : [(46, 110, 137),  35, 9],
        'purple_wool'     : [(126, 61, 181),  35, 10],
        'blue_wool'       : [(46, 56, 141),   35, 11],
        'brown_wool'      : [(79, 50, 31),    35, 12],
        'green_wool'      : [(53, 70, 27),    35, 13],
        'red_wool'        : [(150, 52, 48),   35, 14],
        'black_wool'      : [(25, 22, 22),    35, 15],
        
        'white_clay'      : [(209, 177, 161), 159, 0],
        'orange_clay'     : [(161, 83, 37),   159, 1],
        'magenta_clay'    : [(149, 88, 108),  159, 2],
        'lightBlue_clay'  : [(113, 108, 137), 159, 3],
        'yellow_clay'     : [(186, 133, 35),  159, 4],
        'lime_clay'       : [(103, 117, 52),  159, 5],
        'pink_clay'       : [(162, 78, 78),   159, 6],
        'gray_clay'       : [(57, 42, 35),    159, 7],
        'silver_clay'     : [(135, 107, 97),  159, 8],
        'cyan_clay'       : [(86, 90, 91),    159, 9],
        'purple_clay'     : [(118, 70, 86),   159, 10],
        'blue_clay'       : [(74, 60, 91),    159, 11],
        'brown_clay'      : [(77, 51, 35),    159, 12],
        'green_clay'      : [(76, 83, 42),    159, 13],
        'red_clay'        : [(143, 61, 46),   159, 14],
        'black_clay'      : [(37, 23, 16),    159, 15],
       }
    
    
    min_dif = 10000
    block_id = 0
    block_data = 0

    for block in colors:
        diff = dif(pixel, colors[block][0])
        if diff < min_dif:
             min_dif = diff
             block_id = colors[block][1]
             block_data = colors[block][2]
    return block_id, block_data
             
                   
def avr_color():
    file_name = input("Enter file name: ")
    f = open(file_name, 'r')
    for line in f:
        file_name = line.strip() #Удаляем ненужные пробелы в начале и в конце line - строки

        # Убираем ненужную инфу, оставляем только цвет
        color = file_name
        '''
        color = color.replace('hardened_clay_stained_', ' ' )
        color = color.replace('.png', ' ' )
        color = color.strip()
        '''
        if len(file_name)>=3:
            avr = avr_color(str(file_name))
            print(color, avr)

    
     

