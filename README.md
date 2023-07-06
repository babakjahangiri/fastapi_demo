# fastapi_demo



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!
 

## Run with Docker

```
docker build -t fastdemo:v1 .
```

```
docker run -it --rm -p 30000:30000 fastdemo:v1
```


## Run The Application


```
git clone https://gitlab.com/babak.uk/fastapi-demo.git 

uvicorn main:app --reload
```

### with python command
```
python main.py
```

### on cutome host & port
```
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

### with gunicorn
```
gunicorn -k uvicorn.workers.UvicornWorker -w 3 -b 0.0.0.0:30000 -t 360 --reload --access-logfile - main:app & gunicorn --access-logfile - -k --ca_certs ca_certs.txt uvicorn.workers.UvicornWorker -w 3 -b 0.0.0.0:8443 -t 360 --reload --access-logfile - main:app
```
## pipenv requirements


 _creating requirements.txt:_
```
pipenv requirements > requirements.txt
```

 _using requirements.txt:_
```
pipenv install -r requirements.txt
```


## API Documentation

 openAPI documentation url: http://127.0.0.1:8000/docs
 redoc documentation url: http://127.0.0.1:8000/redoc
