import os
from PIL import Image

def merge_images(directory):

    images = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(directory, filename)
            images.append(Image.open(filepath))

    total_width = sum(image.width for image in images)
    max_height = max(image.height for image in images)

    merged_image = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for image in images:
        merged_image.paste(image, (x_offset, 0))
        x_offset += image.width

    merged_image.save('merged_image.jpg')

if __name__ == '__main__':
    directory = 'merged'
    merge_images(directory)
