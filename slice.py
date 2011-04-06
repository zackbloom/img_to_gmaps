import sys
import os.path
import os
import shutil
import Image

ZOOM_MIN = 0
ZOOM_MAX = 2
TILE_WIDTH = 640
TILE_HEIGHT = 480

def make_out_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

    os.makedirs(path)

def open_image(path):
    return Image.open(path)

def slice_img(in_path, out_path):
    in_img = open_image(in_path)

    x1, y1, x2, y2 = in_img.getbbox()
    w = width = x2 - x1
    h = height = y2 - y1

    for zoom in range(ZOOM_MIN, ZOOM_MAX + 1):
        path = os.path.join(out_path, str(zoom))
        os.mkdir(path)

        parts = 2 ** (zoom + 1)
        
        for y_i in range(0, parts):
            y_path = os.path.join(path, str(y_i))
            os.mkdir(y_path)

            for x_i in range(0, parts):
                img_path = os.path.join(y_path, str(x_i) + '.png')
                
                img = in_img.crop((w*x_i, h*y_i, w*(x_i + 1), h*(y_i + 1)))
                img.resize((TILE_WIDTH, TILE_HEIGHT))
                img.save(img_path)

        w = w / 2
        h = h / 2

if __name__ == '__main__':
    in_path = sys.argv[1]
    out_path = os.path.join(os.path.dirname(__file__), 'static', 'cart_imgs')

    make_out_dir(out_path)
    slice_img(in_path, out_path)
