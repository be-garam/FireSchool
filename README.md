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

## Task
- [ ] Organize user flow
- [ ] Study Docker content
- [ ] Remind Svelte kit tutorial
- [ ] A clear understanding of the API integration part → complete the test by attaching slm
- [ ] Write crawling code
- [ ] Extract the desired file from the crawling code
- [ ] Test whether the content can be checked based on the crawling data to slm
- [ ] Deployment through Docker
- [ ] Contemplation on handling cookies, sessions, etc.