import cv2
import logging as lg
import numpy as np
from human_detector.config import HOG_INITIALIZATION_MODE
from human_detector.utils import get_url, close


class DetectHuman:

    def __init__(self, url_path, mode):
        self.path = url_path
        self.mode = mode

    def human_detection(self):
        """
        TO DO
        :return:
        """
        if self.mode == "HOG":
            self.compute_hog()
        else:
            print("TO DO")

    def compute_hog(self):
        model = self._initialize_hog(HOG_INITIALIZATION_MODE)
        path_ = get_url(self.path)
        capture = cv2.VideoCapture(path_)
        while True:
            self._launch_hog_analyzer(capture, model)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        close(capture)

    @staticmethod
    def _initialize_hog(initalization_mode: str) -> cv2.HOGDescriptor:
        hog = cv2.HOGDescriptor()
        if initalization_mode == "standard":
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            return hog
        else:
            lg.info("TO DO")

    @staticmethod
    def _launch_hog_analyzer(capture, model):
        """
        TO DO
        :param capture:
        :param model:
        :return:
        """
        lg.info(type(model))
        ret, frame = capture.read()
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        boxes, weights = model.detectMultiScale(gray, winStride=(8, 8))
        boxes_ = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        [cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2) for (xA, yA, xB, yB) in boxes_]
        cv2.imshow('frame', frame)
