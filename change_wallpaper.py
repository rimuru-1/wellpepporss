import ctypes
import os

def change_wallpaper(image_path):
    # التأكد من أن الصورة موجودة في المسار المحدد
    if not os.path.exists(image_path):
        print("مسار الصورة غير صحيح.")
        return
    
    # استخدام مكتبة ctypes لاستدعاء دالة تغيير الخلفية في نظام Windows
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    print("تم تغيير الخلفية بنجاح.")

# المسار الكامل للصورة التي تريد تعيينها كخلفية
image_path = r"C:\path\to\your\image.jpg"
change_wallpaper(image_path)
