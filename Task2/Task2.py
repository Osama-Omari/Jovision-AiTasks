from PIL import Image

def color_to_black(img):
    image = Image.open(img)
    image = image.convert('RGB')

    width , height = image.size
    
    newimage = Image.new('RGB', (width,height))

    for y in range(height):
        for x in range(width):
            r, g,b = image.getpixel((x,y))
            grayValue = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            newimage.putpixel((x,y),(grayValue,grayValue,grayValue))

    
    return newimage

if __name__ == "__main__":
    imgPath = r'C:/Users/ORZOm/Desktop/Jovision-AiTasks/Task2/Modric.JPG'
    newImage = color_to_black(imgPath)
    newImage.save(r'C:/Users/ORZOm/Desktop/Jovision-AiTasks/Task2/Test.JPG')
    newImage.show()