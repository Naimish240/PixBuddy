import click
import imagehash
import numpy as np
from PIL import Image
from tqdm import tqdm
from os import listdir


def calculate_hash(img, hash):
    image = Image.open(images[i])
    image.convert('L')
    image = image.resize((64, 64))

    if hash == 'avg_hash':
        hashes.append(imagehash.average_hash(image))
    elif hash == 'crop_hash':
        hashes.append(imagehash.crop_resistant_hash(image))
    elif hash == 'dhash':
        hashes.append(imagehash.dhash(image))
    elif hash == 'dhash_vert':
        hashes.append(imagehash.dhash_vertical(image))
    elif hash == 'phash':
        hashes.append(imagehash.phash(image))
    elif hash == 'whash':
        hashes.append(imagehash.whash(image))


def get_images(folder):
    images = []

    for item in listdir(folder):
        foo = item.lower()
        if foo[-4:] in ['.png', '.jpg'] or foo[-5:] in [".jpeg"]:
            images.append(folder + '/' + item)

    return images


@click.command()
@click.option(
    "--path",
    prompt="Path to index: ",
    help="Path to folder that contains all images"
)
@click.option(
    "--hash",
    prompt="Hash to use for comparision: ",
    help="avg_hash, crop_hash, dhash, dhash_vert, phash, whash"
)
def main(path, hash):
    images = get_images(path)
    hashes = []

    print("... Calculating Hashes.")

    for i in tqdm(range(len(images))):
        image = Image.open(images[i])
        image.convert('L')
        image = image.resize((64, 64))

        if hash == 'avg_hash':
            hashes.append(imagehash.average_hash(image))
        elif hash == 'crop_hash':
            hashes.append(imagehash.crop_resistant_hash(image))
        elif hash == 'dhash':
            hashes.append(imagehash.dhash(image))
        elif hash == 'dhash_vert':
            hashes.append(imagehash.dhash_vertical(image))
        elif hash == 'phash':
            hashes.append(imagehash.phash(image))
        elif hash == 'whash':
            hashes.append(imagehash.whash(image))

        else:
            print("... Invalid Hash!")
            return None


if __name__ == '__main__':
    main()
