import platform
import os
import sys
import distro


print(platform.system() + " | ", platform.release())

print(distro.name() + " | ", distro.version())

#print(sys.platform)
#print(os)
