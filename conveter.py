import xml.etree.ElementTree as ET
import sys



src = sys.argv[1]
des = sys.argv[2]

tree = ET.parse(src)

android_key = '{http://schemas.android.com/apk/res/android}'

root = tree.getroot()

height = root.attrib[android_key+'viewportHeight']
width = root.attrib[android_key+'viewportWidth']

print('height', height, 'width', width)

paths = []

for child in list(root):
    paths.append(child.attrib[android_key+'pathData'])


with open(des, 'w') as f:
    f.write('<?xml version="1.0" encoding="utf-8"?>\n')
    f.write('<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"\n')
    f.write(' viewBox="0 0 '+width+' '+height +
            '" style="enable-background:new 0 0 '+width+' '+height+';" xml:space="preserve">\n')
    f.write('<style type="text/css">\n')
    f.write('	.st0{fill:#333333;}\n')
    f.write('</style>\n<g>\n')

    for path in paths:
        f.write('<path class="st0" d="'+path+'"/>\n')

    f.write('</g>\n</svg>\n')

    f.flush()
    f.close()
