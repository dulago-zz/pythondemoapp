FROM python:3

RUN mkdir /opt/python
COPY helloworld.py /opt/python/
RUN chmod +x /opt/python/helloworld.py

ENV DD_APM_ENABLED=true
ENV DATADOG_TRACE_ENABLED=true
ENV DD_LOGS_INJECTION=true
ENV DD_SERVICE=PythonApp
ENV DD_ENV=dev
ENV DD_VERSION=0.1
ENV DD_TRACE_ANALYTICS_ENABLED=true

RUN pip install flask
RUN pip install flask_restful
RUN pip install ddtrace 

WORKDIR /opt/python

EXPOSE 80

ENTRYPOINT [ "/bin/bash", "-c", "ddtrace-run python helloworld.py" ]