# Mini project for intern

## Requirements
* [Requirement](https://docs.google.com/document/d/1IzBBIlad8VPO_7FcaLlDki5X8g8EiyWcQfDRw4_ACaA/edit?usp=sharing)
* [QA](https://docs.google.com/spreadsheets/d/1r3qkfMrJ735s77rh9j_q9d6cG9pW6AobuXnzd21fJm4/edit?gid=1150971954#gid=1150971954)

## Set up
1. Pre-setup:
    1. Run `git clone https://github.com/uynvk/InternMiniProject.git`
    2. Install all required libs in project.
2. Set up database:
    1. Move to `./InternMiniProject`
    2. Modify DB variables in `.env` file
    3. Run `sudo docker compose up`
3. Set up slack: Modify SLACK_WEBHOOK_URL in `.env` file
4. Set up JWT: Modify JWT variables in `.env` file
5. Run server
    1. Move to `./InternMiniProject/InternMiniProject`
    2. Run `python manage.py runserver`
