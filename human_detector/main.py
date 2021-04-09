"""Entry point"""
import sys

from human_detector.HumanDetector import DetectHuman
from human_detector.utils import parse_args


def main(video_path, mode, haarcascade_mode):
    detection = DetectHuman(video_path, mode, haarcascade_mode)
    return detection.human_detection()


if __name__ == '__main__':
    ARGS = parse_args(args=sys.argv[1:])
    VIDEO_PATH = ARGS.video_path
    MODE = ARGS.mode
    HAARCASCADE_MODE = ARGS.haarcascade_mode
    main(VIDEO_PATH, MODE, HAARCASCADE_MODE)
