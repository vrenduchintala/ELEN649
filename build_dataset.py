# USAGE
# python build_dataset.py

# import the necessary packages
from pyimagesearch import config
from imutils import paths
import shutil
import os

# loop over the data splits
for split in (config.TRAIN, config.TEST):
    # grab all image paths in the current split
        #if split == config.TRAIN:
            #continue
        print("[INFO] processing '{} split'...".format(split))
        p = os.path.sep.join([config.ORIG_INPUT_DATASET, split])
        imagePaths = list(paths.list_images(p))

        # loop over the image paths
        #i  =  0
        for imagePath in imagePaths:
            # extract class label from the filename
                #i = i+1
                filename = imagePath.split(os.path.sep)[-1]
                print(imagePath)
                # construct the path to the output directory
                dirpath = ''
                label= config.CLASSES[int(imagePath.split("/")[2].split("c")[1])]
                dirPath = os.path.sep.join([config.BASE_PATH, split, label])
                #print(dirPath)
                # if the output directory does not exist, create it
                if not os.path.exists(dirPath):
                    os.makedirs(dirPath)

                # construct the path to the output image file and copy it
                p = os.path.sep.join([dirPath, filename])
                print(p)
                shutil.copy2(imagePath, p)
                #if i > 100:
                 #   break
