import os
import re
import cv2
import shutil
from pathlib import Path

def fix_naming(name):
    name = str(name)
    name = name.replace('(1)', '')
    name = name.replace('(2)', '')
    name = name.replace('(3)', '')
    name = name.replace('(4)', '')
    return name

def generate_training_set():
    img_and_ocr_path = Path('./sroie_dataset/0325updated.task1train(626p)-20210607T205344Z-001/0325updated.task1train(626p)')
    img_and_key_path = Path('./sroie_dataset/0325updated.task2train(626p)-20210610T032512Z-001/0325updated.task2train(626p)')
    
    dst_path = Path('./sroie_dataset/dataset/training_data/')
    dst_ocr = dst_path / "bbox"
    dst_img = dst_path / "images"
    dst_key = dst_path / "labels"

    dst_ocr.mkdir(parents=True, exist_ok=True)
    dst_img.mkdir(parents=True, exist_ok=True)
    dst_key.mkdir(parents=True, exist_ok=True)
    
    for i, source_img in enumerate(img_and_key_path.glob('**/*.jpg'), 1):
        file_num = str(i).zfill(3)
        base_name = source_img.stem
        source_key = img_and_key_path / f"{base_name}.txt"
        source_ocr = img_and_ocr_path / f"{base_name}.txt"
        if not all([source_ocr.exists(), source_key.exists()]):
            continue
        shutil.copy(source_ocr, dst_ocr / f"{file_num}.csv")
        shutil.copy(source_img, dst_img / f"{file_num}.jpg")
        shutil.copy(source_key, dst_key / f"{file_num}.json")

    

def generate_test_set():

    key_files_path = Path('./sroie_dataset/SROIE_test_gt_task_3/')
    img_files_path = Path('./sroie_dataset/SROIE_test_images_task_3/')
    ocr_files_path = Path('./sroie_dataset/text.task1_2-test（361p)/')

    dst_path = Path('./sroie_dataset/dataset/testing_data/')
    dst_ocr = dst_path / "bbox"
    dst_img = dst_path / "images"
    dst_key = dst_path / "labels"

    dst_ocr.mkdir(parents=True, exist_ok=True)
    dst_img.mkdir(parents=True, exist_ok=True)
    dst_key.mkdir(parents=True, exist_ok=True)

    for i, source_key in enumerate(key_files_path.glob('**/*'), 1):
        file_num = str(i).zfill(3)
        base_name = source_key.stem
        source_img = img_files_path / f"{base_name}.jpg"
        source_ocr = ocr_files_path / f"{base_name}.txt"
        shutil.copy(source_ocr, dst_ocr / f"{file_num}.csv")
        shutil.copy(source_img, dst_img / f"{file_num}.jpg")
        shutil.copy(source_key, dst_key / f"{file_num}.json")


if __name__ == '__main__':
    # These files can be downloaded here
    # https://rrc.cvc.uab.es/?ch=13&com=downloads

    generate_training_set()
    generate_test_set()