"""Project pipelines."""
from __future__ import annotations

from .pipelines.feature_engineering import feat_eng_pipeline_training, feat_eng_pipeline_inference
from .pipelines.training import create_training_pipeline
from .pipelines.inference import create_inference_pipeline
from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> dict[str, Pipeline]:
    feature_engineering_training = feat_eng_pipeline_training()
    feature_engineering_inference = feat_eng_pipeline_inference()
    training_pipeline = create_training_pipeline()
    inference_pipeline = create_inference_pipeline()

    return {
        "__default__": feature_engineering_training + training_pipeline,
        "training": feature_engineering_training + training_pipeline,
        "inference": feature_engineering_inference + inference_pipeline,
    }
