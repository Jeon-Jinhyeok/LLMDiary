# 📖 LLM Diary: 감정 분석 기반 다이어리 플랫폼

<!--배지-->
![Apache 2.0][license-shield] 
![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.1-lightblue?logo=django&logoColor=white&labelColor=green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql&logoColor=Blue&labelColor=Blue)
![TailwindCSS][tailwind-shield]
[![Hugging Face Model](https://img.shields.io/badge/HuggingFace-Model-yellow?logo=huggingface)](https://huggingface.co/xxhyeok/koBERT-emotion)
![Docker](https://img.shields.io/badge/Docker-Supported-blue?style=flat&logo=docker&logoColor=white&labelColor=black)

<!--Project LOGO-->
<p align="center">
 <img src="https://github.com/user-attachments/assets/ebe90fd9-00ee-4ded-bbbd-af419bcd822f" width=60%; >
</p>

<!--목차-->
## 📌 Table of Contents
- [🔍 About the Project](#-about-the-project)
- [🚀 Features](#-features)
- [💻 Technologies](#-technologies)
- [🛠 Getting Started](#-getting-started)
- [📌 Usage](#-usage)
- [📧 Contact](#-contact)
- [📜 License](#-license)

## 🔍 About the Project
거대 언어 모델(LLM)을 사용하여 사용자의 일기를 바탕으로 감정을 분석하고, 사용자에게 감정 통계 및 맞춤형 상담을 제안하는 시스템.

## 🚀 Features 
### 🏷️ROLE
- **User** 
- **Counselor**
- **Admin**
- **UserSupporter**

### 📊 Emotion Analsis
- **Model**: [koBERT](https://huggingface.co/monologg/kobert). 
- **Fine-tuning Dataset**:  [감성대화 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=86)
- **Emotion** : 분노, 슬픔, 불안, 상처, 당황, 기쁨

### 🏥 Counsel
- User can request a consultation, view connselor info
- Counselor can schedule, conduct, suggest consultations.

## 💻 Technologies
 - [Python](https://www.python.org) 3.10.0
 - [Django](https://www.djangoproject.com/) 5.1.3
 - [tailwindcss](https://tailwindcss.com/) 3.4.14
 - [transformers](https://huggingface.co/docs/transformers/ko/index) 4.47.0
 
## 🛠 Getting Started
### 0️⃣ Pre-requisite
The easiest way to start the LLMDiary is through **docker compose**. Before running this with the following commands, make sure that [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) are installed on your machine:


### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Jeon-Jinhyeok/LLMDiary.git
cd LLMDiary
```
### 2️⃣ Download the Model (Hugging Face)
```bash
sudo apt install git-lfs
git lfs clone https://huggingface.co/xxhyeok/koBERT-emotion
```
> 💡 **참고:** Hugging Face 모델 저장소에 접근하려면 SSH를 이용한 로그인 인증이 필요할 수 있습니다.
> [Hugging Face SSH Key 설정 가이드](https://huggingface.co/docs/hub/security-tokens) 참고
### 3️⃣ Configure Environment Variables
- setup.env파일 수정
 ```ini
 POSTGRES_DB=emotion_diary_db
 POSTGRES_USER=admin
 POSTGRES_PASSWORD=your-password
 POSTGRES_HOST=db
 POSTGRES_PORT=5432
 DJANGO_SECRET_KEY=your-secret-key
 DEBUG=False
 ALLOWED_HOSTS=*
 ```
- setup.env 파일 적용
 ```bash
 source ./setup.env
 ```

### 4️⃣ Run with Docker
```bash
docker compose up
```
### 5️⃣ Access the Web Interface
```plaintext
http://localhost:8000
```

## 📌 Usage

### Login Page
<img width="1310" alt="image" src="https://github.com/user-attachments/assets/ee90d531-a7ab-4ec9-9718-c9f5eb6128ba" />

---

### Diary List with Representative emotion
<img alt="image" src="https://github.com/user-attachments/assets/6fb9c4d8-390d-4ef0-a2e4-b312338900fe" />

---

### Diary Details

<img alt="image" src="https://github.com/user-attachments/assets/d681b426-edfa-45c2-8c28-2249c0099bbc" />

 - Diary Details with Result of Emotion Analysis and Recommended Action
 - You can edit or delete the written diary.
   
---

### Home
<img width="1646" alt="image" src="https://github.com/user-attachments/assets/3619b25a-4800-4308-81cb-81d17434863f" />

- You can check latest Diaries in Home
- You can check emotional statistics for one week.

## 📧 Contact
- [Jinhyeok, JEON](https://github.com/Jeon-Jinhyeok) - aqwstn@gmail.com
- [Donggeon, KIM](https://github.com/ehdrjs6831) - 

## 📜 License
Apache 2.0

---

<!--Url for Badges-->
[license-shield]: https://img.shields.io/badge/license-Apache%202.0-blue?style=round
[repository-size-shield]: https://img.shields.io/github/repo-size/dev-ujin/readme-template?labelColor=D8D8D8&color=BE81F7
[django-shield]: "https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"
[tailwind-shield]: https://img.shields.io/badge/TailwindCSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white
