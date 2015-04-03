from __future__ import print_function
import os
for root, dirs, files in os.walk("/home/vtbhat/Desktop/images"):
    for file in files:
        if file.endswith(".jpg"):
            print(os.path.join(root, file))
