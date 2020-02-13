import glob
import pydicom
import os
import cv2

# original dataset
root_dir = './2.8Gb Dignosis for Cancer'

# for filename in glob.iglob(root_dir + '**/**', recursive=True):
#     if '.dcm' in filename:

lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(root_dir):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName,filename))

"""accesing pixel_array for each file and convert to binary and store"""

for image_path in lstFilesDCM:
    ds = pydicom.dcmread(image_path) 
    brain_image = ds.pixel_array

    brain_image = brain_image.astype('uint8')
    brain_image = cv2.cvtColor(brain_image,cv2.COLOR_GRAY2BGR)
    brain_image_bytes = brain_image.tobytes()

    path = image_path.split("/")
    path = "lsdp_dataset/"+"_".join(path[1:])
    path = path[:-4]
    print(path)
    f = open(path,'wb')
    f.write(brain_image_bytes)
    f.close()

