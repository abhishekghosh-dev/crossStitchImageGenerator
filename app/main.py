from PIL import Image, ImageDraw
import os

def main():
    print("Hello!!")
    draw()

def draw():
    file_path = input("Give the fila path : ") 
    image = Image.open(file_path)
    print("File opened!")
    print(f"You given file size is {image.height} X {image.width} (H x W)")
    h_step_count = int(input("Give the horigental step count : "))
    w_step_count = int(input("Give the vertical step count : "))

    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    w_step_size = int(image.width / w_step_count)
    h_step_size = int(image.height / h_step_count)

    for x in range(0, image.width, w_step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=0)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, h_step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=0)

    del draw

    file_name = os.path.basename(file_path).split('/')[-1]
    file_path = file_path.replace(file_name,'gen_' + file_name)
    image.save(file_path,"PNG") 
    image.show()
    print(f"genearated file at {file_path}!")

    

if __name__ == "__main__":
    main()