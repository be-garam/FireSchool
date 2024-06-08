# SurfSchool
web app for crawling school homepage and get information by chatting with GPT

## Prototype
- [prototype link](https://www.figma.com/proto/D1EF1mWfnYy6P35D4QXWyS/FireSchool?page-id=0%3A1&type=design&node-id=5-55&viewport=122%2C463%2C0.1&t=dSSh5TIK81uSF9LJ-1&scaling=contain&starting-point-node-id=1%3A3&mode=design)

# Installing what we need
## Svelte
``` terminal
$ conda install -c conda-forge nodejs=20
$ npm create svelte@latest frontend # Skeleton project, no type checking, no additional options
$ cd frontend
$ npm install
$ npx svelte-add@latest tailwindcss
$ npm intsall flowbite flowbite-svelte classnames @popperjs/core
$ npm run dev -- --host
```
- after setting like above, we need to update [tailwind.confg.cjs](frontend/tailwind.config.cjs)

## Django
### terminal
``` terminal
$ conda install django django-ninja
$ pip install django-cors-headers
$ django-admin startproject backend
$ cd backend
$ python manage.py startapp api
```

### SurfSchool/backend/settings.py
- INSTALLED_APPS에 api 추가
- django-cors-headers 설정 
- ko-kr setting, 등
``` python
# settings.py
INSTALLED_APPS = [
    ...,
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    ...,
    'corsheaders.middleware.CorsMiddleware',
    ...,
]

CORS_ALLOW_ALL_ORIGINS = True  # 개발 환경에서만 사용, 실제 배포 시에는 특정 도메인만 허용
```


## Tasks and todo 
- [x] Organize user flow
- [ ] Study Docker content
- [ ] Remind Svelte kit tutorial
- [ ] A clear understanding of the API integration part → complete the test by attaching slm
- [ ] Write crawling code
- [ ] Extract the desired file from the crawling code
- [ ] Test whether the content can be checked based on the crawling data to slm
- [ ] Deployment through Docker
- [ ] Contemplation on handling cookies, sessions, etc.
-----

### User and Data flow
-----
- Point) I'll never gather user's data
    - we need statistic data and need to limit user's flexibility
-----
1. input link in admin page
2. `f_1` crawl this link
3. `f_2_1` get link 
4. `f_2_2` get keywords
5. `f_2_3` get file link
6. `f_2_4` get "https://r.jina.ai/" prefix data
7. `f_3` store these to DB
8. User select link store in DB(change input field to select UI)
9. User get static data(link, keywords, file link)
10. `f_4` teach SLM to get information base on `f_2_4` data
    - founded way: we just need to give content with "role": "system"
11. `f_5` User ask SLM for new data and get answer for this