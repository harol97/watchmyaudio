# PROJECT: WHATCHMYAUDIO

# DEV ENVIRONMENT 

Please enter to backend o frontend directory and check README.md


# PROD ENVIRONMENT

At the moment We're using docker. so You're free of choise a differente way

1. Install docker if You don't have docker in your computer: [click here to read how install docker](https://docs.docker.com/desktop/)

2. execute as administrator

        docker compose up -d admin-frontend       


3. About it.

        You have a configure variables in docker-compose. Please check the file, por example:


        configure url (line 7): It's to database


        configure BASE_URL (line 17): It's to connect to backend (http://yourdomain/api). Please don't forget /api


        configure SOCKET_URL (line 18): It's to connect to backend socket (if you're deploy backend in other server so. SOCKET_URL and BASE_URL have a same domain)


        Also you can configure ports on docker-compose files. 



Please check documentation for more information:  [docker docs](https://docs.docker.com/compose/)
