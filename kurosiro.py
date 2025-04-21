import os
from PIL import Image

def convert_downloaded_image_to_grayscale(filename, output_path="grayscale_output.jpg"):
    """
    Downloads 폴더에서 주어진 이름의 이미지 파일을 찾아 흑백으로 변환하여 지정된 경로에 저장합니다.

    Args:
        filename (str): 변환할 이미지 파일의 이름 (확장자 포함).
        output_path (str, optional): 흑백 이미지를 저장할 파일의 경로. 기본값은 "grayscale_output.jpg"입니다.
    """
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    image_path = os.path.join(download_folder, filename)

    try:
        img = Image.open(image_path)
        grayscale_img = img.convert("L")
        grayscale_img.save(output_path)
        print(f"'{filename}' 이미지를 흑백으로 변환하여 '{output_path}'에 저장했습니다.")
    except FileNotFoundError:
        print(f"오류: '{image_path}' 파일을 Downloads 폴더에서 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

# 변환하고 싶은 이미지 파일의 이름을 정확하게 입력하세요. (예: "my_photo.png")
image_file_name = "your_image.jpg"
output_file_path = "grayscale_downloaded.jpg" # 저장할 흑백 이미지 파일 이름 (경로를 포함할 수도 있습니다.)

convert_downloaded_image_to_grayscale(image_file_name, output_file_path)
