from __future__ import print_function
import os
import json
path = os.walk("/home/vtbhat/visual-search/webui-flask/static/visual-search/images")
for root, dirs, files in path:
    for file in files:
        if file.endswith(".jpg"):
            print(os.path.join(root, file))
