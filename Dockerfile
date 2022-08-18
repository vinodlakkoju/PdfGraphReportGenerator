#FROM public.ecr.aws/lambda/python:3.8
FROM python:3.7
MAINTAINER "vinod.lakk@gmail.com"
RUN mkdir /uploads
RUN mkdir /code
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir -p /root/.config/matplotlib
RUN echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc

CMD ["python", "/code/app.py"]
