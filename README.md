# Mini project for intern

## Requirements
* [Requirement](https://docs.google.com/document/d/1IzBBIlad8VPO_7FcaLlDki5X8g8EiyWcQfDRw4_ACaA/edit?usp=sharing)
* [QA](https://docs.google.com/spreadsheets/d/1r3qkfMrJ735s77rh9j_q9d6cG9pW6AobuXnzd21fJm4/edit?gid=1150971954#gid=1150971954)

## Example of .env file
`SECRET_KEY=django-insecure-56qfioulh#d1f!d1uylehsto)np57x9x+g!b1r1*+fuuuo$=(i`
`JWT_SECRET_CHAR_LEN=64`
`JWT_ALGO=HS256`
`JWT_EXP_SECOND=60`
`DB_ENGINE=django.db.backends.mysql`
`DB_NAME=mini_project`
`DB_USER=admin`
`DB_PASSWORD=...`
`DB_HOST=127.0.0.1`
`DB_PORT=3306`
`SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...`
`ICENTER_SLACK=http://127.0.0.1:8000/icenter/apis/integration/slack_proxy/`

## Set up
1. Pre-setup:
    1. Run `git clone https://github.com/uynvk/InternMiniProject.git`
    2. Install all required libs in project.
    3. Create file `.env` at `./InternMiniProject`
2. Set up database:
    1. Move to `./InternMiniProject`
    2. Modify DB variables in `.env` file
    3. Run `sudo docker compose up`
    4. Run `python manage.py migrate hire_center`
    5. Run `python manage.py migrate icenter`
3. Set up slack: Modify SLACK_WEBHOOK_URL in `.env` file
4. Set up JWT: Modify JWT variables in `.env` file
5. Run server
    1. Move to `./InternMiniProject/InternMiniProject`
    2. Run `python manage.py runserver`
