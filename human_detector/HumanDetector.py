import os
import cv2
from imutils.object_detection import non_max_suppression
import logging as lg
import numpy as np
import pkg_resources
from human_detector.config import OVERLAP_NMS, WINSTRIDE, PADDING, SCALE, MIN_NEIGHBORS
from human_detector.utils import get_url, close


class DetectHuman:

    def __init__(self, url_path, mode, haarcascade_mode=None):
        self.path = url_path
        self.mode = mode
        self.haarcascade_mode = haarcascade_mode

    def human_detection(self):
        """
        TO DO
        :return:
        """
        lg.info(self.haarcascade_mode)
        path_ = get_url(self.path)
        capture = cv2.VideoCapture(path_)
        while True:
            self.analyze_video(capture)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        close(capture)

    def analyze_video(self, capture):
        """
        TO DO
        :return:
        """
        frame, gray = self._prepare_video(capture)
        if self.mode == "HOG":
            boxes = self._launch_hog_analyzer(gray, nms=True)
        elif self.mode == "HAARCASCADE":
            boxes = self._launch_haarcascade_classifier(gray)
        self._set_boxes_on_video(boxes, frame)

    @staticmethod
    def _prepare_video(capture):
        """
        TO DO
        :param capture:
        :return:
        """
        ret, frame = capture.read()
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        return frame, gray

    @staticmethod
    def _set_boxes_on_video(boxes, frame):
        """
        TO DO
        :return:
        """
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('frame', frame)

    @staticmethod
    def _launch_hog_analyzer(gray, nms=False):
        """
        TO DO
        :param gray:
        :param nms:
        :return:
        """
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        boxes, weights = hog.detectMultiScale(gray, winStride=WINSTRIDE, padding=PADDING, scale=SCALE)
        if nms:
            return non_max_suppression(boxes, probs=None, overlapThresh=OVERLAP_NMS)
        return boxes

    def _launch_haarcascade_classifier(self, gray):
        if self.haarcascade_mode == 'fullbody':
            cascade_classifier = 'haarcascade_fullbody.xml'
        elif self.haarcascade_mode == 'face':
            cascade_classifier = 'haarcascade_frontalface_alt.xml'
        else:
            lg.info("Haarcascade mode is not correct : {0}".format(self.haarcascade_mode))
        path_model = pkg_resources.resource_filename(__name__,  os.path.join('resources', cascade_classifier))
        lg.info(path_model)
        detector = cv2.CascadeClassifier(path_model)
        return detector.detectMultiScale(gray, SCALE, MIN_NEIGHBORS)
