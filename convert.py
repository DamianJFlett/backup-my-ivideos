import sys
from PIL import Image
from pillow_heif import register_heif_opener

def convert_and_save(heic_name: str, out_name: str, out_format: str):
    register_heif_opener()
    
    im = Image.open(heic_name)
    im.save(out_name, out_format)