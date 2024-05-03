
![web_app testing badge](https://github.com/software-students-spring2024/5-final-project-spring-2024-metty/actions/workflows/web_app.yml/badge.svg)
![web_app docker image publish, digital ocean deploy badge](https://github.com/software-students-spring2024/5-final-project-spring-2024-metty/actions/workflows/dockeranddeploy.yml/badge.svg)

# DoroPomo

DoroPomo is a gamified Pomodoro web application designed to enhance productivity and time management skills. With DoroPomo, users embark on an exciting journey of focused work sessions, unlocking new levels and animations as they progress. Two types of users are catered for: guest users, who can access the default animation and utilize the Pomodoro timer, and logged-in users, who enjoy additional features such as multiple animations, data analysis insights, and level-based achievements.

Logged-in users can delve into their productivity patterns through the Data Analysis tab, where they can visualize their usage trends with informative graphs and statistics. DoroPomo encourages users to stay engaged and motivated by offering a diverse range of animations, making the journey towards enhanced productivity both enjoyable and rewarding.

![demo](images/doropomo.gif)

# Deployment

Check our deployed app [here](http://167.71.252.118:5000)!

# Dockerhub Images

[web_app image](https://hub.docker.com/r/teammetty4eva/web_app)

## Contributors

* [Shriya Kalakata](https://github.com/shriyakalakata)
* [Ahmet Ilten](https://github.com/iltenahmet)
* [Glenda Boeker](https://github.com/gboeker)
* [Amber Li](https://github.com/al6862)


# FOR DEVS:

## To build + run:

From the root dir, run

`docker compose up --build`

Check localhost:5000 to try the web app.

## To build + run db container if entering pipenv shell manually:

From the root dir, run

`docker run --name mongodb -d -p 27017:27017 mongo`

Then, make a .env with `MONGO_URI=mongodb://localhost:27017/` and `SECRET_KEY=dev` in the root dir. You can now `pipenv install` and `pipenv shell` in the web_app dir.

## To check code coverage:

Navigate to the `web_app` directory, and run `coverage run -m pytest` and then `coverage report -m`

## Figma file
https://www.figma.com/file/24LGaSUtQbYkMu7X7xB6Nf/doropomo?type=design&node-id=0-1&mode=design&t=YfX4QiaG4TQj6vn1-0
