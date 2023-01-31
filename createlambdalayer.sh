#!/bin/bash

echo "Creating layer compatible with python version 3.9"
docker run -v "$PWD":/var/task "public.ecr.aws/sam/build-python3.9:latest" /bin/sh -c "pip install -r requirements.txt -t python/lib/python3.9/site-packages/; exit"
zip -r layer.zip python > /dev/null
rm -r python
echo "Done creating layer!"
ls -lah layer.zip
