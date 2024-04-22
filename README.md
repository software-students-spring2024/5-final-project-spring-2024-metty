# Final Project

An exercise to put to practice software development teamwork, subsystem communication, containers, deployment, and CI/CD pipelines. See [instructions](./instructions.md) for details.

# DoroPomo

DoroPomo is a gamified Pomodoro web application designed to enhance productivity and time management skills. With DoroPomo, users embark on an exciting journey of focused work sessions, unlocking new levels and animations as they progress. Two types of users are catered for: guest users, who can access the default animation and utilize the Pomodoro timer, and logged-in users, who enjoy additional features such as multiple animations, data analysis insights, and level-based achievements.

Logged-in users can delve into their productivity patterns through the Data Analysis tab, where they can visualize their usage trends with informative graphs and statistics. DoroPomo encourages users to stay engaged and motivated by offering a diverse range of animations, making the journey towards enhanced productivity both enjoyable and rewarding.

# To build + run:

From the root dir, run

`docker compose up --build`

Check localhost:5000 to try the web app.

# To build + run db container if entering pipenv shell manually:

`docker run --name mongodb -d -p 27017:27017`

Then, make a .env with `MONGO_URI=mongodb://localhost:27017/`.

## Contributors

* [Shriya Kalakata](https://github.com/shriyakalakata)
* [Ahmet Ilten](https://github.com/iltenahmet)
* [Glenda Boeker](https://github.com/gboeker)
* [Amber Li](https://github.com/al6862)