#!/usr/bin/env python3
import os
import subprocess
import sys
import uuid

def die_usage():
	print("Usage: {prg} filterprog [arg ... -- ] file".format(prg=sys.argv[0]), file=sys.stderr)
	sys.exit(1)

def do_filter(prog,filename):
	# first run the equivalent of 'prog < filename > tmp'
	fin = open(filename, "rb")

	# make sure the tmp file is created on the same file system as the original
	d,f = os.path.split(filename)
	tmpname = os.path.join(d, "%s.%s.tmp" % (f, uuid.uuid4()))
	fout = open(tmpname, "wb")

	p = subprocess.Popen(prog, stdin=fin, stdout=fout)
	p.communicate()
	if p.returncode != 0: sys.exit(1)
	fin.close()
	fout.close()

	# Now move the filtered file in place.
	# Note: on win, atomic rename apparently isn't possible;
	# because dst already exists, this code will raise.
	os.rename(tmpname, filename)

def do():
	args = sys.argv[1:]
	if len(args) < 2: die_usage()
	if len(args) == 2:
		opt_filterprog = [args[0]]
		opt_file = args[1]
	else:
		if args[-2] != '--': die_usage()
		opt_filterprog = args[:-2]
		opt_file = args[-1]

	do_filter(opt_filterprog, opt_file)

do()
