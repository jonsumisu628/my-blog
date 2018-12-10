# my-blog Back-end

## Setup

Create file the `.env`

```sh
MYSQL_ROOT_PASSWORD=
MYSQL_USER=
MYSQL_PASSWORD=

# Option
```
check the `.env.sample`

### In case of Docker compose

#### start
```bash
$ docker-compose -f ./build-config/docker-compose-dev.yml up -d --build
```

#### build
```bash
# build
$ docker-compose -f ./build-config/docker-compose-dev.yml build
# up
$ docker-compose -f ./build-config/docker-compose-dev.yml up -d
# restart
$ docker-compose -f ./build-config/docker-compose-dev.yml restart
```

### In case of Host

1. virtualenv setup

- Not installed virtualenv

```bash
$ pip install virtualenv
$ virtualenv -p python3 virtualenv
```

- Installed virtualenv
```bash
$ virtualenv -p python3 virtualenv
```

2. Start virtualenv

```bash
$ source virtualenv/bin/activate
```

3. Install dependencies

```bash
$ pip install -r requirements.txt
```

- Exit virtualenv
```bash
$ deactivate
```

## Run AppSync-test Apprication

Run main.py
```
$ python3 main.py
```

## Development

### VSCode
1. set up virtualenv
2. create `.vscode/settings.json`

- Case: project root is `back-end`
```json
{
    "python.pythonPath": "./virtualenv/bin/python"
}
```

- Case: Project root is `my-blog`
```json
{
    "python.pythonPath": "./back-end/virtualenv/bin/python"
}
```

## Check source lint
```bash
$ flake8 *.py
```
