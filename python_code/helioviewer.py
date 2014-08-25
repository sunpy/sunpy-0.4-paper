from sunpy.net.helioviewer import HelioviewerClient
hv = HelioviewerClient()
hv.download_png("2099/01/01", 6,
                 "[SDO,AIA,AIA,304,1,100],[SDO,AIA,AIA,193,1,50],"+
                 "[SOHO,LASCO,C2,white-light,1,100]",
                 x0=0, y0=0, width=768, height=768)