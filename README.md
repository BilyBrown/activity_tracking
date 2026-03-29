# activity_tracking
a little playthrough to build up an activity tracking app. This may include gps and a mobile app.

This whole project is a little play thing for me. I want to mess around a bit more with utilizing cloud servies as well as over-nerd-out my activity tracking. I would love to create an app on my phone where I can track gym workouts as well as backcountry ski, mountain bike, and running activities. Maybe even have a mobile app where you can see OpenMaps and your track - and collect GPS data.


## 2025.03.28
### Notes
Initial "Sprint" tasks / todo list for the coming weeks

#### Week 1: Infrastructure & Data Modelling
- [ ] Setup
  - [ ] Create AWS account
  - [ ] Launch micro RDS postgreSQL
  - [ ] Launch S3 bucket
- [ ] Schema Design
  - [ ] work out on paper/visualize
  - [ ] write the SQL DDL for tables
  - [ ] GitHub
    - [ ] Initialize the repo
    - [ ] add readme
    - [ ] add DB architecture diagram
- [ ] Get Data Ready
  - [ ] Download data from gsheets
  - [ ] Clean data
  - [ ] Try out little db on personal computer

**Week 1 Goal**
Successfully connect to your RDS from a local tool (DBeaver, or SQL in python) and upload data to RDS and a photo to S3

#### Week 2: The ETL Pipeline
Initially working off of laptop
- [ ] GPX Parser
  - [ ] Write a python script to convert CalTopo and OnX gpxs into PostGIS geometries
  - [ ] update RDS
- [ ] S3 Uploader
  - [ ] Use boto3 to upload photos
  - [ ] returns S3 key
  - [ ] Store S3 key in RDS
- [ ] Gym Workout Parser
  - [ ] python script to update RDS from gsheets
    - [ ] Eventually replace gsheets with native app
- [ ] Write up documentation on how to run data ingestion

**Week 2 Goal**
Bulk loads of tracks, gym workouts, and photos

#### Week 3: Report Application
Create a web-base dashboard/report using streamlit
- [ ] Connection
  - [ ] connect database to streamlit instance
  - [ ] connect S3 to streamlit instance
- [ ] Map Integration
- [ ] Photo Viewer

**Week 3 Goal**
A semi-functional local web app where selecting activities updates maps, or updates graphs/visuals, and tables/metrics

#### Week 4: Mobile App
Develop a mobile app to handle data ingestion
TBD

