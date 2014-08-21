from sunpy import wcs
print(wcs.convert_hg_hpc(10, 53))
# Convert that position back to heliographic coordinates
print(wcs.convert_hpc_hg(100.49, 767.97))
# Try to convert a position which is not on the Sun to HG
print(wcs.convert_hpc_hg(-1500, 0))
# Convert sky coordinate to a position in HCC
print(wcs.convert_hpc_hcc(-300, 400, z=True))