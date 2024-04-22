# DoroPomo

DoroPomo is a gamified Pomodoro web application designed to enhance productivity and time management skills. With DoroPomo, users embark on an exciting journey of focused work sessions, unlocking new levels and animations as they progress. Two types of users are catered for: guest users, who can access the default animation and utilize the Pomodoro timer, and logged-in users, who enjoy additional features such as multiple animations, data analysis insights, and level-based achievements.

Logged-in users can delve into their productivity patterns through the Data Analysis tab, where they can visualize their usage trends with informative graphs and statistics. DoroPomo encourages users to stay engaged and motivated by offering a diverse range of animations, making the journey towards enhanced productivity both enjoyable and rewarding.

# To build + run:

From the root dir, run

`docker compose up --build`

Check localhost:5000 to try the web app.

# Dockerhub Images

[web_app image](https://hub.docker.com/r/teammetty4eva/web_app)

[final_project image](https://hub.docker.com/r/teammetty4eva/final_project)

## Contributors

* [Shriya Kalakata](https://github.com/shriyakalakata)
* [Ahmet Ilten](https://github.com/iltenahmet)
* [Glenda Boeker](https://github.com/gboeker)
* [Amber Li](https://github.com/al6862)


# FOR DEVS:

## To build + run db container if entering pipenv shell manually:

`docker run --name mongodb -d -p 27017:27017`

Then, make a .env with `MONGO_URI=mongodb://localhost:27017/`.

## Figma file
https://www.figma.com/file/24LGaSUtQbYkMu7X7xB6Nf/doropomo?type=design&node-id=0-1&mode=design&t=YfX4QiaG4TQj6vn1-0