"""
Argument parser
"""
import argparse

import cv2
import pafy


def create_parser():
    """
    Parser
    :return: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--video_path',
        help='Video to process',
        required=True
    )
    parser.add_argument(
        '--mode',
        help='Define which algo to use'
    )
    parser.add_argument(
        '--haarcascade_mode',
        help='Define which pre trained cascade classifier you want to use'
    )
    return parser


def parse_args(args):
    """
    Parse arguments
    :param args: raw args
    :return: Parsed arguments
    """
    parser = create_parser()
    return parser.parse_args(args=args)


def get_url(path: str) -> str:
    """
    TO DO
    :param path:
    :return:
    """
    return pafy.new(path).getbest().url


def close(capture):
    """
    Close capture and windows
    :return:
    """
    capture.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)
