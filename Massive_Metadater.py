#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DEVELOPED BY Di0nJ@ck - February 2015 - v1.0
__author__      = 'Di0nj@ck'
__version__     = 'v1.0'
__last_update__ = 'Februrary 2015'

import os

from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset
from sys import argv, stderr, exit

def get_metadata(file_names):
    print ("- Analyzing files metadata.." + "\n")
    file_ = open('results.txt', 'w')
    file_extensions = [".3do",    ".3ds",    ".7z",    ".a",    ".ace",    ".aif",    ".aifc",    ".aiff",    ".ani",    ".apm",    ".asf",    ".au",    ".avi",    ".bin",    ".bmp",    ".bz2",    ".cab",    ".cda",    ".chm",    ".class",    ".cur",    ".deb",    ".der",    ".dll",    ".doc",    ".dot",    ".emf",    ".exe",    ".flv",    ".gif",    ".gz",    ".ico",    ".jar",    ".jpeg",    ".jpg",    ".laf",    ".lnk",    ".m4a",    ".m4b",    ".m4p",    ".m4v",    ".mar",    ".mid",    ".midi",    ".mka",    ".mkv",    ".mod",    ".mov",    ".mp1",    ".mp2",    ".mp3",    ".mp4",    ".mpa",    ".mpe",    ".mpeg",    ".mpg",    ".msi",    ".nst",    ".oct",    ".ocx",    ".odb",    ".odc",    ".odf",    ".odg",    ".odi",    ".odm",    ".odp",    ".ods",    ".odt",    ".ogg",    ".ogm",    ".otg",    ".otp",    ".ots",    ".ott",    ".pcf",    ".pcx",    ".pdf",    ".png",    ".pot",    ".pps",    ".ppt",    ".ppz",    ".psd",    ".ptm", ".pyo",    ".qt",    ".ra",    ".rar",    ".rm",    ".rpm",    ".s3m",    ".sd0",    ".snd",    ".so",    ".stc",    ".std",    ".sti",    ".stw",    ".swf",    ".sxc",    ".sxd",    ".sxg",    ".sxi",    ".sxm",    ".sxw",    ".tar",    ".tga",    ".tif",    ".tiff",    ".torrent",    ".ts",    ".ttf",    ".vob",    ".wav",    ".wma",    ".wmf",    ".wmv",    ".wow",    ".xcf",    ".xla",    ".xls",    ".xm",    ".zip",    ".zs1",    ".zs2",    ".zs3",    ".zs4",    ".zs5",    ".zs6",    ".zs7",    ".zs8",    ".zs9",    ".zst"]
    for filename in file_names:
        print ("- Extracting file metadata: " + filename + "\n")
        extension = os.path.splitext(filename)
        if extension[1] in file_extensions:
            print ("    * The file extension is: " + extension[1] + "\n")
            filename, realname = unicodeFilename(filename), filename
            file_.write('Name: ')
            file_.write(filename)
            file_.write('\n')
            parser = createParser(filename, realname)
            if not parser:
                print >>stderr, "Error, parsing file"
                exit(1)
            try:
                metadata = extractMetadata(parser)
            except Exception as e:
                print ("Error extracting file metadata: " + str(e))
                metadata = None
            if not metadata:
                print ("Metadata can not be extracted")
                exit(1)
            text = metadata.exportPlaintext()
            for line in text:
                file_.write(line)
                file_.write('\n')
            print ("    * Successfull metadata extraction" + "\n" + "\n")
        if not extension[1] in file_extensions:
            print ("    * File extension is unknown or not supported" + "\n" + "\n")
    return text
    file_.close()


def get_filenames(directory):
    file_names = []
    print ("- Recovering file list..." + "\n")
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_names.append(filename)
    return file_names  # Self-explanatory


#MAIN   
full_filenames = get_filenames("C:/Documents") #OR WHATEVER DIRECTORY YOU WANT TO PARSE FOR METADATA EXTRACTION
print ('- The following files have been found on the directory: ' + "\n")
for filename in full_filenames:
    print ("    * " + filename + "\n")
full_metadatas = get_metadata(full_filenames)
print ('- An output file with results has been successfully created, check it' + '\n')