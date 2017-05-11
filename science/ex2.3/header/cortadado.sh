segyread tape=cube.sgy >cube.su

suwind <cube.su key=offset min=0 max=0 | \
sushw key=ntr a=500 >zerooffset.su

