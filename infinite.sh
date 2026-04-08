#!/bin/bash

for i in {1..5}
do
  echo "Run $i"
  pytest tests/test_calculate_rebate.py
done