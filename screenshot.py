from PIL import Image
import face_recognition
import sys
import os

def process_image(image_path, padding=20):
    # 加载图片
    image = face_recognition.load_image_file(image_path)
    
    # 在图片中找到所有的人脸
    face_locations = face_recognition.face_locations(image)
    
    # 处理找到的每一张人脸
    for i, face_location in enumerate(face_locations):
        top, right, bottom, left = face_location
        
        # 扩大裁剪区域
        top = max(0, top - padding)
        right = min(image.shape[1], right + padding)
        bottom = min(image.shape[0], bottom + padding)
        left = max(0, left - padding)
        
        # 裁剪并转换为PIL图片
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        
        # 调整大小
        resized_image = pil_image.resize((300, 300))
        

         # 保存图片，避免覆盖原图
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        
        output_path = f"{base_name}_face_{i+1}.jpg"
        
        resized_image.save(output_path)
        
        print(f"Saved {output_path}")


if __name__ == "__main__":
    # if len(sys.argv) != 2:

    #     print("Usage: python script.py <image_path>")

    #     sys.exit(1)
    
    #image_path = sys.argv[1]

    image_path = './180.jpg'

    process_image(image_path, padding=200)
    
    print('ok')



