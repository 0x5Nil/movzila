#!/usr/bin/env python3

import glob, os, argparse, sys, shutil

current_dir=""
destination_dir=""
files_reg=""

def check_path_tail(s):
	return s.endswith('/')

def list_in_dir():
	os.chdir(current_dir)
	count = 1
	for file in glob.glob(files_reg):
		print(f"{count} - {file}")
		count = count + 1

	print(f"{'#' * (len(current_dir) *2)}")

def move_list():
	count = 0
	for file in glob.glob(files_reg):
		count = count + 1
		shutil.move(f"{current_dir}{file}", f"{destination_dir}{file}")
		print(f"[{count}] {current_dir}{file} moved to {destination_dir}{file}")

	print(f"{'#' * (len(current_dir) *2)}")
	print(f"{count} moved :)")
	print(f"from : {current_dir}")
	print(f"to : {destination_dir}")
	print(f"{'#' * (len(current_dir) *2)}")

parser = argparse.ArgumentParser(
                    prog = 'movzila',
                    description = 'A simple tool to move the content of a DIR to another path',
                    usage='%(prog)s [options]')
parser.add_argument("-c", "--current", action="store", type=str, help="full path of your current dir")
parser.add_argument("-d", "--dest", action="store", type=str, help="full path of your destination dir")
parser.add_argument("-r", "--regex", help="files regex format", default="*")
args = parser.parse_args()

if args.current and args.dest:
	if check_path_tail(args.current) and check_path_tail(args.dest):
		current_dir = args.current
		destination_dir = args.dest
		files_reg = args.regex
	else:
		print("Error: PATH must end with '/'")
		sys.exit(2)
	
	print(f"{'*' * (len(current_dir) *2)}")
	print("Current DIR: ", current_dir)
	print("Destination DIR: ", destination_dir)
	print("RegEx: " ,files_reg)
	print(f"{'*' * (len(current_dir) *2)}")

	list_in_dir()

	move_list()

else:
	print("movzila.py -h ")
	sys.exit(2)