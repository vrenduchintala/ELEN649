# import the necessary packages
import os

# initialize the path to the *original* input directory of images
ORIG_INPUT_DATASET = "distracted_drivers"

# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
BASE_PATH = "imgs"

# define the names of the training, testing, and validation
# directories
TRAIN = "train"
TEST = "test"

# initialize the list of class label names
CLASSES = ["c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"]

# set the batch size
BATCH_SIZE = 32

# initialize the label encoder file path and the output directory to
# where the extracted features (in CSV file format) will be stored
LE_PATH = os.path.sep.join(["img_output", "le.cpickle"])
BASE_CSV_PATH = "img_output"

# set the path to the serialized model after training
MODEL_PATH = os.path.sep.join(["img_output", "model.cpickle"])
