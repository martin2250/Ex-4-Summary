.PHONY: all show
BUILD = latexmk -pdf -interaction=nonstopmode -synctex=1
FILE = $(shell basename "$(CURDIR)")

all: $(FILE).pdf show

build: $(FILE).pdf

$(FILE).pdf: $(FILE).tex
	$(BUILD) $(FILE).tex

show:
	xdg-open $(FILE).pdf > /dev/null 2>&1 &

clean:
	git clean -Xf
