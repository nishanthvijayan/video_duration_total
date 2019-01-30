#!/usr/bin/env python

import os
import vlc
import argparse

ALLOWED_VIDEO_FORMATS = ('.mp4', '.avi', '.mov', '.mpg', '.vlc', '.mkv', '.webm')


def get_duration(filename):
    """
    Extract the duration (in seconds) of a media file
    """
    m = vlc.Media(filename)
    m.parse()
    dur_in_seconds = m.get_duration() / 1000
    return dur_in_seconds


def calcuate_total_duration(root_dir):
    """
    Calculate the total duration of all videos in a given directory
    """
    total_duration_in_seconds = 0
    for dirName, subdirList, fileList in os.walk(root_dir):
        for fname in fileList:
            if fname.lower().endswith(ALLOWED_VIDEO_FORMATS):
                fileName = dirName + '/' + fname

                try:
                    total_duration_in_seconds += get_duration(fileName)
                except Exception as e:
                    print "Error reading " + fileName

    total_duration_in_minutes = total_duration_in_seconds / 60
    total_duration_in_hrs = total_duration_in_minutes / 60
    print ('Total Duration of video files in  '
           + root_dir + ' = '
           + str(total_duration_in_hrs) + " hours , "
           + str(total_duration_in_minutes % 60) + ' minutes.'
    )

    return total_duration_in_minutes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate duration of all videos in a directory ")
    parser.add_argument("-d", "--dir", default=".", type=str, nargs='+', help="Input Directories")
    args = parser.parse_args()

    root_dir = args.dir[0]
    calcuate_total_duration(root_dir.encode('utf-8'))
