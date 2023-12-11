from alignment.align_images import align_images
import numpy as np
import imutils
import shutil
import cv2
import os
import glob

INPUT_DIR = "./surveys/"
OUTPUT_DIR = "./Results"
TEMPLATE_DIR = "./template.jpg"

def main():
  if(os.path.exists(OUTPUT_DIR)):
    shutil.rmtree(OUTPUT_DIR)

  os.mkdir(OUTPUT_DIR)

  for path, dirs, files in os.walk(INPUT_DIR):
    for file in files:
      print(file)
      if not file == '.DS_Store':
        print('AQUI ANDAMOS------------', INPUT_DIR + file, TEMPLATE_DIR)
        alignedDocument = align_document(INPUT_DIR + file, TEMPLATE_DIR)
        print("Results/" + file)
        cv2.imwrite("Results/" + file, alignedDocument)

def align_document(imagePath, templatePath):
  # load input image and template from storage
  print("[INFO] loading images...")
  image = cv2.imread(imagePath)
  template = cv2.imread(templatePath)

  # align the images
  print("[INFO] aligning images...")
  aligned = align_images(image, template, debug=True)

  # resize images and tempolate to visualise
  aligned = imutils.resize(aligned, width=700)
  template = imutils.resize(template, width=700)

  # side-by-side comparison
  stacked = np.hstack([aligned, template])

  # ovelay second image
  overlay = template.copy()
  output = aligned.copy()
  cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)

  # showing two output
  # cv2.imshow("Image alignment stack", stacked)
  # cv2.imshow("Image alignment overlay", output)
  # cv2.waitKey(0)
  return aligned

main()