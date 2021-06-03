import PIL.Image
ASCII_CHARS = ["@","#","S","%","?","*","+",";",":",",","."]
patch = input("Ruta de la imagen a dibujar: ")
try:
    image = PIL.Image.open(patch)
except:
    print("Ruta del Archivo no válida.")
    import time
    time.sleep(1)
    exit()
width, height = image.size
ratio = height / width / 2
if (width < 1024):
    new_width = width
else:
    new_width = 1024
new_height = int(new_width * ratio)
resized_image = image.resize((new_width,new_height))
grayscale_image = resized_image.convert("L")
pixels = grayscale_image.getdata()
ascii_image = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
pixel_count = len(ascii_image)
text_ascii_image = "\n".join(ascii_image[i:(i+new_width)] for i in range(0, pixel_count, new_width))
with open("ascii_image.txt","w") as f:
    f.write(text_ascii_image)
import webbrowser
webbrowser.open("ascii_image.txt")
