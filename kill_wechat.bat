@echo off
set log_file=%~dp0log\kill_wechat_log.txt
date /T >>%log_file%
time /T >>%log_file%
tasklist /fi  "imagename eq wechat.exe" >>%log_file%
taskkill  /F /IM wechat.exe  >>%log_file%
