# Real Estate Copilot (부동산 매물 AI 카피라이터)

## 1. 프로젝트 개요

Real Estate Copilot은 공인중개사 및 부동산 마케터를 위한 PropTech 솔루션입니다. 매물 사진과 기본 정보를 입력하면, Vision AI 기술을 활용하여 매물의 특징을 분석하고 블로그, 직방, 다방 등 플랫폼에 즉시 게시 가능한 고품질의 홍보 문구를 자동으로 생성합니다.

기존의 수동적인 매물 설명 작성 방식에서 벗어나, OpenAI의 **gpt-5-mini** 모델을 통해 시각적 데이터(이미지)와 텍스트 데이터(스펙)를 결합한 멀티모달 분석을 수행합니다. 이를 통해 채광, 인테리어 상태, 공간감 등 사진에 담긴 비언어적 요소를 마케팅 언어로 변환하여 중개 업무의 효율성을 극대화합니다.

### 주요 기능
* **Vision 기반 매물 분석:** 이미지 내의 채광, 바닥재, 조망, 옵션 상태 등을 시각적으로 인식.
* **마케팅 카피라이팅:** 매물 유형(아파트, 원룸, 상가 등)에 최적화된 세일즈 멘트 자동 생성.
* **키워드 및 해시태그 추출:** 검색 노출(SEO)에 유리한 핵심 키워드와 해시태그 자동 추천.
* **사용자 맞춤형 입력:** 평수, 위치, 특이 사항 등 텍스트 정보를 프롬프트에 동적으로 반영.

## 2. 시스템 아키텍처

본 시스템은 멀티모달(Image+Text) 데이터를 처리하기 위한 파이프라인으로 구성됩니다.

1.  **Input Processing:** 사용자가 업로드한 매물 이미지를 RGB 포맷으로 정규화하고 Base64로 인코딩.
2.  **Context Injection:** 매물 유형, 평수, 추가 특징 등 텍스트 메타데이터를 시스템 프롬프트에 주입.
3.  **AI Inference:** **gpt-5-mini** 모델이 이미지와 텍스트를 종합적으로 분석하여 마케팅 포인트 도출.
4.  **Output Formatting:** 생성된 콘텐츠를 제목, 키워드, 본문, 해시태그로 구조화하여 UI에 렌더링.

## 3. 기술 스택

* **Language:** Python 3.10 이상
* **AI Model:** OpenAI **gpt-5-mini** (Vision capabilities)
* **Web Framework:** Streamlit
* **Image Processing:** Pillow (PIL)
* **Configuration:** python-dotenv

## 4. 프로젝트 구조

확장성을 고려하여 설정, 유틸리티, 생성 로직을 분리한 모듈형 구조입니다.

```text
real-estate-copilot/
├── .env                  # 환경 변수 (API Key)
├── requirements.txt      # 의존성 패키지 목록
├── main.py               # 애플리케이션 진입점 및 UI
└── app/                  # 백엔드 핵심 모듈
    ├── __init__.py
    ├── config.py         # 중개사 페르소나 및 분석 기준 프롬프트
    ├── utils.py          # 이미지 전처리 및 인코딩 헬퍼 함수
    └── generator.py      # OpenAI API 통신 및 데이터 생성 로직
```
요청하신 대로 이모티콘을 완전히 배제하고, gpt-5-mini 모델을 기반으로 작성된 전문적인 README.md 문서입니다.

아래 내용을 복사하여 프로젝트의 README.md 파일로 저장하십시오.

Markdown
# Real Estate Copilot (부동산 매물 AI 카피라이터)

## 1. 프로젝트 개요

Real Estate Copilot은 공인중개사 및 부동산 마케터를 위한 PropTech 솔루션입니다. 매물 사진과 기본 정보를 입력하면, Vision AI 기술을 활용하여 매물의 특징을 분석하고 블로그, 직방, 다방 등 플랫폼에 즉시 게시 가능한 고품질의 홍보 문구를 자동으로 생성합니다.

기존의 수동적인 매물 설명 작성 방식에서 벗어나, OpenAI의 **gpt-5-mini** 모델을 통해 시각적 데이터(이미지)와 텍스트 데이터(스펙)를 결합한 멀티모달 분석을 수행합니다. 이를 통해 채광, 인테리어 상태, 공간감 등 사진에 담긴 비언어적 요소를 마케팅 언어로 변환하여 중개 업무의 효율성을 극대화합니다.

### 주요 기능
* **Vision 기반 매물 분석:** 이미지 내의 채광, 바닥재, 조망, 옵션 상태 등을 시각적으로 인식.
* **마케팅 카피라이팅:** 매물 유형(아파트, 원룸, 상가 등)에 최적화된 세일즈 멘트 자동 생성.
* **키워드 및 해시태그 추출:** 검색 노출(SEO)에 유리한 핵심 키워드와 해시태그 자동 추천.
* **사용자 맞춤형 입력:** 평수, 위치, 특이 사항 등 텍스트 정보를 프롬프트에 동적으로 반영.

## 2. 시스템 아키텍처

본 시스템은 멀티모달(Image+Text) 데이터를 처리하기 위한 파이프라인으로 구성됩니다.

1.  **Input Processing:** 사용자가 업로드한 매물 이미지를 RGB 포맷으로 정규화하고 Base64로 인코딩.
2.  **Context Injection:** 매물 유형, 평수, 추가 특징 등 텍스트 메타데이터를 시스템 프롬프트에 주입.
3.  **AI Inference:** **gpt-5-mini** 모델이 이미지와 텍스트를 종합적으로 분석하여 마케팅 포인트 도출.
4.  **Output Formatting:** 생성된 콘텐츠를 제목, 키워드, 본문, 해시태그로 구조화하여 UI에 렌더링.

## 3. 기술 스택

* **Language:** Python 3.10 이상
* **AI Model:** OpenAI **gpt-5-mini** (Vision capabilities)
* **Web Framework:** Streamlit
* **Image Processing:** Pillow (PIL)
* **Configuration:** python-dotenv

## 4. 프로젝트 구조

확장성을 고려하여 설정, 유틸리티, 생성 로직을 분리한 모듈형 구조입니다.

```text
real-estate-copilot/
├── .env                  # 환경 변수 (API Key)
├── requirements.txt      # 의존성 패키지 목록
├── main.py               # 애플리케이션 진입점 및 UI
└── app/                  # 백엔드 핵심 모듈
    ├── __init__.py
    ├── config.py         # 중개사 페르소나 및 분석 기준 프롬프트
    ├── utils.py          # 이미지 전처리 및 인코딩 헬퍼 함수
    └── generator.py      # OpenAI API 통신 및 데이터 생성 로직
```
## 5. 설치 및 실행 가이드
###5.1. 사전 준비
Python 환경이 설치되어 있어야 합니다. 터미널에서 저장소를 복제하고 프로젝트 디렉토리로 이동하십시오.

```Bash
git clone [레포지토리 주소]
cd real-estate-copilot
```
### 5.2. 의존성 설치
필요한 라이브러리를 설치합니다.

```Bash
pip install -r requirements.txt
```
### 5.3. 환경 변수 설정
프로젝트 루트 경로에 .env 파일을 생성하고, Vision 기능을 지원하는 OpenAI API 키를 입력하십시오.

```Ini, TOML
OPENAI_API_KEY=sk-your-api-key-here
```
### 5.4. 실행
Streamlit 애플리케이션을 실행합니다.

```Bash
streamlit run main.py
```
## 6. 출력 데이터 사양 (JSON Schema)
AI 모델은 마케팅 문구를 다음과 같은 JSON 구조로 반환합니다. 이를 통해 블로그 자동 포스팅 봇이나 매물 관리 시스템(ERP)과 연동할 수 있습니다.

```JSON
{
  "title": "강남역 3분 거리, 채광 좋은 화이트톤 풀옵션 오피스텔 (즉시 입주)",
  "keywords": [
    "초역세권",
    "남향",
    "풀옵션",
    "신축급"
  ],
  "description": "현관을 들어서자마자 쏟아지는 햇살이 매력적인 남향 호실입니다. 화이트톤의 깔끔한 빌트인 가구가 설치되어 있어 공간 활용도가 매우 높습니다...",
  "hashtags": "#강남역오피스텔 #강남원룸 #풀옵션 #단기임대가능"
}
```

## 7. 실행 화면
<img width="639" height="628" alt="스크린샷 2026-02-05 120601" src="https://github.com/user-attachments/assets/0ce9b9a6-4a65-44d3-a07a-f309be3065fb" />

