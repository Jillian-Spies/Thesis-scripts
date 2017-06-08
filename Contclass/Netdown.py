#this script
#Assigns the code NTHLB to all areas within the landbase that are unforested
#and the code THLB to all areas that are forested
#June 2017
#Jillian Spies (Jillian.Spies@forestry.ubc.ca)


import arcpy
import time
Start = time.time()
print 'Start script'

arcpy.env.workspace = r"G:\ArcMap\Clips_for_woodstock_RobValley.gdb"
fc = "Robson_Valley_res_v7_sp"

try:
	arcpy.AddField_management(fc, "contclass", "STRING")
except:
	pass

## short code to enable the use of field names
flist = arcpy.ListFields(fc)
fdic = {}
fl = []
print 'Creating flist'
for f in flist:
	fdic[f.name] = flist.index(f)
	fl.append(f.name)

print 'Reading from ArcMap...'
#the update cursor
with arcpy.da.UpdateCursor(fc, fl) as cursor:
	for row in cursor:
		row[fdic["Netdown"]]="THLB"

		if row[fdic["LAND_COVER_CLASS_CODE"]] in ["Water", "Wetland"]:
			row[fdic["netdown"]]="NTHLB"
		if row[fdic["ENGLISH_NAME"]] not in [None, ""]:
			row[fdic["netdown"]]="NTHLB"
		if row[fdic["FID_ALR"]] != -1:
			row[fdic["netdown"]]="NTLB"
		if row[fdic["BCLCS_LEVEL_1"]] == "N":
			row[fdic["netdown"]]="NTLB"
		if row[fdic["BCLCS_LEVEL_2"]] in ["N", "W"]:
			row[fdic["netdown"]]="NTLB"

		cursor.updateRow(row)
print 'It took ', round((time.time()-Start)/60,1), " minutes to run this script."