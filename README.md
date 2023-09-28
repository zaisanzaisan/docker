# Hw3_Docker_Base

docker build . --tag=python_app:v1<br>
docker run -d -p 7773:8000 python_app:v1<br>
<br>
docker run -d -p 7001:8000 --name=pyapplepenv1 python_app:v1 - run by name<br>
docker start pyapplepenv1 - by name<br>
