import random
from io import BytesIO
from PIL import ImageColor
from PIL import Image, ImageDraw


class Icon:
    def generate(self, hex=None):
        im = Image.new('RGB', (420, 420), (240, 240, 240))
        draw = ImageDraw.Draw(im)
        color = (94, 112, 214)

        if hex:
            color = ImageColor.getcolor(f'#{hex}', "RGB")

        for i in range(5):
            for j in range(5):
                x = 10 + (i*80)
                y = 10 + (j*80)
                x_ = x+80
                y_ = y+80
                if random.randrange(2):
                    draw.rectangle([(x, y), (x_, y_)], color)

        byte_io = BytesIO()
        im.save(byte_io, 'PNG')
        byte_io.seek(0)
        return byte_io