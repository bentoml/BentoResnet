import bentoml

MODEL_ID = "microsoft/resnet-50"
BENTO_MODEL_TAG = "resnet-50"

def import_model(model_id, bento_model_tag):

    import torch
    from transformers import AutoImageProcessor, ResNetForImageClassification

    model = ResNetForImageClassification.from_pretrained(
        model_id,
        low_cpu_mem_usage=True,
    )
    processor = AutoImageProcessor.from_pretrained(model_id)

    with bentoml.models.create(bento_model_tag) as bento_model_ref:
        model.save_pretrained(bento_model_ref.path_of("model"))
        processor.save_pretrained(bento_model_ref.path_of("processor"))


if __name__ == "__main__":
    import_model(MODEL_ID, BENTO_MODEL_TAG)    
