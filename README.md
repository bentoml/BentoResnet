<div align="center">
    <h1 align="center">Serving a ResNet model with BentoML</h1>
</div>

ResNet (Residual Network) is a convolutional neural network that democratized the concepts of residual learning and skip connections. This is a BentoML example project, demonstrating how to build an image classification inference API server with a [ResNet model (ResNet-50 v1.5)](https://huggingface.co/microsoft/resnet-50) and BentoML.

See [here](https://github.com/bentoml/BentoML/tree/main/examples) for a full list of BentoML example projects.

## Install dependencies

```bash
git clone https://github.com/bentoml/BentoResnet.git
cd BentoResnet

# Recommend Python 3.11
pip install -r requirements.txt
```

## Run the BentoML Service

This repo demonstrates pulling the the model weights from Hugging Face and storing them in the BentoML model store. It allows you to gain full control over the model weights and leverage model loading acceleration during a container cold start. To download and store the model weights in the BentoML model store, run the `import_model.py` script.

```bash
python import_model.py
```

We have defined a BentoML Service in `service.py`. Run `bentoml serve` in your project directory to start the Service.

```bash
bentoml serve .

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
    result = client.classify(
        images=[
            Path("cat1.jpg"),
        ],
    )
```

## Deploy to BentoCloud

After the Service is ready, you can deploy the application to BentoCloud for better management and scalability. [Sign up](https://www.bentoml.com/) if you haven't got a BentoCloud account.

Make sure you have [logged in to BentoCloud](https://docs.bentoml.com/en/latest/bentocloud/how-tos/manage-access-token.html), then run the following command to deploy it.

```bash
bentoml deploy .
```

Once the application is up and running on BentoCloud, you can access it via the exposed URL.
