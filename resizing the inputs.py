#!/usr/bin/env python
# coding: utf-8

# In[14]:


from PIL import Image
import os


# In[15]:


input_folder = 'C:/Users/ayzeg/Desktop/merged dataset/input'  # مسیر پوشه ورودی
output_folder = 'C:/Users/ayzeg/Desktop/merged dataset/input resized'  # مسیر پوشه خروجی
size = (256, 256)  # اندازه جدید عکس‌ها


# In[16]:


# ایجاد پوشه خروجی اگر وجود نداشته باشد
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# In[17]:


# بررسی فایل‌های موجود در پوشه ورودی
for file_name in os.listdir(input_folder):
    # اگر فایل یک عکس باشد، آن را باز کرده و سپس ساز آن را به اندازه جدید تغییر دهید و در پوشه خروجی ذخیره کنید
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
        with Image.open(os.path.join(input_folder, file_name)) as img:
            img = img.resize(size)
            output_path = os.path.join(output_folder, file_name)
            img.save(output_path)


# In[ ]:




