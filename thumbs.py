from io import BytesIO
from PIL import Image
import os
import io

import_filepath = "thumbsimport"
export_filepath = "thumbs"
for f in os.listdir(import_filepath):
    base, ext = os.path.splitext(f)
    if ext == ".png" or ".jpg":
        img = Image.open(import_filepath + "/" + f)
        size = img.height
        center_x = int(img.width / 2)
        center_y = int(img.height / 2)
        img = img.crop(
            (
                center_x - size / 2,
                center_y - size / 2,
                center_x + size / 2,
                center_y + size / 2,
            )
        )
        img = img.resize((256, 256))
        img.save(export_filepath + "/" + base + ".png", format="PNG")
    else:
        pass
