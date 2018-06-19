from PIL import Image
from mcpi.colors import typle_color
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y-1, pos.z, 35, 5)

def getIMG():
    img_name = input("Enter img name: ")
    #img_name = "burger.jpg"
    file = '/home/katerina/Рабочий стол/Python projects/Pictures/'+img_name
    im = Image.open(file)
    im = im.convert('RGBA')
    im.show()
    return im
"""
def cut(im):
    cut = (9, 12, 56, 53)
    im = im.crop(cut)
    ###
    cut_x, cut_y = 0, 0
    xsize, ysize = im.size
    for y in range(ysize):
    
        for x in range(xsize):
            print('')
"""           
       
im = getIMG()
xsize, ysize = im.size


for y in range(ysize):
    for x in range(xsize):
        pixel = im.getpixel((x,y))
        pixel = list(pixel)
        alpha = pixel.pop()
        block_id, block_data = typle_color(pixel)
        if  alpha > 10:
            #mc.setBlock(pos.x+xsize-x, pos.y+ysize-y, pos.z, block_id, block_data) # Вертикально
            mc.setBlock(pos.x+xsize-x, pos.y-1, pos.z-ysize+y, block_id, block_data) # Горизонтально
            
        
        
clear = input('Clear? T/F ')
if clear == 'T':
    for y in range(ysize):
        for x in range(xsize):
            mc.setBlock(pos.x+xsize-x, pos.y-1, pos.z-ysize+y, 0)
    print ('Area is clean')

    
