#!/bin/bash
cd bot
zip -r ../lambda_function.zip * -x "__pycache__*"
