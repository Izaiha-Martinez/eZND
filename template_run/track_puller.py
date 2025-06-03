
import sys
import h5py
import numpy as np
import subprocess as sp


f = h5py.File(sys.argv[1],'r')
wanttrackid = int(sys.argv[2])


trackids = f["trackids"][:]

# find the index of track we're looking for
# start in the obvious place
ti = wanttrackid -1
if ( trackids[ti] != wanttrackid ) :
	print("didn't find desired track id where it was expected to be")
	print("need to implement search")
	exit(2)


trackstart = f["trackstarts"][ti]
tracklength = f["tracklengths"][ti]
trackdata = f["trackdata"]
d = trackdata[ trackstart:trackstart+tracklength , 0:3]

shell_base_density=2e5

if d[0,1] < shell_base_density:
	sp.check_call('cp inlist_one_zone_burn_shell inlist_one_zone_burn',shell=True)
else:
	sp.check_call('cp inlist_one_zone_burn_core inlist_one_zone_burn',shell=True)

actuallength = tracklength
for i in range(tracklength):
	if i >= 1 and d[i-1,0] == d[i,0]:
		actuallength -= 1

print(actuallength)
for i in range(tracklength):
	if i == 0 or d[i-1,0] != d[i,0]:
		print("%20.14e\t\t%20.14e\t\t%20.14e\t\t%20.14e\n" % (d[i,0], np.log10(d[i,2]), np.log10(d[i,1]), 1.0 ))


