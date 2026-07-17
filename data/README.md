# Data Directory

This directory contains all datasets used in RoadVision AI.

## Structure

- raw/       : Original downloaded datasets (never modified)
- interim/   : Temporary preprocessing outputs
- processed/ : Final datasets used for model training
- external/  : External metadata and supporting files

## Dataset

Version 1 uses the German Traffic Sign Recognition Benchmark (GTSRB).

The raw dataset must never be edited directly.
All preprocessing outputs should be generated into the `processed/` directory.
