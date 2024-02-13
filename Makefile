.PHONY: all install run clear

NAME = population distribution comparison 

SHELL := bash
python = python3

ifeq ($(OS),Windows_NT)
	python := python
endif

all:
	@echo 'population distribution comparison'

install:
	$(python) -m pip install $(pip_user_option) -r requirements.txt

run:
	$(python) main.py

clear:
	@rm -fr **/__pycache__
