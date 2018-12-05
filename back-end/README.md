# my-blog Back-end

## Setup

Create file the `.env`

```sh

# Option
```
check the `.env.sample`

### In case of Docker

```bash
$ docker build -t my-blog ./
$ docker run -p 8080:80 -d -v $PWD:/back-end my-blog
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

## Check source lint
```bash
$ flake8 *.py
```
