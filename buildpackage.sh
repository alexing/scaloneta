#!/bin/bash
rm lambda_function.zip
cd bot
zip -r ../lambda_function.zip * -x "__pycache__*"
