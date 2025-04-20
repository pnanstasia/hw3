# Homework 3: Containerization with Podman

Author: **Anastasiia Kucheruk**

## 📝 Description

In this homework I used podman to wrap applications into containers and run them.

## 🖥 Usage

### How to run the application

1. Clone the repository
2. Open folder *business*
3. To complete task 1, firstly build the image *podman build -t app .*
4. Then run *podman run -d -p 8000:8000 --name con app*
5. Now, you are able to check whether program works, for instance run *curl http://localhost:8000/* and *curl http://localhost:8000/health*
6. To complete task 2, run the code *podman-compose build* and after this 
*podman-compose up*
7. To clean the environment, first of all I stop containers - *podman stop (continer name)* 
8. Then, I clean everuthing *podman system prune -a*
9. Finaly, after the cleaning, I check disk space usage *podman system df*

### Results

