Установка
Предварительные требования
Python 3.8 или выше
Docker (если используется Docker для развертывания)


**Использование виртуальной среды**


1. Поднять виртуальную среду
python3 -m venv venv
source venv/bin/activate

2. Идете в директорию source и пишите эту команду для установки всех зависимостей
pip install -r requirements.txt


**Использование Docker (Debian Linux)**


1. Установите Docker и Docker Compose:


sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Добавьте репозиторий в источники Apt:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


2. Проверьте установку Docker Compose:
   docker-compose --version

   
**Использование**


1. Запуск/Остановка контейнеров:
   # Запустить контейнеры
docker-compose up --build

# Остановить контейнеры
docker-compose down


2. Дополнительные команды Docker:
# Остановить все контейнеры
docker stop $(docker ps -a -q)

# Удалить все остановленные контейнеры
docker rm -f $(docker ps -aq)

# Удалить все образы
docker rmi $(docker images -q)

# Запустить контейнеры в фоновом режиме
docker-compose up --d

# Запустить контейнеры с выводом логов
docker-compose up --build





