"""USB camera on the lead-screw mount; canopy imaging for plant-health assessment."""


class Camera:
    def capture(self):
        # TODO: cv2.VideoCapture(...).read() and return the frame.
        return None

    def assess(self, frame) -> str:
        """Return 'healthy' | 'yellowing' | 'curling'.

        At runtime this calls the TFLite perception model (see ../../ml). A safe default is
        returned until a model is trained.
        """
        # TODO: run ml/health_model inference on `frame`.
        return "healthy"
