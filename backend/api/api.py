from ninja import NinjaAPI
from .models import School, SchoolData

import requests
import json
import re 


api = NinjaAPI()

# POST api to get link and archieve response of link's body to database
@api.post("/cms_get_school")
def cms_get_school(request, school_name: str, school_link: str):
    
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
@api.post("/cms_get_school_data")
def cms_get_school_data(request, school_name: str):
    school = School.objects.get(name=school_name)

    def extract_files(contents):
        # want to extract files' links with "https://~.pdf" or .jpg, .hwp format
        pattern = r"https://[^\s]+?\.(pdf|hwp)"

        # 내용에서 모든 매칭되는 링크 찾기
        file_links = re.findall(pattern, contents)

        if len(file_links) <= 3:
            i_pattern = r"https://[^\s]+?\.(jpg|png)"
            img_links = re.findall(i_pattern, contents)

        links = file_links + img_links
        if links:
            return links
        else: 
            return []

    # preparing requests data for open slm 
    url = "http://10.125.208.189:9241/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {"role": "system", "content": school.contents},
            {"role": "api", "content": """
                다른 부가 설명없이 아래의 양식대로 입학예정자에게 도움이 될 정보들로 각 list에 값이 딱 3개만 들어갈 수 있도록 데이터를 얻어주세요.
                이때, keywords를 위한 각 elements들은 2단어 이하로 추출하고, files는 pdf 파일이 가장 우선이고, 그외 파일의 경우에는 해당 file의 url로 저장해줘
                양식:{"links":[], "keywords":[]}
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
            files=extract_files(school.contents),
            keywords=json_data.get('keywords')
        )
        school_data.save()

        return {"result": "school data extracted successfully"}

    else: 
        return {"result": "failed to get school data"}

# User chat with open slm
@api.post("/chat/completions")
def chat_completions(request, chat: str, userid: str, school_name: str):
    school = School.objects.get(name=school_name)

    # preparing requests data for open slm 
    url = "http://10.125.208.189:9241/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        'accept': 'application/json'
    }

    payload = {
        "messages": [
            {"role": "system", "content": school.contents},
            {"role": "user", "content": chat}
        ],
        "model": "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
    }

    # requests to open slm
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        answer = response.json().get('choices')[0].get('message').get('content')
        chatResponse = {
            "id": userid,
            "speaker": "bot",
            "message": answer,
        }
        return chatResponse

# User get school's name from School
@api.get("/school_list")
def school_list(request):
    schools = School.objects.all()
    # want to return only school names
    schools = [school.name for school in schools]
    return schools

# User get school data
@api.post("/school_data")
def school_data(request, school_name: str):
    school = School.objects.get(name=school_name)
    school_data = SchoolData.objects.filter(school=school)

    if school_data.exists():
        school_data = school_data.last()
        return {
            "links": school_data.links,
            "files": school_data.files,
            "keywords": school_data.keywords
        }
    else:
        return {"result": "school data not found"}