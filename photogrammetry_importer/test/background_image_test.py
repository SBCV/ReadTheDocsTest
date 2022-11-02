import os
import bpy


image_fp = "/home/sebastian/Desktop/test/100_7104.JPG"

# Create camera with dynamic Background
camera_name = "CameraWithDynamicBackground"
bcamera = bpy.data.cameras.new(camera_name)
animated_cam_obj = bpy.data.objects.new(camera_name, bcamera)
bpy.context.collection.objects.link(animated_cam_obj)

# Determine directory path and file name
dp = os.path.dirname(image_fp)
first_fn = os.path.basename(image_fp)

# Remove previously created movie clip (if any)
if first_fn in bpy.data.movieclips:
    bpy.data.movieclips.remove(bpy.data.movieclips[first_fn])
# Create movie clip
first_sequence_fn = [{"name": first_fn}]
bpy.ops.clip.open(directory=dp, files=first_sequence_fn)

# Add Movie Clip as Background Image Sequence
dynamic_camera_data = bpy.data.objects[animated_cam_obj.name].data
dynamic_camera_data.show_background_images = True
dynamic_background_image = dynamic_camera_data.background_images.new()
dynamic_background_image.source = "MOVIE_CLIP"
dynamic_background_image.clip = bpy.data.movieclips[first_fn]

# Add camera with Static Background
cam_with_static_bg_name = "CameraWithStaticBackground"
cam_with_static_bg = bpy.data.cameras.new(cam_with_static_bg_name)
cam_with_static_bg_obj = bpy.data.objects.new(cam_with_static_bg_name, cam_with_static_bg)
cam_with_static_bg_obj.matrix_world[0][3] = 1
bpy.context.collection.objects.link(cam_with_static_bg_obj)

# Add Single Background Image
static_camera_data = bpy.data.objects[cam_with_static_bg_name].data
static_camera_data.show_background_images = True
static_background_image = static_camera_data.background_images.new()
static_background_image.image = bpy.data.images.load(image_fp)