.PHONY: all show images
BUILD = latexmk -pdf -interaction=nonstopmode -synctex=1
FILE = $(shell basename "$(CURDIR)")

all: $(FILE).pdf show

build: $(FILE).pdf

$(FILE).pdf: $(FILE).tex images
	$(BUILD) $(FILE).tex

show:
	xdg-open $(FILE).pdf > /dev/null 2>&1 &

clean:
	git clean -Xf

images: img/energieniveaus.pdf

img/%.pdf: img/%.py
	./$< $@
