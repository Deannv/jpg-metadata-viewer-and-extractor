from PIL import Image
from PIL.ExifTags import TAGS

imagename = "example.jpg"

image = Image.open(imagename)
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

for label, value in info_dict.items():
    print(f"{label:25}: {value}")

rawExifData = image.getexif()

for imageTagId in rawExifData:
    imageTag = TAGS.get(imageTagId, imageTagId)
    metaData = rawExifData.get(imageTagId)
    if isinstance(metaData, bytes):
        metaData = metaData.decode()

    print(f"{imageTag:25}: {metaData}")
