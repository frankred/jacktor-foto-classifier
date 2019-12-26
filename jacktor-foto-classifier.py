import cv2
import os
import argparse
import sqlite3
import numpy as np
from pyfiglet import figlet_format
from termcolor import cprint 
from pyfiglet import figlet_format

# Logo
cprint(figlet_format('Jacktor', font='starwars'))

# Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pictures", required=True, help="path to the pictures folder")
ap.add_argument("-x", "--prototxt", default="models/MobileNetSSD_deploy.prototxt.txt", help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-c", "--confidence", type=float, default=0.2, help="minimum probability to filter weak detections")
ap.add_argument("-m", "--model", default="models/MobileNetSSD_deploy.caffemodel", help="path to Caffe pre-trained model")
args = vars(ap.parse_args())
fotos_folder = args["pictures"]

# Database
database_path = fotos_folder + '/' + 'photos.sqlite'
conn = sqlite3.connect(database_path)
conn.text_factory = str
c = conn.cursor()

def table_already_exists(table_name):
    c.execute("SELECT name FROM sqlite_master WHERE name='" + table_name + "'")
    rows = c.fetchall()
    if len(rows) > 0:
        print('[table already exist]: ' + table_name)
        return True
    else:
        return False

def index_already_exists(index_name, table_with_index):
    c.execute("PRAGMA INDEX_LIST('" + table_with_index + "')")
    conn.commit()
    rows = c.fetchall()
    for row in rows:
        if row[1] == index_name:
            print('[table index already exists]: ' + index_name)
            return True
    return False

if not table_already_exists('picture'):
    print('[create table start]: ' + 'picture')
    c.execute('''CREATE TABLE "picture" ("id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "filepath" TEXT NOT NULL)''')
    conn.commit()
    print('[create table end]: ' + 'picture')

if not table_already_exists('tag'):
    print('[create table start]: ' + 'tag')
    c.execute('''CREATE TABLE "tag" ("id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "picture_id" INTEGER, "tag" TEXT, "confidence" REAL, "x_start" REAL, "x_end" REAL, "y_start" REAL, "y_end" REAL, FOREIGN KEY("picture_id") REFERENCES "picture"("id") ON DELETE CASCADE)''')
    conn.commit()
    print('[create table end]: ' + 'tag')
    
if not index_already_exists('filepath_index', 'picture'):
    print('[create index filepath_index start]')
    c.execute('''CREATE INDEX filepath_index ON picture (filepath)''')
    conn.commit()
    print('[create index filepath_index end]')

    
if not index_already_exists('tag_index', 'tag'):
    print('[create index tag_index start]')
    c.execute('''CREATE INDEX tag_index ON tag (tag)''')
    conn.commit()
    print('[create index tag_index end]')

# OpenCV
# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
    "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])


########################################################################################
########################################################################################
########################################################################################

def scan(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        if subfolders:
            for subfolder in subfolders:
                scan(subfolder)

        for filename in filenames:
            filepath = folderName + '\\' + filename
            
            if picture_already_exists(filepath):
                continue

            image = cv2.imread(filepath)
            if image is None:
                continue

            print('[NEW]: ' + filepath)
            picture_id = insert_picture(filepath)
            detect_image(filepath, picture_id, image)

def picture_already_exists(filepath):
    c.execute("SELECT id FROM picture WHERE filepath=? LIMIT 1", (filepath,))
    rows = c.fetchall()
    if len(rows) > 0:
        print('[OK]: ' + filepath)
        return True
    else:
        return False

def insert_picture(filepath):
    c.execute("INSERT INTO picture (filepath) VALUES (?)", (filepath,))
    conn.commit()
    c.execute("SELECT id FROM picture where filepath=:filepath LIMIT 1", {"filepath": filepath})
    rows = c.fetchall()
    return rows[0][0] # return id

def insert_tag(picture_id, tag, confidence, x_start, x_end, y_start, y_end):
    c.execute("INSERT INTO tag (picture_id, tag, confidence, x_start, x_end, y_start, y_end) VALUES (?,?,?,?,?,?,?)", (picture_id, tag, confidence, x_start, x_end, y_start, y_end))
    conn.commit()

def detect_image(image_path, picture_id, image):
    # load the input image and construct an input blob for the image
    # by resizing to a fixed 300x300 pixels and then normalizing it
    # (note: normalization is done via the authors of the MobileNet SSD
    # implementation)

    if image is not None:
        print('[resize start]: ' + image_path)
        image = image_resize(image, height = 800)
        (image_height, image_width) = image.shape[:2]
        print('[resize end]: ' + image_path)

        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843,
            (300, 300), 127.5)

        # pass the blob through the network and obtain the detections and
        # predictions
        # print("[INFO] computing object detections...")
        net.setInput(blob)
        detections = net.forward()

        # loop over the detections
        for i in np.arange(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with the
            # prediction
            confidence = detections[0, 0, i, 2]
        
            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > args["confidence"]:
                # extract the index of the class label from the `detections`,
                # then compute the (x, y)-coordinates of the bounding box for
                # the object
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([image_width, image_height, image_width, image_height])
                (startX, startY, endX, endY) = box.astype("float")

                x_start = startX / image_width
                x_end = endX / image_width
                y_start = startY / image_width
                y_end = endY / image_width

                print('[tag]: ' + CLASSES[idx] + ' ' + str(float(confidence)) + ' (' + str(x_start) + ', ' +  str(x_end) + ', ' +  str(y_start) + ', ' +  str(y_end)  + ')')
                insert_tag(picture_id, CLASSES[idx], float(confidence), x_start, x_end, y_start, y_end)

                # display the prediction
                # label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                # print("{}".format(label))
                # cv2.imshow("Output", image)

                #print("[INFO] {}".format(label))
                # cv2.rectangle(image, (startX, startY), (endX, endY),
                #    COLORS[idx], 2)
                # y = startY - 15 if startY - 15 > 15 else startY + 15
                # cv2.putText(image, label, (startX, y),
                #    cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

                # if CLASSES[idx] is 'cat':
                #    print('Cat ' + str(confidence * 100) + '%:' + image_path)
                #     # show the output image
                #
                #    if show_gui is 1:
                #        cv2.imshow("Output", image)

def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized

########################################################################################
########################################################################################
########################################################################################





# Scan
scan(fotos_folder)

# Close db connection
conn.commit()
c.close()
conn.close()
exit()