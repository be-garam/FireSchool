from ninja import NinjaAPI
from .models import School, SchoolData, SuggestedSchool, UserReport

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

        files_links = file_links + img_links
        if files_links:
            return files_links
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
                한국어나 영어로 부가 설명없이 아래의 양식으로 해당 학교를 처음 접한 입학예정자에게 학교를 소개하는데 도움이 될 정보들로 각 list에 값이 딱 3개만 들어갈 수 있도록 데이터를 얻어주세요.
                이때, keywords를 위한 각 elements들은 2단어 이하로 추출하고, urls는 https://로 시작하는 링크들만 추출해주세요.
                files는 pdf, hwp, jpg, png 파일들의 링크들을 우선순위로 두고 추출해주세요.
                양식:{"links":[], "files": [], "keywords":[]}
                """}
        ],
        "model": "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
    }

    # requests to open slm
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    # print(response.json())

    if response.status_code == 200:
        answer = response.json().get('choices')[0].get('message').get('content')
        print(answer)
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
            # files=extract_files(school.contents),
            files=json_data.get('files'),
            keywords=json_data.get('keywords')
        )
        school_data.save()

        return {"result": "school data extracted successfully"}

    else: 
        return {"result": "failed to get school data"}

# User chat with open slm
@api.post("/chat/completions")
# def chat_completions(request, chat: str, userid: str, school_name: str):
def chat_completions(request, chat: str, school_name: str):
    school = School.objects.get(name=school_name)

    # preparing requests data for open slm 
    url = "http://10.125.208.189:9241/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        'accept': 'application/json'
    }

    payload = {
        "messages": [
            {"role": "system", "content": school.contents + "Please respond in Korean"},
            {"role": "user", "content": chat}
        ],
        "model": "OpenBuddy/openbuddy-llama3-8b-v21.1-8k", 
        "max_tokens": 500,
    }

    # requests to open slm
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        answer = response.json().get('choices')[0].get('message').get('content')
        chatResponse = {
            # "id": userid,
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

# POST api to get user's suggestion and save it to database
@api.post("/user_suggest_school")
def user_suggest_school(request, user_name: str, school_name: str, school_link: str):
    
    suggestedSchool = SuggestedSchool.objects.create(
        user_name=user_name,
        school_name=school_name,
        school_link=school_link
    )
    suggestedSchool.save()

    return {"result": "school data suggested successfully"}

# User get suggested school data list
@api.get("/suggested_school_list")
def suggested_school_list(request):
    suggested_schools = SuggestedSchool.objects.all()
    suggested_schools = [{
        "user_name": suggested_school.user_name,
        "school_name": suggested_school.school_name,
        "school_link": suggested_school.school_link,
        "date_suggested": suggested_school.date_suggested
    } for suggested_school in suggested_schools]
    return suggested_schools

# POST api for User to report Error
@api.post("/user_report_error")
def user_report_error(request, school_name: str, error: str):
        
        userReport = UserReport.objects.create(
            school_name=school_name,
            error=error
        )
        userReport.save()
    
        return {"result": "error reported successfully"}
