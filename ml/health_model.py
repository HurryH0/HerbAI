"""
Plant-health perception model (stub).

Train OFF-device, export to TFLite, and load the .tflite on the Pi for inference.
This file sketches the interface; fill in once you have labelled frames in ml/data/.
"""

LABELS = ["healthy", "yellowing", "curling"]


def train(data_dir: str = "ml/data", epochs: int = 15):
    """Fine-tune a small pretrained backbone on labelled canopy frames.

    TODO:
      1. Load frames + labels.csv from data_dir.
      2. Transfer-learn (e.g. MobileNetV2, frozen base) -> 3-class head.
      3. Export to models/health.tflite.
    """
    raise NotImplementedError("add training once labelled data exists")


def predict(frame) -> str:
    """Return one of LABELS for a single canopy frame.

    Loads models/health.tflite via tflite-runtime at call time. Returns 'healthy' as a safe
    default until a model is trained.
    """
    # TODO: tflite-runtime Interpreter inference on `frame`.
    return "healthy"
