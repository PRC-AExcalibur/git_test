.PHONY: all debug clean 
include tools/Make.def
all:
	@mkdir -p build/tmpobjs build/$(NAME)
	# @rm -rf build/$(NAME)/include
	# @cp -r  include build/$(NAME)/include
	@rm -rf build/Make.def
	@cp tools/Make.def build/Make.def
	@python3 tools/makefile_build.py --mode=release --is_lib=n
	@make -C build all

debug:
	@mkdir -p build/tmpobjs build/$(NAME)
	# @rm -rf build/$(NAME)/include
	# @cp -r  include build/$(NAME)/include
	@rm -rf build/Make.def
	@cp tools/Make.def build/Make.def
	@python3 tools/makefile_build.py --mode=debug --is_lib=n
	@make -C build all

clean:
	@rm -rf build