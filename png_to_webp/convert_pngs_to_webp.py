import glob
import os

from PIL import Image


def convert_pngs_to_webp(input_folder, output_folder):
    # 입력 폴더 내의 모든 PNG 파일 가져오기
    png_files = glob.glob(os.path.join(input_folder, "*.png"))

    for png_file in png_files:
        try:
            # 파일명과 확장자 분리
            file_name, ext = os.path.splitext(os.path.basename(png_file))

            # WebP로 변환된 파일 경로 생성
            output_file = os.path.join(output_folder, f"{file_name}.webp")

            # PNG 이미지 열기
            with Image.open(png_file) as image:
                # WebP로 변환 및 저장
                image.save(output_file, "webp", lossless=True)

            print(f"Successfully converted {png_file} to WebP format: {output_file}")
        except Exception as e:
            print(f"Error converting {png_file} to WebP format: {str(e)}")


# 변환할 PNG 파일이 있는 폴더 경로
sticker_name = "habit_007"
input_folder = f"./{sticker_name}"

# WebP로 변환된 파일을 저장할 폴더 경로
output_folder = input_folder + "_webp"

# output_folder가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    files = glob.glob(os.path.join(output_folder, "*"))
    for f in files:
        os.remove(f)

# PNG를 WebP로 변환
convert_pngs_to_webp(input_folder, output_folder)


def generate_item_image_query(output_folder):
    # 입력 폴더 내의 모든 WebP 파일 가져오기
    webp_files = glob.glob(os.path.join(output_folder, "*.webp"))
    # 파일명으로 오름차순 정렬
    webp_files.sort()
    pre_order = 0
    small_order = 0
    stic_order = 0
    source_id = 10002
    bucket = "dev-mooda-item"

    for webp_file in webp_files:
        filename = os.path.basename(webp_file)
        image_key = filename.split(".")[0]
        order = "null"
        # _pre_가 포함된 이미지
        if "_pre_" in filename:
            order = pre_order
            pre_order += 1
            image_type = 3
        elif "_stic_" in filename:
            order = stic_order
            stic_order += 1
            image_type = 4
        elif "_small_" in filename:
            order = small_order
            small_order += 1
            image_type = 5
        elif "_tag@" in filename:
            image_type = 1
        elif "_thumb@" in filename:
            image_type = 2

        print(
            f"INSERT INTO item_image (image_key, image_type, `order`, source_id, original_file_name, image_size, extension, bucket, upload_path, status, created_at, updated_at) VALUES ('{image_key}', {image_type}, {order}, {source_id}, '{filename}', 0.00, 'webp', '{bucket}', '{sticker_name}/{filename}', 'USE', now(), now());")


generate_item_image_query(output_folder)
