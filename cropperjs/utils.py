# coding=utf-8

import sys
from base64 import b64decode

from django.core.files.base import ContentFile
from django.utils.text import slugify

# Used for consistent string/type comparisons across Python 2 and 3
# without requiring six, future or other external dependencies
TEXT_TYPE = str if sys.version_info[0] >= 3 else unicode

def cropperImageFile(base64data, defaultName):
    try:
        metadata, imagedata = base64data.split("base64")
        filename, mimetype = metadata[:-1].split(";")
    except:
        # Too many values to unpack, unexpected format
        raise ValueError
    if 'filename' in metadata:
        filename = metadata.split(";")[0].split(":")[1]
        filename = slugify(filename)
    else:
        filename = defaultName
    fileext = mimetype.split("/")[1]

    return ContentFile(b64decode(imagedata), "%s.%s" % (filename, fileext))

