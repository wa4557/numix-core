#!/usr/bin/python

import glob
import os.path

squaretemp='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
 <defs>
  <linearGradient x2="47" gradientTransform="matrix(1 0 0 1 -48 0.002)" id="linearGradient3764" x1="1" gradientUnits="userSpaceOnUse">
   <stop style="stop-color:repl1;stop-opacity:1"/>
   <stop style="stop-color:repl2;stop-opacity:1" offset="1"/>
  </linearGradient>
 </defs>
 <g>
  <path style="opacity:0.02" d="m 1 43 l 0 0.25 c 0 2.216 1.784 4 4 4 l 38 0 c 2.216 0 4 -1.784 4 -4 l 0 -0.25 c 0 2.216 -1.784 4 -4 4 l -38 0 c -2.216 0 -4 -1.784 -4 -4 z m 0 0.5 l 0 0.5 c 0 2.216 1.784 4 4 4 l 38 0 c 2.216 0 4 -1.784 4 -4 l 0 -0.5 c 0 2.216 -1.784 4 -4 4 l -38 0 c -2.216 0 -4 -1.784 -4 -4 z"/>
  <path style="opacity:0.05" d="m 1 43.25 l 0 0.25 c 0 2.216 1.784 4 4 4 l 38 0 c 2.216 0 4 -1.784 4 -4 l 0 -0.25 c 0 2.216 -1.784 4 -4 4 l -38 0 c -2.216 0 -4 -1.784 -4 -4 z"/>
  <path style="opacity:0.1" d="m 1 43 l 0 0.25 c 0 2.216 1.784 4 4 4 l 38 0 c 2.216 0 4 -1.784 4 -4 l 0 -0.25 c 0 2.216 -1.784 4 -4 4 l -38 0 c -2.216 0 -4 -1.784 -4 -4 z"/>
 </g>
 <rect width="46" style="fill:url(#linearGradient3764);fill-opacity:1" rx="4" height="46" x="-47" y="1" transform="matrix(0 -1 1 0 0 0)"/>
 <g>
  <g transform="matrix(1 0 0 1 0 -1004.36)">
   <path style="opacity:0.1" d="m 1 1043.36 0 4 c 0 2.216 1.784 4 4 4 l 38 0 c 2.216 0 4 -1.784 4 -4 l 0 -4 c 0 2.216 -1.784 4 -4 4 l -38 0 c -2.216 0 -4 -1.784 -4 -4 z"/>
  </g>
 </g>
</svg>'''

#first color is bottom of thing
#second top

#circle: bottom dark - top light
#square: the same

def find_nth(s, x, n, i = 0):
    i = s.find(x, i)
    if n == 1 or i == -1:
        return i 
    else:
        return find_nth(s, x, n - 1, i + len(x))



morethantwo = []
onlyincirc = []
cantbeautomated = []
for file in list(glob.glob('./icons/circle/48/*.svg')):
    if not os.path.islink(file):
        bn = os.path.split(file)[-1]
        if not os.path.exists('./icons/square/48/%s'%(bn)):
            onlyincirc.append(bn)
            f = open(file, 'r')
            lines = f.readlines()
            f.close()
            svg = "".join(lines)
            searchString = "stop-color:"
            if svg.count(searchString) == 2:
                l = len(searchString)
                firstind = find_nth(svg, searchString, 1)
                secondind = find_nth(svg, searchString, 2)
                col1 = (svg[firstind+l:firstind+l+7])
                col2 = (svg[secondind+l:secondind+l+7])
                square = squaretemp.replace("repl1", col1)
                square = square.replace("repl2", col2)
                f = open('./icons/square/48/templates/%s'%bn, 'w')
                f.write(square)
                f.close()
            else:
                cantbeautomated.append(bn)

#onlyincirc=$(comm -23 <(ls ./icons/circle/48/ |sort) <(ls ./icons/square/48/ |sort))
