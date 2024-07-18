@echo off
REM 获取批处理文件所在目录
set SCRIPT_DIR=%~dp0

REM 指定相对于批处理文件的路径
set VITE_PATH=%SCRIPT_DIR%tsfrontapp
set DJANGO_PATH=%SCRIPT_DIR%djangobackproject

REM 启动 Vite
echo Starting Vite...
start powershell -NoExit -Command "cd '%VITE_PATH%' ; npm start"

REM 启动 Django
echo Starting Django...
start powershell -NoExit -Command ".venv\\Scripts\\activate ; cd '%DJANGO_PATH%' ; python manage.py runserver"

echo Both servers have been started.