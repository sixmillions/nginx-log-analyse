#!/bin/bash
# 分析hoozhi.net的nginx访问log

echo "运行分析脚本开始时间：`date '+%Y-%m-%d %H:%M:%S'`"
echo "定义nginx的access.log路径"
LOG_PATH=/var/log/nginx/access.log

echo "计算PV UV IP"
IP=$(awk '{print $1,$7}' ${LOG_PATH} | grep -E "^/$|html$|/detail/[0-9]+$|/policy/[0-9]+$" | awk '{print $1}' | sort -r | uniq -c | wc -l)
PV=$(awk '{print $7}' ${LOG_PATH} | grep -E "^/$|html$|/detail/[0-9]+$|/policy/[0-9]+$" | wc -l)
UV=$(awk '{print $NF}' ${LOG_PATH} | grep "ACCESS_GUID" | sort -r | uniq -c | wc -l)
echo "计算结果分别是：${PV} ${UV} ${IP}"

echo "分析结果保存数据库"
/usr/local/bin/python3 /calc/save-result-to-db.py ${PV} ${UV} ${IP}

echo "运行分析脚本结束时间：`date '+%Y-%m-%d %H:%M:%S'`"
