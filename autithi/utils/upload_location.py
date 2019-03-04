import os
import random


def get_filename_ext(filepath):
    return os.path.splitext(os.path.basename(filepath))


def upload_image_path(instance, filename):
    print(instance, filename)
    new_filename = random.randint(1, 99999999)
    name, ext = get_filename_ext(filename)
    final_filename = f"{new_filename}{ext}"
    return f"products/{new_filename}/{final_filename}"
