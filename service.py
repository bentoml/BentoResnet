import typing as t
import numpy as np
from PIL.Image import Image

import bentoml


MODEL_ID = "microsoft/resnet-50"

@bentoml.service(
    name="bentoresnet",
    traffic={
        "timeout": 300,
        "concurrency": 256,
    },
    resources={
        "gpu": 1,
        "gpu_type": "nvidia-tesla-t4",
    },
)
class Resnet:
    
    def __init__(self) -> None:
        from transformers import AutoImageProcessor, ResNetForImageClassification
        import torch
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = ResNetForImageClassification.from_pretrained(MODEL_ID).to(self.device)
        self.processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
        print("Model resnet loaded", "device:", self.device)

    @bentoml.api(batchable=True)
    async def classify(self, images: t.List[Image]) -> t.List[str]:
        '''
        Classify input images to labels
        '''
        import torch

        inputs = self.processor(images=images, return_tensors="pt").to(self.device)
        with torch.no_grad():
            logits = self.model(**inputs).logits

        labels = []
        for max_possible in logits.argmax(-1):
            label_id = max_possible.item()
            labels.append(self.model.config.id2label[label_id])

        return labels
