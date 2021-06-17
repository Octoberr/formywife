
FROM python:3.7.10


LABEL Name=adenupload Version=0.0.1

COPY ./requirements.txt /home/data-upload/
WORKDIR /home/data-upload


# Using pip:
# 升级pip
RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
# 安装本地的
RUN pip install ./resource/packages/commonbaby*.whl -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN pip install -r ./resource/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

CMD ["python", "start.py"]