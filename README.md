## Prerequisites

- You have installed Python 3.8+ and `pip`. See the [Python downloads page](https://www.python.org/downloads/) to learn more.
- You have a basic understanding of key concepts in BentoML, such as Services. We recommend you read [Quickstart](https://docs.bentoml.com/en/1.2/get-started/quickstart.html) first.
- (Optional) We recommend you create a virtual environment for dependency isolation for this project. See the [Conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or the [Python documentation](https://docs.python.org/3/library/venv.html) for details.

## Install dependencies

```bash
git clone https://github.com/bentoml/BentoResnet.git
cd BentoResnet
pip install -r requirements.txt
```

## Run the BentoML Service

We have defined a BentoML Service in `service.py`. Run `bentoml serve` in your project directory to start the Service.

```bash
$ bentoml serve .

2024-01-08T09:07:28+0000 [INFO] [cli] Prometheus metrics for HTTP BentoServer from "service:Resnet" can be accessed at http://localhost:3000/metrics.
2024-01-08T09:07:28+0000 [INFO] [cli] Starting production HTTP BentoServer from "service:Resnet" listening on http://localhost:3000 (Press CTRL+C to quit)
Model resnet loaded device: cuda
```

The Service is accessible at [http://localhost:3000](http://localhost:3000/). You can interact with it using the Swagger UI or in other different ways:

CURL

```bash
curl -s \
     -X POST \
     -F 'images=@cat1.jpg' \
     http://localhost:3000/classify
```

Python client

```python
import bentoml
from pathlib import Path

with bentoml.SyncHTTPClient("http://localhost:3000") as client:
    result = client.encode_image(
        images=[
            Path("cat1.jpg"),
        ],
    )
```
