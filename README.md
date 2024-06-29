# py-api

Python API

##### Setup
    # clone repo
    git clone https://github.com/scranth/py-api.git

    # install python
    pyenv local 3.12.4
    pyenv exec python -m venv .venv
    source .venv/bin/activate  (mac)

    # install requirements
    pip install -r requirements.txt

##### Use
    # start
    uvicorn src.main:app --reload

    # docs
    http://127.0.0.1:8000/docs

    # test
    pytest tests

    # format
    black src tests

    # lint
    pylint src tests

    # docker
    docker-compose up

### License

[The MIT License](http://opensource.org/licenses/MIT)
