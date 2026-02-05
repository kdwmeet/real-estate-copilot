from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from app.config import MODEL_NAME, SYSTEM_PROMPT
from app.utils import encode_image

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_description(uploaded_file, property_type, info_text):
    """매물 사진과 정보를 받아 마케팅 문구 JSON 생성"""
    base64_image = encode_image(uploaded_file)
    if not base64_image:
        return {"error": "이미지 처리 실패"}
    
    try:
        # 사용자 입력 정보 구성
        user_content = f"""
        [매물 정보]
        - 유형: {property_type}
        - 추가 특징: {info_text}
        
        위 정보와 이 사진을 결합해서 홍보 글을 써줘.
        """

        response = client.chat.completions.create(
            model = MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": [
                    {"type": "text", "text": user_content},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]}
            ],
            reasoning_effort="medium",
            response_format={"type": "json_object"}                
        )
        
        result_json = json.loads(response.choices[0].message.content)
        return result_json
    except Exception as e:
        return {"error": f"생성 중 오류 발생: {str(e)}"}