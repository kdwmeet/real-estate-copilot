import base64
from PIL import Image
from io import BytesIO

def encode_image(uploaded_file):
    """이미지를 Base64 문자열로 변환"""
    try:
        image = Image.open(uploaded_file)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
    except Exception as e:
        print(f"인코딩 오류: {e}")
        return None
