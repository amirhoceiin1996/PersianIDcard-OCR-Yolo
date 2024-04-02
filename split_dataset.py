import os
import shutil
import random

def split_dataset(input_folder, output_folder, split_ratio=0.8):
    # Create output folders if they don't exist
    train_folder = os.path.join(output_folder, 'images', 'train')
    val_folder = os.path.join(output_folder, 'images', 'val')
    train_labels_folder = os.path.join(output_folder, 'labels', 'train')
    val_labels_folder = os.path.join(output_folder, 'labels', 'val')

    for folder in [train_folder, val_folder, train_labels_folder, val_labels_folder]:
        os.makedirs(folder, exist_ok=True)

    # List all image files in the input folder
    image_files = [f for f in os.listdir(os.path.join(input_folder, 'images')) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Calculate the number of images for the validation set
    num_val_images = int(len(image_files) * (1 - split_ratio))

    # Randomly shuffle the list of image files
    random.shuffle(image_files)

    # Split the dataset into training and validation sets
    train_images = image_files[:num_val_images]
    val_images = image_files[num_val_images:]

    # Move image files to their respective folders
    for image in train_images:
        shutil.move(os.path.join(input_folder, 'images', image), os.path.join(train_folder, image))
        shutil.move(os.path.join(input_folder, 'labels', image.replace(os.path.splitext(image)[-1], '.txt')),
                    os.path.join(train_labels_folder, image.replace(os.path.splitext(image)[-1], '.txt')))

    for image in val_images:
        shutil.move(os.path.join(input_folder, 'images', image), os.path.join(val_folder, image))
        shutil.move(os.path.join(input_folder, 'labels', image.replace(os.path.splitext(image)[-1], '.txt')),
                    os.path.join(val_labels_folder, image.replace(os.path.splitext(image)[-1], '.txt')))

if __name__ == "__main__":
    input_dataset_folder = r"C:\Users\amirh\OneDrive\Desktop\ID_Card\IDCARD\Hand"
    output_dataset_folder = "HandDataset"

    split_dataset(input_dataset_folder, output_dataset_folder)