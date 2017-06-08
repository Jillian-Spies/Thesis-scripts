#this script
#Assigns the code C to all land that can be harvested and the code N to
#all land that cannot be harvseted
#June 2017
#Jillian Spies (Jillian.Spies@forestry.ubc.ca)


import arcpy
import time
Start = time.time()
print 'Start script'

arcpy.env.workspace = r"G:\ArcMap\Resultant_V1_Final_Thisisit.gdb"
fc = "res_Finalforeal_V5"

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
		row[fdic["contclass"]]="C"

		if row[fdic["SITE_INDEX"]] <= 5:
			row[fdic["contclass"]]="N"
		if row[fdic["OGMA_TYPE"]] in ["PERM", "TRANS", "ROT"]: 
			row[fdic["contclass"]]="N"
		if row[fdic["Riparian_Buffer"]] == "Riparian":
			row[fdic["contclass"]]="N"
		if row[fdic["Road_Buffer"]] == "Road":
			row[fdic["contclass"]]="N"
		if row[fdic["FID_Lake_Wetland"]] == 1:
			row[fdic["contclass"]]="N"
		if row[fdic["TIMBER_HARVEST_CODE"]] == "NO HARVEST ZONE": #this is for UWR
			row[fdic["contclass"]]="N"
		if row[fdic["TIMBER_HARVEST_CODE_1"]] == "NO HARVEST ZONE": #this is for "wildlife habitat areas", they include mt caribou
			row[fdic["contclass"]]="N"
		if row[fdic["PARK_CLASS"]]in ["A", "C"]:
			row[fdic["contclass"]]="N"
		if row[fdic["PROTECTED_LANDS_DESIGNATION"]] in ["PROVINCIAL PARK", "ECOLOGICAL RESERVE"]
			row[fdic["contclass"]]="N"
		if row[fdic["BEC_ZONE_CODE"]] == "IMA":
			row[fdic["contclass"]]="N"

		cursor.updateRow(row)
print 'It took ', round((time.time()-Start)/60,1), " minutes to run this script."