import time
import bpy
import numpy as np
from PIL import Image, ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True
import PIL
print(PIL.__version__)


class StopWatch(object):
    """Class to measure computation times."""

    def __init__(self):
        self.last_t = time.time()

    def reset_time(self):
        """Reset the stop watch to the current point in time."""
        self.last_t = time.time()

    def get_elapsed_time(self):
        """Return the elapsed time."""
        current_t = time.time()
        elapsed_t = current_t - self.last_t
        self.last_t = current_t
        return elapsed_t


sw = StopWatch()

#absolute_fp = "/home/sebastian/Pictures/saved_with_shutter.png"
# absolute_fp = "/home/sebastian/Pictures/100_7100.JPG"
absolute_fp = "/mnt/Data-512GB/BlenderAddons/ImageDataset_SceauxCastle/fixed_images/100_7100.JPG"
# absolute_fp = "/mnt/Data-512GB/BlenderAddons/ImageDataset_SceauxCastle/temp_png/100_7100.PNG"
x_json_file = 500
y_json_file = 500

# Option 1:
sw.reset_time()
pil_image = Image.open(absolute_fp)
pix = pil_image.getpixel((x_json_file, y_json_file))
print(pix)
print(sw.get_elapsed_time())

# Option 2:


# # Option 3:
# sw.reset_time()
# blender_data_image = bpy.data.images.load(absolute_fp)
# np_array = np.asarray(blender_data_image.pixels)
# np_array = np_array.reshape((blender_data_image.size[0], blender_data_image.size[1], blender_data_image.channels))
# pix = np_array[x_json_file, y_json_file]
# print(pix)
# print(sw.get_elapsed_time())


#########################
# def _copy_values_to_image(value_tripplets, image_name):
#     """ Copy values to image pixels. """
#     image = bpy.data.images[image_name]
#     # working on a copy of the pixels results in a MASSIVE performance speed
#     local_pixels = list(image.pixels[:])
#     for value_index, tripplet in enumerate(value_tripplets):
#         column_offset = value_index * 4  # (R,G,B,A)
#         # Order is R,G,B, opacity
#         local_pixels[column_offset] = tripplet[0]
#         local_pixels[column_offset + 1] = tripplet[1]
#         local_pixels[column_offset + 2] = tripplet[2]
#         # opacity (0 = transparent, 1 = opaque)
#         # local_pixels[column_offset + 3] = 1.0    # already set by default
#     image.pixels = local_pixels[:]