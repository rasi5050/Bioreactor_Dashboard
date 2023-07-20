# Bioreactor dashboard

## Introduction/Premise
This is a hobby project to create a web-based dashboard(Python & Dash) to visualize real-time process data originating from a bioreactors(simulated via containerized Postgres DB). 
This project also leverages advanced concepts like Containerization(Docker & Docker compose) and packaging applications using Python entry points

This project idea and skeleton is obtained from internet.

<img width="1512" alt="Screenshot 2023-07-20 at 19 06 36" src="https://github.com/rasi5050/Bioreactor_Dashboard/assets/12760472/bd67c91d-1d01-48f1-b1fe-b709db245a87">

## What all I have done?

● Built a Python-Dash interactive web-based data visualization application to monitor metrics like temperature, pH,
pressure, oxygen% of a Bioreactor streaming from Postgres DB.

● Stylized application using HTML and CSS, further Implemented interactive features for users to select the time
window and hot reloading.

● Configured application to run as python package automatically leveraging python entry points

● Containerized the application and Postgres DB and further leveraged Docker-compose to abstract and run the
application underneath.

## Whats used?

Python, Pandas, Dash, HTML, CSS, Docker, Docker-compose, Postgres 

## Functionality

The dashboard plots each of the metrics(Temperature, pH, Distilled Oxygen, and Pressure) over time.

The features include select time window along both axes or in box, double click to reset, auto-refresh the page, download plot as png, pan, zoom

## How to run?

(skip if you have it) install docker from https://docs.docker.com/engine/install/ 

`$ git clone https://github.com/rasi5050/Bioreactor_Dashboard.git`

`$ cd Bioreactor_Dashboard`

`$ docker-compose up`

Navigate your browser to http://localhost:8888/. That's it!

## Whats happening behind a.k.a Technical Details:

In the directory, you'll find a `Dockerfile` that defines the image the code will be copied into and installed in. Specifically, the source code will be installed into a Python 3.10 virtual environment as a package via pip, along with all dependencies specified in a `requirements.txt` file.

You'll also find a `compose.yaml` file that defines the container that'll be used to run the code. Specifically, to serve the web-based dashboard in a local browser at http://localhost:8888/, Docker is configured to start the container by executing `run-app`, the expected [entrypoint](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) for the application.

### The database

The data visualized will be in a Postgres database, also configured in `compose.yaml`. Credentials to access this database is provided in the following environment variables accessed through `local.env`:
- `POSTGRES_HOST` provides the host
- `POSTGRES_PORT` provides the port
- `POSTGRES_USER` provides the user
- `POSTGRES_PASSWORD` provides the password
- `POSTGRES_DB` provides the database

### The data

The tables in the database:
```
brx1=# \dt
                      List of relations
 Schema |           Name           | Type  |      Owner       
--------+--------------------------+-------+------------------
 public | CM_HAM_DO_AI1/Temp_value | table | process_trending
 public | CM_HAM_PH_AI1/pH_value   | table | process_trending
 public | CM_PID_DO/Process_DO     | table | process_trending
 public | CM_PRESSURE/Output       | table | process_trending
 ```

Each table has the same schema, like so:
```
brx1=# \d public."CM_HAM_DO_AI1/Temp_value"
                Table "public.CM_HAM_DO_AI1/Temp_value"
 Column |            Type             | Collation | Nullable | Default 
--------+-----------------------------+-----------+----------+---------
 time   | timestamp without time zone |           |          | 
 value  | double precision            |           |          | 
```

Each table contains the following data:
| Table                    | Name             | Units   |
|--------------------------|------------------|---------|
| CM_HAM_DO_AI1/Temp_value | Temperature      | Celsius |
| CM_HAM_PH_AI1/pH_value   | pH               | n/a     |
| CM_PID_DO/Process_DO     | Distilled Oxygen | %       |
| CM_PRESSURE/Output       | Pressure         | psi     |

## Screenshots

<img width="1512" alt="Screenshot 2023-07-20 at 19 06 36" src="https://github.com/rasi5050/Bioreactor_Dashboard/assets/12760472/010a12f6-8829-429a-a610-59c33f99ab75">
<img width="1512" alt="Screenshot 2023-07-20 at 19 08 25" src="https://github.com/rasi5050/Bioreactor_Dashboard/assets/12760472/f24a1b5d-5ae5-430a-9a03-6d20749ac64e">
<img width="1510" alt="Screenshot 2023-07-20 at 19 07 00" src="https://github.com/rasi5050/Bioreactor_Dashboard/assets/12760472/ec259424-dd91-456d-9627-a7f14ff35bc5">
<img width="1512" alt="Screenshot 2023-07-20 at 19 08 45" src="https://github.com/rasi5050/Bioreactor_Dashboard/assets/12760472/caf6b0d9-2370-440f-bd53-831da41c7f1e">




