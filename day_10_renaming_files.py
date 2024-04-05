import os
import glob


def main():
    # Prompt user for folder path
    folder_path = input("Enter the absolute folder path: ").strip()

    # Ensure the folder path is absolute
    if not os.path.isabs(folder_path):
        print("Please enter an absolute folder path.")
        return

    # Validate if the folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    # Get a list of all image files in the folder
    image_files = glob.glob(os.path.join(folder_path, "*.jpg")) + glob.glob(os.path.join(folder_path, "*.jpeg")) + glob.glob(
        os.path.join(folder_path, "*.png")) + glob.glob(os.path.join(folder_path, "*.gif")) + glob.glob(os.path.join(folder_path, "*.bmp"))

    if not image_files:
        print("No image files found in the folder.")
        return

    # Rename each image file sequentially
    for i, old_name in enumerate(image_files):
        # Extract file extension
        _, extension = os.path.splitext(old_name)

        # Construct new file name with leading zeros
        new_name = os.path.join(folder_path, f"{str(i+1).zfill(0)}{extension}")

        # Rename file
        os.rename(old_name, new_name)

    print("Image files renamed successfully.")


if __name__ == "__main__":
    main()
