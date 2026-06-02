# Deploy slides

```shell
docker run -d --name edu-csa -p 8002:1948 --restart unless-stopped -v $PWD/slides:/slides -v $PWD/fig:/slides/fig webpronl/reveal-md:latest
```

```text
server {
    listen 80;

        server_name csa.edu.swampbuds.me;

        location / {
                proxy_set_header   X-Forwarded-For $remote_addr;
                proxy_set_header   Host $http_host;
                proxy_pass         "http://127.0.0.1:8002";
                client_max_body_size 200M;
    }
}
```

```shell
systemctl restart nginx.service
```

```shell
sudo docker pull astefanutti/decktape
sudo docker pull sbtscala/scala-sbt:openjdk-8u342_1.8.0_3.2.1
sudo docker build --tag python-tools .

```
