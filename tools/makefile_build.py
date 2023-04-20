#coding=utf8

import os
import argparse

# mode: release/debug
parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default = "debug")
parser.add_argument('--is_lib', type=str, default = "n")
args = parser.parse_args()

os.chdir("src")

dirs = set()
files = []
for d, _, fs in os.walk("."):
    if d.startswith("./"):
        d = d[2 :]
    else:
        assert d == "."
    for f in fs:
        if f.endswith(".cpp"):
            if d != ".":
                dirs.add(d)
            files.append(("" if d == "." else d + "/") + f)

os.chdir("../build")

objs = []
for f in files:
    assert f.endswith(".cpp")
    objs.append("tmpobjs/" + f[: -3] + "o")

for i, f in enumerate(files):
    files[i] = "../src/" + f

mkf = open("Makefile", "w")
def write_line(line):
    mkf.write(line)
    mkf.write("\n")
write_line("""
.PHONY: all
include Make.def
all:""")

for d in dirs:
    write_line("\t@mkdir -p tmpobjs/%s" % d)

# choose mode: release/debug
# choose is_lib: y/n
mode_str = ""
if args.mode =="release":
    mode_str = "\t$(ZKHM_CXX_FLAGS_RELEASE)"

elif args.mode =="debug":
    mode_str = "\t$(ZKHM_CXX_FLAGS_DEBUG)"

for f, o in zip(files, objs):
    write_line("\t$(ZKHM_CXX) " + mode_str + " -I"+"$(NAME)/include -c -o %s %s" % (o, f))

if args.is_lib=="y":
    write_line("\t$(ZKHM_AR) $(ZKHM_AR_FLAGS) " + "$(NAME)/$(NAME)_lib.a %s" % " ".join(objs)+ " $(ZKHM_LIBS_FLAGS)")
else:
    write_line("\t$(ZKHM_CXX) $(ZKHM_LK_FLAGS) -o "+"$(NAME)/$(NAME)_" + args.mode + ".out %s" % " ".join(objs))

mkf.close()