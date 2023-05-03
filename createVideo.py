import cv2
import os

path = "images/"

Images = []



for i in os.listdir(path):
    name, ext = os.path.splitext(i)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        File_Name = path+"/"+i

        print(File_Name)
               
        Images.append(File_Name)
        
print(len(Images))
count = len(Images)

frame = cv2.imread(Images[0]);
height, width, channels = frame.shape;
size = (width, height);
print(size);

out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc('m','p','4','v'), 0.8, size)

for i in range(0, count-1):
    imagens = cv2.imread(Images[1]);
    out.write(imagens)

out.release()
print("Concluido")
