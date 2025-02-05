# LLM Diary

<!--배지-->
![Apache 2.0][license-shield] <img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"/>

<p align="center">
 <img src="https://github.com/user-attachments/assets/ebe90fd9-00ee-4ded-bbbd-af419bcd822f" width=50%; >
</p>

<!--목차-->
# Table of Contents
- [[1] About the Project](#1-about-the-project)
  - [Features](#features)
  - [Technologies](#technologies)
- [[2] Getting Started](#2-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [[3] Usage](#3-usage)
- [[4] Contact](#4-contact)
- [[5] License](#5-license)

# [1] About the Project
거대 언어 모델(LLM)을 사용하여 사용자의 일기를 바탕으로 감정을 분석하고, 사용자에게 통계 및 맞춤형 상담을 제안하는 시스템. 
## Features 
* 강조하고싶은 **주요 기능**이나 **차별성 있는 특징**
 
## Technologies
 [Python](https://www.python.org) 3.10.0
 [Django](https://www.djangoproject.com/) 5.1.3
 [tailwindcss](https://tailwindcss.com/) 3.4.14
 [transformers](https://huggingface.co/docs/transformers/ko/index) 4.47.0
 
# [2] Getting Started

# [3] Usage
스크린샷, 코드 등을 통해 사용 방법과 사용 예제를 보여기. 사용 예제별로 h2 헤더로 나누어 설명

# [4] Contact
- 📧 [Jinhyeok, JEON](https://github.com/Jeon-Jinhyeok) aqwstn@gmail.com
- 📧 []()

# [5] License
Apache 2.0

---

## 주요 기능
### 사용자 기능
1. **일기 작성 및 저장**  
   사용자에게 자신의 감정을 기록할 수 있는 일기 작성 기능을 제공. 작성된 일기는 감정 분석 모델을 통해 분석되며, 분석 결과는 일기에 저장됨

2. **감정 통계 제공**  
   사용자는 지난 한 달 동안의 감정 데이터를 시각화된 막대그래프로 확인 가능하며 감정별로 기록된 횟수를 파악 가능

3. **맞춤형 상담 제안**  
   사용자의 감정 데이터를 기반으로 고객 지원 담당자가 상담을 제안할 수 있음. 또한 사용자가 상담사에게 상담을 신청할 수 있음

### 관리자 및 고객 지원 담당자 기능
1. **상담 제안**  
   관리자 또는 고객 지원 담당자는 특정 사용자의 감정을 분석한 데이터를 기반으로 "상담 제안" 버튼을 클릭하여 상담을 제안할 수 있습니다.

2. **감정 통계 관리**  
   모든 사용자에 대한 감정 데이터를 한눈에 파악할 수 있는 대시보드 제공. 사용자별 감정 빈도를 표시하며, 상담이 필요한 사용자에게 상담을 제안할 수 있습니다.

---

### 감정 분석
- **Model**: [koBERT](https://huggingface.co/monologg/kobert). 
- **Fine-tuning Dataset**:  [감성대화 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=86)
- **Emotion** : 분노, 슬픔, 불안, 상처, 당황, 기쁨

## 주요 기술
### 백엔드
- **Django**: 서버 및 데이터베이스 관리.
- **PostgreSQL**: 데이터 저장 및 관리.
- **Django ORM**: PostgreSQL과의 연동 및 데이터 처리.


<!--Url for Badges-->
[license-shield]: https://img.shields.io/badge/license-Apache%202.0-blue?style=round
[repository-size-shield]: https://img.shields.io/github/repo-size/dev-ujin/readme-template?labelColor=D8D8D8&color=BE81F7
[django-shield]: "https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white"
