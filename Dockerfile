FROM python:3.13

WORKDIR /precioluzhoy 
COPY . .
ENV VIRTUAL_ENV=/precioluzhoy/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.13 -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN reflex init

#It was hard to get this two lines right
ENV DB_URL="sqlite:///reflex.db"


CMD reflex db init && reflex db makemigrations && reflex db migrate && reflex run --env prod --backend-only

#CMD reflex db init && reflex db makemigrations && reflex db migrate && reflex run --env prod --backend-only

#CMD ["reflex", "run", "--env", "prod", "--backend-only"]