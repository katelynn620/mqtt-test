#!/bin/bash
dd if=/dev/zero of=1mb bs=1024 count=1024
dd if=/dev/zero of=10mb bs=1024 count=10240
dd if=/dev/zero of=100mb bs=1024 count=102400