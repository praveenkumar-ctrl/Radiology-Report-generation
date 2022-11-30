import torch
import os
a=torch.rand(512,512)
batch=[]
x = []
b=torch.rand(512,512)
x.append(a)
x.append(b)
s=torch.stack(x)
print(s.shape)
batch.append(s)
from PIL import Image
for filename in os.listdir("/home/cse/ckm/code/seelam/code/MedViLL/data/vqa_rad/home/mimic-cxr/dataset/data_RAD/img_preprocess"):
    image = Image.open(os.path.join("/home/cse/ckm/code/seelam/code/MedViLL/data/vqa_rad/home/mimic-cxr/dataset/data_RAD/img_preprocess",filename))
    print(f"Original size : {image.size}")
    # img_resized = image.resize((512, 512))
    # img_resized.save(os.path.join("/home/cse/ckm/code/seelam/code/MedViLL/data/vqa_rad/home/mimic-cxr/dataset/data_RAD/img_preprocess",filename))
# print(f"Original size : {image.size}") # 5464x3640

# sunset_resized = image.resize((400, 400))
# sunset_resized.save('sunset_400.jpeg')

