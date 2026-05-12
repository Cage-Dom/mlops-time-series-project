"""Project pipelines."""
from __future__ import annotations

from .pipelines.feature_engineering import create_feature_engineering_pipeline
from .pipelines.training import create_training_pipeline
from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> dict[str, Pipeline]:
    feature_engineering_pipeline = create_feature_engineering_pipeline()
    training_pipeline = create_training_pipeline()

    return {
        "__default__": feature_engineering_pipeline + training_pipeline,
        "feature_engineering": feature_engineering_pipeline,
        "training": feature_engineering_pipeline + training_pipeline,
    }
