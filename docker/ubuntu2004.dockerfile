FROM ubuntu:20.04

RUN apt update && apt install -y \
	build-essential \
	python3-pip

RUN pip3 install \
	cmake \
	conan

# TODO: Precache Conan dependencies?
