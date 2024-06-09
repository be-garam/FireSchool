from ninja import NinjaAPI
from .models import School

import requests


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