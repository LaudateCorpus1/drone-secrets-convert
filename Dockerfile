FROM python:3.6

RUN pip install oyaml

COPY convert.py /
COPY startup.sh /

ENTRYPOINT ["/startup.sh"]
