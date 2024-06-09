import requests
import json

system_content = """
Title: 카이스트 의과학대학원

URL Source: https://gsmse.kaist.ac.kr/pages/sub/sub0201

Markdown Content:
#### 입학 전형

**전형 Timeline**

*   ![Image 1](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/i_04.png)
    
    온라인 원서접수
    
*   ![Image 2](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/i_05.png)
    
    1단계 서류전형
    
*   ![Image 3](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/i_06.png)
    
    2단계 면접전형  
    (인성/논문)
    
*   ![Image 4](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/i_07.png)
    
    최종 합격자 발표
    

**모집전형 및 일정**

| 구 분 | 봄학기(1차) 모집 | 가을학기 모집 |
| --- | --- | --- |
| 원서접수 | 7월 초 | 4월 초 |
| 서류전형 | 8월 초 | 5월 초 |
| 서류전형 합격자 발표 | 8월 중순 | 5월 중순 |
| 면접전형 | 8월 말 | 5월 말 |
| 최종합격자 발표 | 9월 중순 | 6월 중순 |
| 입학시기 | 다음해 3월 | 당해 9월 |

※ 학과 사정에 따라 모집 시기는 변동될 수 있음

**모집분야**

| 모집분야 | 학생구분별 모집여부 |
| --- | --- |
| 국비 장학생 | KAIST 장학생 | 일반 장학생 |
| --- | --- | --- |
| 석·박사통합과정 | O | O | O |
| 박사과정 | O | O | O |

**지원자격**

 
| 모집과정 | 석·박사통합과정 | 박사과정 |
| --- | --- | --- |
| 의사과학자과정 | 학사학위 취득(예정)자로서 의사면허증, 치과의사면허증 또는 한의사면허증 취득(예정)자 | 석사학위 취득(예정)자로서 의사면허증, 치과의사면허증 또는 한의사면허증 취득(예정)자 (석사과정의 전공은 제한 없음) |
| 의과학자과정 | 이공계 분야 학사학위 취득(예정)자 (약학,수의학 전공자 포함) | 이공계 분야 석사학위 취득(예정)자 (약학, 수의학 전공자 포함) |

**장학생 구분 및 혜택**

  
| 구 분 | 설 명 | 장학혜택 |
| --- | --- | --- |
| 국비 장학생 | 학생 교육경비의 일부를 정부출연금에 의하여 KAIST가 지원하는 학생 | 
*   **국비장학생**
    *   **석·박사통합과정**첫 1년은 석사학자금 지급 그 후는 박사학위과정과 동일
        
    *   **박사과정**1년차 ~ 4년차(8학기간) 조교수당 매월 지급
        
*   **수탁연구조사비**학생이 지도교수를 정한 후, 지도교수의 연구 프로젝트에 동참할 시에 소정의 수탁연구비 지급
    
*   **학생복지**입학생 전원 기숙사 입사 기회
    

 |
| KAIST 장학생 | 학생 교육경비의 일부를 KAIST에서 조성한 장학금, 외부출연기금, 교수연구비 등에서 지원하는 학생 |
| 일반 장학생 | 학생 교육경비의 전부 또는 일부를 산업체, 연구기관, 교육기관, 국가기관 등이 부담하는 학생 ※ 산업체, 연구기관 등 소속기관(직장)에 재직 중인 지원자는 국비나 KAIST장학생으로 지원할 수 없으며, 일반 장학생으로 지원하여야 함. (단, 소속기관이 있더라도 합격 후 입학 전까지 퇴직 예정인 자는 지원 가능함.) |

**온라인 입시설명회**

*   **의사과학자과정**
*   **의과학자과정**

[의과학대학원 공식 ![Image 5](https://gsmse.kaist.ac.kr/resources/wis-layout/images/sub/02/yotube_t.png) 바로가기](https://www.youtube.com/channel/UCCrlXfD_Fy_DxSo4lhxZTbQ)

"""

url = "http://10.125.208.189:9241/v1/chat/completions"
payload = {
    "messages": [
        {"role": "system", "content": system_content},
        {"role": "api", "content": """
            다른 부가 설명없이 아래의 양식대로 입학예정자에게 도움이 될 정보들로 각 list에 3개의 값이 들어갈 수 있도록 데이터를 얻어줘
            이때, keywords를 위한 각 elements들은 2단어 이하로 추출하고, files는 pdf 파일이 가장 우선이고, 그외 파일의 경우에는 해당 file의 url로 저장해줘
            양식:{"links":[], "files":[], "keywords":[]}
            """}
    ],
    "model": "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
}

headers = {
    "Content-Type": "application/json"
}


# def get_gpt_response(system_content):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": system_content},
#             {"role": "api", "content": """
#             다른 부가 설명없이 아래의 양식대로 각 list에 3개의 값이 들어갈 수 있도록 데이터를 얻어줘
#             양식:{"links":[], "files":[], "keywords":[]}
#             """}
#         ]
#     )
#     return response.choices[0].message['content']

# response = get_chatgpt_response(system_content, user_input)
# print(response)

response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response
print(response.status_code)
answer = response.json().get('choices')[0].get('message').get('content')

# converting the response to a json
json_string = answer
# Clean up the string (remove the '</content>' tag)
clean_json_string = json_string.replace("</content>", "").strip()

# Convert the cleaned JSON string to a Python dictionary
json_data = json.loads(clean_json_string)

# Print the dictionary
print(json_data)
