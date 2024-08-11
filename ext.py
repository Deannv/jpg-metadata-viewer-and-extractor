import argparse
from PIL import Image


def clearMetadata(imageName):
    img = Image.open(imageName)
    data = list(img.getdata())
    clearedImage = Image.new(img.mode, img.size)
    clearedImage.putdata(data)
    clearedImage.save(imageName)
    print(f"[ INFO ] Metadata successfully removed from '{imageName}'.")


parser = argparse.ArgumentParser(
    description="Remove metadata from an image."
)
parser.add_argument(
    "img",
    help="Image"
)
args = parser.parse_args()
if args.img:
    clearMetadata(args.img)
