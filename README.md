# Radiology-Report-generation
# MedViLL

This repository provides the code for MedViLL(Medical Vision Language Learner).

---

 
## 1) Downloads.
### Pre-trained weights.
We provide five versions of BERT-based pre-trained weights with different types of self-attention masks. Pre-training for the joint embedding was built on the BERT-base architecutre(12 hidden layers, 12 attention heads, 768 hidden size), and training details are described in our paper. Currently avaliable versions of pre-trained weights are as follows:
 
- [MedViLL](https://drive.google.com/file/d/1shOQrOWbkIeUUsQN48fEP6wj0e266jOb/view?usp=sharing) - BERT-Base model with Bidirectional Auto-regressive attention mask.

### Datasets.
We provide a pre-processed version of multiple datasets for each task as follows:
 
 Download each dataset to the path /data/[dataset].
- [MIMIC-CXR](https://drive.google.com/file/d/1aVamW2kBkcVUxhq2lOi38mKHEQ33FhQZ/view?usp=sharing) (2.27 GB): Unique study of 91,685 AP view image and associated report pairs.
- [OPEN-I](https://drive.google.com/file/d/1aAKW2UcR7KhX9rckYtNfTfzNYulgrzle/view?usp=sharing) (74.1 MB): Unique study of 3,547 AP and PA image-report pairs from the official Open-I dataset.


 
## 2) Reproduce.
### Section A. Installation
Sections below describe the virtual env installation and the fine-training process of MedviLL based on pytorch version 1.7, python version 3.8. 
To fine-tune MedViLL, you need to download the pre-trained weights of MedViLL. After downloading the pre-trained weights, use medvill.yaml to install conda based virtual env as follows:

```
$ git clone https://github.com/SuperSupermoon/MedViLL.git
$ cd Radiology_report_Generation ; conda env create --file medvill.yaml
```

 

### Section B. Prepare pre-processed dataset

Unzip mimic, openi, and VQA-RAD tar.gz files. 

```
$ cd Radiology_report_Generation; tar -zxvf [file_name.tar.gz]
```

### Section C. Pre-training model
Example:
```
$ cd MedViLL
$ python main.py
```


### Section D. Downstream model

- Report Generation
Example:
```
$ cd MedViLL/downstream_task/report_generation_and_vqa
$ python finetune.py --tasks report_generation --mask_prob 0.15 --s2s_prob 1 --bi_prob 0
```
