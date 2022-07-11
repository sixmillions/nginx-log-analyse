FROM python:3.7-alpine3.13
RUN \
 apk add --no-cache tzdata && \
 cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
 echo "Asia/Shanghai" > /etc/timezone && \
 apk del tzdata && \
 apk add --no-cache postgresql-libs jq && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install psycopg2 --no-cache-dir && \
 apk --purge del .build-deps

COPY nginx-log-analyse.sh /calc/nginx-log-analyse.sh
COPY save-result-to-db.py /calc/save-result-to-db.py
# 运行分析脚本
CMD ["/bin/sh", "/calc/nginx-log-analyse.sh"]
