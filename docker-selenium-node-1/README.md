## Docker image for Selenium Node

* [selenium](http://docs.seleniumhq.org/)
* Forked from https://github.com/lzhang/docker-selenium

## Install

Either git pull and build this docker image yourself, or pull down the version you need from the docker index.

```sh
$ sudo docker pull momer/docker-selenium-node:1.0.0
```
(note: Replace 1.0.0 with up-to-date version if any, check [DockerHub page](https://registry.hub.docker.com/u/momer/docker-selenium-node/tags/manage/) for more info about this image)


## Starting the container

This was designed to work with [MaestroNG](https://github.com/signalfuse/maestro-ng). 

```
  seleniumnode:
    image: momer/docker-selenium-node:1.0.0
    requires: [ seleniumhub ]
    env:
      SELENIUM_HUB_HOST: server1.my-host.com
    instances:
      ca2-selenium-node:
        ship: ca2
        ports: {seleniumnode: 5555}
        volumes:
          /var/log/supervisor/selenium_node: /opt/docker_volumes/selenium_node/log/supervisor
        limits:
          memory: 8g
        lifecycle:
          running: [{type: tcp, port: selenium}]
      ca3-selenium-node:
        ship: ca3
        ports: {seleniumnode: 5555}
        volumes:
          /var/log/supervisor/selenium_node: /opt/docker_volumes/selenium_node/log/supervisor
        limits:
          memory: 8g
        lifecycle:
          running: [{type: tcp, port: selenium}]
```


Alternatively, you can pass the necessary environment variables to `docker run` command to start the container. 

    SELENIUM_NODE_CONTAINER=$(sudo docker run -e "CONTAINER_HOST_ADDRESS=xxx.xx.xx.xx" -e "SELENIUM_HUB_HOST=xxx.xx.xx.xx" -p 5555:5555 -d momer/docker-selenium-node:1.0.0)

Selenium node is now available on port 5555 at the host and container.
