from ninja import NinjaAPI
from .models import School, SchoolData

import requests
import json


api = NinjaAPI()

# POST api to get link and archieve response of link's body to database
@api.post("/get_school")
def get_school(request, school_name: str, school_link: str):
    
    # requests from school_link(using r.jina.ai)
    def get_r_jina_response(school_link):
        response = requests.get("https://r.jina.ai/" + school_link)
        response_body = response.text
        return response_body

    # save the response_body to database(models.School)

    # check if school_name already exists
    school = School.objects.filter(name=school_name)
    
    if school.exists():
        school = school.first()
        school.urls.append(school_link)
        school.contents += get_r_jina_response(school_link)
        school.save()

        return {"result": "school data updated successfully"}

    else:
        school = School.objects.create(
            name=school_name, 
            urls=[school_link],
            contents=get_r_jina_response(school_link)
        )
        school.save()

        return {"result": "school data created successfully"}

# extract datas(link, files, keywords) from school contents
@api.post("/get_school_data")
def get_school_data(request, school_name: str):
    school = School.objects.get(name=school_name)

    # preparing requests data for open slm 
    url = "http://10.125.208.189:9241/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {"role": "system", "content": school.contents},
            {"role": "api", "content": """
                다른 부가 설명없이 아래의 양식대로 입학예정자에게 도움이 될 정보들로 각 list에 3개의 값이 들어갈 수 있도록 데이터를 얻어줘
                이때, keywords를 위한 각 elements들은 2단어 이하로 추출하고, files는 pdf 파일이 가장 우선이고, 그외 파일의 경우에는 해당 file의 url로 저장해줘
                양식:{"links":[], "files":[], "keywords":[]}
                """}
        ],
        "model": "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
    }

    # requests to open slm
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        answer = response.json().get('choices')[0].get('message').get('content')

        # converting the response to a json
        json_string = answer
        # Clean up the string (remove the '</content>' tag)
        clean_json_string = json_string.replace("</content>", "").strip()
        # Convert the cleaned JSON string to a Python dictionary
        json_data = json.loads(clean_json_string)

        # save the response_body to database(models.SchoolData)
        school_data = SchoolData.objects.create(
            school=school,
            links=json_data.get('links'),
            files=json_data.get('files'),
            keywords=json_data.get('keywords')
        )
        school_data.save()

        return {"result": "school data extracted successfully"}

    else: 
        return {"result": "failed to get school data"}



    