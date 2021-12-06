FROM ubuntu:latest
RUN apt-get update && \
         DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y python3.9 python3-pip python3.9-dev
RUN  pip3 install aliyun-python-sdk-core aliyun-python-sdk-ecs flask 
ADD SendSMS.py /
CMD ["python3","SendSMS.py"]



