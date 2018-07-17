# coding=utf-8

import re
from base64 import b64decode

from django.core.files.base import ContentFile


def cropperImageFile(base64data, defaultName):
    try:
        metadata, imagedata = base64data.split("base64")
        filename, mimetype = metadata[:-1].split(";")
    except:
        # Too many values to unpack, unexpected format
        raise ValueError
    if 'filename' in metadata:
        filename = metadata.split(";")[0].split(":")[1]
        filename = re.sub("[^a-zA-Z0-9]", "", filename.lower())
    else:
        filename = defaultName
    fileext = mimetype.split("/")[1]

    return ContentFile(b64decode(imagedata), "%s.%s" % (filename, fileext))

