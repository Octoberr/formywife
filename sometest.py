from PIL import Image

from pathlib import Path

clo = Path("./pictures/pants")

for c in clo.iterdir():
    print(c.as_posix())
    im = Image.open(c.as_posix())
    (x, y) = im.size # 读取图片大小
    new_x = 750
    new_y = 1038
    out = im.resize((new_x, new_y), Image.ANTIALIAS)
    out.save(f"./pants/{c.name}")