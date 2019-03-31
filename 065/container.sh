#!/usr/bin/env bash

docker run \
    --privileged \
    --rm \
    -it \
    --cpuset-cpus="1" \
    -v $(pwd):/src \
    centos:7 \
    /bin/bash
