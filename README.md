# Translating sentiment analyzer project

Using translation from original language to perform sentiment analysis with pretrained model

We use [translate and analyze](translate_and_analyze.ipynb) notebook as the main file, which utilizes other modules.

## Environment

This was ran with jupyter datascience notebook environment within docker-compose.

docker-compose.yaml

```
jupyterlab:
  image: "jupyter/datascience-notebook"
  ports:
    - "8890:8890"
  volumes:
    - ./data:/opt/app/data
    - ./notebooks:/opt/app/notebooks
  entrypoint: sh -c 'jupyter lab --ip=0.0.0.0 --port=8890 --no-browser --notebook-dir=/opt/app/ --allow-root'

```

