import os
pathNameLength = len(os.path.basename(__file__))
pathModule = __file__[:-pathNameLength]
path = pathModule+'PPTData/PPT.py'
os.system('start py '+path)