## this script
#adds AU field and updATes the AU field based on AU definitions from the TSAs accordingly
#Feb 2017
#Jillian Spies (Jillian.Spies@forestry.ubc.ca)


import arcpy
import time
Start = time.time()
print 'Start script'

arcpy.env.workspace = r"G:\ArcMap\Resultant_V1_Final_Thisisit.gdb"
fc = "res_Finalforeal_V5"

try:
    arcpy.AddField_management(fc, "AU", "LONG")
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

print "Defining species list"
#define species lists
Aspen=["AC","ACT","AT","VB","MB"]
Bal=["B","BA","BG","BL"]
Cedar=["CW", "YC"]
Alder=["D","DR"]
DougFir=["F", "FD","FDC","FDI"]
Hem=["H","HM","HW"]
Pine=["PA","PL","PLC", "PW", "PLI", "PY"]
Spruce=["S","SS","SW","SX", "SE", "SXW", "SB", "SXL"] #SXL seen once in WL TSA
Birch=["EP",'E']
HemBal=Bal+Hem
HemBalSpruce = Bal+Hem+Spruce
Larch = ["LW","L"]
Decid = Alder+Aspen+Birch

print 'Reading from arcMap...'
#the update cursor
with arcpy.da.UpdateCursor(fc, fl) as cursor:
	for row in cursor:
		row[fdic["AU"]]=None

		if row[fdic["TSA_NUMBER_DESCRIPTION"]] == "Lillooet TSA":
			if row[fdic["Slope"]]<=40:
				if row[fdic["SPECIES_CD_1"]] in DougFir:
					if row[fdic["BEC_ZONE_CODE"]] == "IDF":
						if row[fdic["BEC_SUBZONE"]] == "dk":
							if row[fdic["BEC_VARIANT"]] == "2":
								row[fdic["AU"]]=200 #was 1
							elif row[fdic["BEC_VARIANT"]] in ["1","3","4"]:
								if row[fdic["SITE_INDEX"]] >=17:
									row[fdic["AU"]]=201 #was 2
								elif row[fdic["SITE_INDEX"]] <17:
									row[fdic["AU"]]=202 #was 3
						elif row[fdic["BEC_SUBZONE"]] == "xh":
							row[fdic["AU"]]=200 #was 1
						elif row[fdic["BEC_SUBZONE"]] in ["xw", "xm", "xk", "xc", "xv", "dh", "dw", "dm", "dc", "dv"]:
							if row[fdic["SITE_INDEX"]] >=17:
								row[fdic["AU"]] = 201 #was 2
							elif row[fdic["SITE_INDEX"]] <17:
								row[fdic["AU"]] = 202 # was 3
					elif row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
						row[fdic["AU"]]= 200 # was 1
					elif row[fdic["BEC_ZONE_CODE"]] in ["AT", "BWBS", "CWH", "ESSF", "ICH", "MH", "SBPS", "SBS", "SWB", "MS"]:
						if row[fdic["SITE_INDEX"]] >=17:
							row[fdic["AU"]]= 201 # was 2
						elif row[fdic["SITE_INDEX"]] <17:
							row[fdic["AU"]]= 202 # was 3
				elif row[fdic["SPECIES_CD_1"]] in Spruce+Bal+Hem+Cedar:
					if row[fdic["SITE_INDEX"]] >=15:
						row[fdic["AU"]]= 205 # was 6
					elif row[fdic["SITE_INDEX"]] <15:
						row[fdic["AU"]]= 206 # was 7
				elif row[fdic["SPECIES_CD_1"]] in ["PL","PLI","PLC"]:
					if row[fdic["SITE_INDEX"]] >=16:
						row[fdic["AU"]]=350 #was 10
					if row[fdic["SITE_INDEX"]] <16:
						row[fdic["AU"]]= 214 # was 15
				elif row[fdic["SPECIES_CD_1"]] in Aspen+Alder+Birch:
					row[fdic["AU"]]= 133
				elif row[fdic["SPECIES_CD_1"]] in ["PA", "PY"]:
					row[fdic["AU"]]= 500
			if row[fdic["Slope"]]>40:
					if row[fdic["SPECIES_CD_1"]] in DougFir:
						if row[fdic["BEC_ZONE_CODE"]] == "IDF":
							if row[fdic["BEC_SUBZONE"]] == "dk":
								if row[fdic["BEC_VARIANT"]] == "2":
									row[fdic["AU"]]= 222 # was 119
								elif row[fdic["BEC_VARIANT"]] in ["1","3","4"]:
									if row[fdic["SITE_INDEX"]] >=17:
										row[fdic["AU"]]= 223 # was 120
									elif row[fdic["SITE_INDEX"]] <17:
										row[fdic["AU"]]=121
							elif row[fdic["BEC_SUBZONE"]] == "xh":
								row[fdic["AU"]]=222 # was 119
							elif row[fdic["BEC_SUBZONE"]] in ["xw", "xm", "xk", "xc", "xv", "dh", "dw", "dm", "dc", "dv"]:
								if row[fdic["SITE_INDEX"]] >=17:
									row[fdic["AU"]] = 223 # was 120
								elif row[fdic["SITE_INDEX"]] <17:
									row[fdic["AU"]] =121
						elif row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
							row[fdic["AU"]]= 222 # was 119
						elif row[fdic["BEC_ZONE_CODE"]] in ["AT", "BWBS", "CWH", "ESSF", "ICH", "MH", "SBPS", "SBS", "SWB", "MS"]:
							if row[fdic["SITE_INDEX"]] >=17:
								row[fdic["AU"]]= 223 # was 120
							elif row[fdic["SITE_INDEX"]] <17:
								row[fdic["AU"]]=121
					elif row[fdic["SPECIES_CD_1"]] in Spruce+Bal+Hem+Cedar:
						if row[fdic["SITE_INDEX"]] >=15:
							row[fdic["AU"]]=124
						elif row[fdic["SITE_INDEX"]] <15:
							row[fdic["AU"]]=125
					elif row[fdic["SPECIES_CD_1"]] in ["PL","PLI","PLC"]:
						if row[fdic["SITE_INDEX"]] >=16:
							row[fdic["AU"]]=128
						if row[fdic["SITE_INDEX"]] <16:
							row[fdic["AU"]]=129
					elif row[fdic["SPECIES_CD_1"]] in Aspen+Alder+Birch:
						row[fdic["AU"]]= 133
					elif row[fdic["SPECIES_CD_1"]] in ["PA", "PY"]:
						row[fdic["AU"]]= 500
		elif row[fdic["TSA_NUMBER_DESCRIPTION"]] == "Quesnel TSA":
			if row[fdic["SPECIES_CD_1"]] in Pine:
				if row[fdic["BEC_ZONE_CODE"]] in "ESSF" + "ICH":
					if 5<row[fdic["SITE_INDEX"]]<=12:
						row[fdic["AU"]]=140
					elif 12<row[fdic["SITE_INDEX"]]<=19:
						row[fdic["AU"]]=141
					elif 19<row[fdic["SITE_INDEX"]]<=26:
						row[fdic["AU"]]=142
					elif 26<row[fdic["SITE_INDEX"]]:
						row[fdic["AU"]]=143
				if row[fdic["BEC_ZONE_CODE"]] in "SBS" + "IDF":
					if 5<row[fdic["SITE_INDEX"]]<=12:
						row[fdic["AU"]]=164
					elif 12<row[fdic["SITE_INDEX"]]<=19:
						row[fdic["AU"]]=165
					elif 19<row[fdic["SITE_INDEX"]]<=26:
						row[fdic["AU"]]=166
					elif 26<row[fdic["SITE_INDEX"]]:
						row[fdic["AU"]]=167
			if row[fdic["SPECIES_CD_1"]] in Spruce:
				if 5<row[fdic["SITE_INDEX"]]<=10:
					row[fdic["AU"]]=144
				elif 10<row[fdic["SITE_INDEX"]]<=15:
					row[fdic["AU"]]=145
				elif 15<row[fdic["SITE_INDEX"]]<=20:
					row[fdic["AU"]]=146
				elif 20<row[fdic["SITE_INDEX"]]:
					row[fdic["AU"]]=147
			if row[fdic["SPECIES_CD_1"]] in DougFir:
				if 5<row[fdic["SITE_INDEX"]]<=11:
					row[fdic["AU"]]=148
				elif 11<row[fdic["SITE_INDEX"]]<=17:
					row[fdic["AU"]]=149
				elif 17<row[fdic["SITE_INDEX"]]<=23:
					row[fdic["AU"]]=150
				elif 23<row[fdic["SITE_INDEX"]]:
					row[fdic["AU"]]=151
			if row[fdic["SPECIES_CD_1"]] in HemBal:
				if 5<row[fdic["SITE_INDEX"]]<=11:
					row[fdic["AU"]]=152
				elif 11<row[fdic["SITE_INDEX"]]<=17:
					row[fdic["AU"]]=153
				elif 17<row[fdic["SITE_INDEX"]]<=23:
					row[fdic["AU"]]=154
				elif 23<row[fdic["SITE_INDEX"]]:
					row[fdic["AU"]]=155
			if row[fdic["SPECIES_CD_1"]] in Decid:
				if 5<row[fdic["SITE_INDEX"]]<=15:
					row[fdic["AU"]]=156
				elif 15<row[fdic["SITE_INDEX"]]<=20:
					row[fdic["AU"]]=157
				elif 20<row[fdic["SITE_INDEX"]]<=25:
					row[fdic["AU"]]=158
				elif 25<row[fdic["SITE_INDEX"]]:
					row[fdic["AU"]]=159
			if row[fdic["SPECIES_CD_1"]] in Cedar:
				if 5<row[fdic["SITE_INDEX"]]<=11:
					row[fdic["AU"]]=160
				elif 11<row[fdic["SITE_INDEX"]]<=17:
					row[fdic["AU"]]=161
				elif 17<row[fdic["SITE_INDEX"]]<=23:
					row[fdic["AU"]]=162
				elif 23<row[fdic["SITE_INDEX"]]:
					row[fdic["AU"]]=163

		elif row[fdic["TSA_NUMBER_DESCRIPTION"]] == "Williams Lake TSA": #this works (April 25)
			if row[fdic["SPECIES_CD_1"]] in DougFir:
				if row[fdic["SPECIES_PCT_1"]]>=40:
					if row[fdic["UWR_NUMBER"]] not in ['',None]:
						if row[fdic["SITE_INDEX"]]>=7:
							if row[fdic["BEC_ZONE_CODE"]] in ['BG', "ESSF", "MS"]:
								row[fdic["AU"]]=101
							elif row[fdic["BEC_ZONE_CODE"]] in ['IDF', 'SBPS']:
								row[fdic["AU"]]=102
							elif row[fdic["BEC_ZONE_CODE"]] in ['SBS', 'ICH']:
								row[fdic["AU"]]=104
						if row[fdic["SITE_INDEX"]]<7:
							row[fdic["AU"]]=805
					elif row[fdic["UWR_NUMBER"]] in ['',None]:
						if 7<=row[fdic["SITE_INDEX"]]<12:
							if row[fdic["BEC_ZONE_CODE"]] not in ['IDF','SBPS']:
								row[fdic["AU"]]=108
							if row[fdic["BEC_ZONE_CODE"]] in ['IDF','SBPS']:
								row[fdic["AU"]]=119
						elif row[fdic["SITE_INDEX"]]>=12:
							if row[fdic["BEC_ZONE_CODE"]] not in ['IDF','SBPS']:
								row[fdic["AU"]]=109
							if row[fdic["BEC_ZONE_CODE"]] in ['IDF','SBPS']	:
								row[fdic["AU"]]=120
						if row[fdic["SITE_INDEX"]]<7:
							row[fdic["AU"]]=805
				elif row[fdic["SPECIES_PCT_1"]]<40:
					if row[fdic["UWR_NUMBER"]] in ['',None]:
						if 7<=row[fdic["SITE_INDEX"]]<12:
							if row[fdic["BEC_ZONE_CODE"]] not in ['IDF','SBPS'] :
								row[fdic["AU"]]=108
							if row[fdic["BEC_ZONE_CODE"]] in ['IDF','SBPS'] :
								row[fdic["AU"]]=119
						elif row[fdic["SITE_INDEX"]]>=12:
							if row[fdic["BEC_ZONE_CODE"]] not in ['IDF','SBPS']	:					
								row[fdic["AU"]]=109
							if row[fdic["BEC_ZONE_CODE"]] in ['IDF','SBPS']	:
								row[fdic["AU"]]=120								
			elif row[fdic["SPECIES_CD_1"]] in Cedar + Hem:
				if row[fdic["SITE_INDEX"]]>17:
					row[fdic["AU"]]=112
				elif 7<=row[fdic["SITE_INDEX"]] <12:
					row[fdic["AU"]]=110
				elif 12<=row[fdic["SITE_INDEX"]] <=17:
					row[fdic["AU"]]=111
				elif row[fdic["SITE_INDEX"]] <7:
					row[fdic["AU"]]=804                     
			elif row[fdic["SPECIES_CD_1"]] in Spruce + Bal:
				if row[fdic["SITE_INDEX"]]>17:
					row[fdic["AU"]]=115
				elif 7<=row[fdic["SITE_INDEX"]] <=12:
					row[fdic["AU"]]=114
				elif 12<row[fdic["SITE_INDEX"]] <=17:
					row[fdic["AU"]]=114
				elif row[fdic["SITE_INDEX"]] <7:
					row[fdic["AU"]]=803	
			elif row[fdic["SPECIES_CD_1"]] in Pine:
				if row[fdic["SITE_INDEX"]]>17:
					row[fdic["AU"]]=118
				elif 7<=row[fdic["SITE_INDEX"]] <=12:
					row[fdic["AU"]]=116
				elif 12<row[fdic["SITE_INDEX"]] <=17:
					row[fdic["AU"]]=117
				elif row[fdic["SITE_INDEX"]] <7:
					row[fdic["AU"]]=802
			elif row[fdic["SPECIES_CD_1"]] in Aspen:
				row[fdic["AU"]]=800
			elif row[fdic["SPECIES_CD_1"]] in Birch:
				row[fdic["AU"]]= 801

		elif row[fdic["TSA_NUMBER_DESCRIPTION"]] == "Robson Valley TSA": #all is good here. you're killin it, Jill
			if row[fdic["SPECIES_CD_1"]] in Spruce:
				if row[fdic["SPECIES_PCT_1"]]>=81:
					if row[fdic["BEC_ZONE_CODE"]] in "ESSF":
						row[fdic["AU"]]=61
					if row[fdic["BEC_ZONE_CODE"]] in ["ICH", "SBS"]:
						row[fdic["AU"]]=62
				if row[fdic["SPECIES_CD_2"]] in Pine + Hem + Cedar + DougFir + Bal + Aspen + Alder + Birch + ["L"]+Spruce:
					if row[fdic["BEC_ZONE_CODE"]] in "ESSF":
						row[fdic["AU"]]=61
					if row[fdic["BEC_ZONE_CODE"]] in ["ICH","SBS"]:
						row[fdic["AU"]]=62
			elif row[fdic["SPECIES_CD_1"]] in ["PW","PA"]:
				if row[fdic["BEC_ZONE_CODE"]] == "ESSF":
					row[fdic["AU"]]=63
				elif row[fdic["BEC_ZONE_CODE"]] in ["ICH","SBS"]:
					row[fdic["AU"]]=64
			elif row[fdic["SPECIES_CD_1"]] in ["PL","PLI"]:
				if row[fdic["SPECIES_PCT_1"]]>=81:
					if row[fdic["BEC_ZONE_CODE"]] == "ESSF":
						row[fdic["AU"]]=63
					elif row[fdic["BEC_ZONE_CODE"]] in ["ICH","SBS"]:
						row[fdic["AU"]]=64        
				elif row[fdic["SPECIES_CD_2"]] in DougFir + Pine + Hem + Cedar + Bal + Aspen + Birch + Alder + Spruce + ["L"]:
					if row[fdic["BEC_ZONE_CODE"]] == "ESSF":
						row[fdic["AU"]]=63
					elif row[fdic["BEC_ZONE_CODE"]] in ["ICH","SBS"]:
						row[fdic["AU"]]=64
				elif row[fdic["SPECIES_CD_2"]] in DougFir + Pine + Hem + Cedar + Bal + Aspen + Birch + Alder + Spruce + ["L"]:
					if row[fdic["BEC_ZONE_CODE"]] in ["ICH","SBS"]:
						row[fdic["AU"]]=64
			elif row[fdic["SPECIES_CD_1"]] in DougFir:
				if row[fdic["PSTSPCSCD"]] != "DRA": 
					if row[fdic["SPECIES_PCT_1"]]>=81:
						row[fdic["AU"]]=65
					elif row[fdic["SPECIES_CD_2"]] in Pine + Cedar + Hem + Bal + Spruce + ["L"] + Aspen + Alder + Birch:
						row[fdic["AU"]]=65 #This AU is NOT Armillaria areas
				elif row[fdic["PSTSVRTCD"]] in ["S"]:
					row[fdic["AU"]]=74 #severe
				elif row[fdic["PSTSVRTCD"]] in ["M"]:
					row[fdic["AU"]]=73 #moderate
			elif row[fdic["SPECIES_CD_1"]] in Bal:
				if row[fdic["SPECIES_PCT_1"]]>=81:
					if row[fdic["BEC_ZONE_CODE"]] == "ESSF":
						row[fdic["AU"]]=66
					elif row[fdic["BEC_ZONE_CODE"]] in ["SBS", "ICH"]:
						row[fdic["AU"]]=67
				elif row[fdic["SPECIES_CD_2"]] in DougFir + Pine + ["L"] + Aspen + Alder + Birch + Hem + Cedar + Spruce:
					if row[fdic["BEC_ZONE_CODE"]] == "ESSF":
						row[fdic["AU"]]=66
					elif row[fdic["BEC_ZONE_CODE"]] in ["SBS", "ICH"]:
						row[fdic["AU"]]=67
			elif row[fdic["SPECIES_CD_1"]] in Cedar:
				if row[fdic["SPECIES_PCT_1"]]>=81:
					if row[fdic["BEC_ZONE_CODE"]] == "ICH":
						row[fdic["AU"]]=71
					else:
						row[fdic["AU"]]=68
				elif row[fdic["SPECIES_CD_2"]] in Cedar + Pine + Aspen + Birch + Alder + ["L"] + Hem + Spruce + Bal + DougFir:
					if row[fdic["BEC_ZONE_CODE"]] == "ICH":
						row[fdic["AU"]]=71
					else:
						row[fdic["AU"]]=68 
			elif row[fdic["SPECIES_CD_1"]] in Hem:
				if row[fdic["SPECIES_PCT_1"]]>=81:
					if row[fdic["BEC_ZONE_CODE"]] == "ICH":
						row[fdic["AU"]]=72
					else:
						row[fdic["AU"]]=69
				elif row[fdic["SPECIES_CD_2"]] in Pine + DougFir + ["L"] + Cedar + Bal + Spruce + Aspen + Alder + Birch:
					if row[fdic["BEC_ZONE_CODE"]] == "ICH":
						row[fdic["AU"]]=72
					else:
						row[fdic["AU"]]=69
			elif row[fdic["SPECIES_CD_1"]] in ["Cot"] + Aspen + Alder + Bal + Birch:
				row[fdic["AU"]]=70
		elif row[fdic["TSA_NUMBER_DESCRIPTION"]] == "Prince George TSA": #this works
			if row[fdic["SPECIES_CD_1"]] in DougFir:
				if row[fdic["SITE_INDEX"]]>=10:
					if row[fdic["SPECIES_PCT_1"]]>=81:
						row[fdic["AU"]]=81
					elif row[fdic["SPECIES_CD_2"]] in ["L"] + Alder + Aspen+ Cedar + Pine + HemBalSpruce:
						row[fdic["AU"]]=81
				if row[fdic["SITE_INDEX"]]<10:
					if row[fdic["SPECIES_PCT_1"]]>=81:
						row[fdic["AU"]]=82
					elif row[fdic["SPECIES_CD_2"]] in ["L","ACB"] + Cedar + Pine + Alder + Aspen + HemBalSpruce:
						row[fdic["AU"]]=82
			if row[fdic["SPECIES_CD_1"]] in Aspen:
				if row[fdic["SPECIES_CD_2"]] in ["ACB"] + Alder + Aspen:
					row[fdic["AU"]]=83
			if row[fdic["SPECIES_CD_1"]] in Cedar:
				if row[fdic["SPECIES_PCT_1"]]>=81:
					row[fdic["AU"]]=83
				elif row[fdic["SPECIES_CD_2"]] in ["ACB","L"] + Aspen + DougFir + Alder + Pine + Cedar +HemBalSpruce:
					row[fdic["AU"]]=83
			if row[fdic["SPECIES_CD_1"]] in Hem:
				if row[fdic["SPECIES_PCT_1"]]>=81:
					row[fdic["AU"]]=84
				elif row[fdic["SPECIES_CD_2"]] in ["L","ACB"]+ Alder + Aspen + Pine + DougFir + Cedar + Bal + Spruce:
					row[fdic["AU"]]=84
			if row[fdic["SPECIES_CD_1"]] in Bal:
				if row[fdic["SITE_INDEX"]]>=10:
					if row[fdic["SPECIES_PCT_1"]]>=81:
						row[fdic["AU"]]=85
					elif row[fdic["SPECIES_CD_2"]] in ["L","ACB"]+Pine+Aspen+Alder+Hem+Cedar+Spruce+Hem+DougFir:
						row[fdic["AU"]]=85
				if row[fdic["SITE_INDEX"]]<10:
					if row[fdic["SPECIES_PCT_1"]]>=81:
						row[fdic["AU"]]=86
					elif row[fdic["SPECIES_CD_2"]] in DougFir+Pine+Aspen+Alder+Hem+Cedar+Spruce+["L","ACB"]:
						row[fdic["AU"]]=86
			if row[fdic["SPECIES_CD_1"]] in Spruce:
				if row[fdic["SITE_INDEX"]]>=15:
					if row[fdic["SPECIES_PCT_1"]]>=81:
						row[fdic["AU"]]=87
					elif row[fdic["SPECIES_CD_2"]] in Cedar+Pine+Aspen+Alder+["L","ACB"]+Bal+Hem+DougFir:
						row[fdic["AU"]]=87
				if 15>row[fdic["SITE_INDEX"]]>=10:
					if row[fdic["SPECIES_PCT_1"]]>=81:
						row[fdic["AU"]]=88
					elif row[fdic["SPECIES_CD_2"]] in Cedar+Pine+Aspen+Alder+["L","ACB"]+Bal+Hem+DougFir:
						row[fdic["AU"]]=88
				if row[fdic["SITE_INDEX"]]<10:
					if row[fdic["SPECIES_PCT_1"]]>=81:
						row[fdic["AU"]]=89
					elif row[fdic["SPECIES_CD_2"]] in Cedar+Pine+DougFir+Hem+Aspen+Alder+["L","ACB"]+Bal:
						row[fdic["AU"]]=89
			if row[fdic["SPECIES_CD_1"]] in Pine:
				if row[fdic["SITE_INDEX"]]>=15:
					if row[fdic["SPECIES_CD_2"]] in DougFir+Pine+Spruce+Bal+Hem+Cedar+Aspen+Alder+["L", "ACB"]:
						row[fdic["AU"]]=90
				if 10<=row[fdic["SITE_INDEX"]]<15:
					if row[fdic["SPECIES_CD_2"]] in DougFir+Pine+Spruce+Bal+Hem+Cedar+Aspen+Alder+["L", "ACB"]:
						row[fdic["AU"]]=91
				if row[fdic["SITE_INDEX"]]<10:
					if row[fdic["SPECIES_CD_2"]] in DougFir+Pine+Spruce+Bal+Hem+Cedar+Aspen+Alder+["L", "ACB"]:
						row[fdic["AU"]]=92
			if row[fdic["SPECIES_CD_1"]] == "L":
				if row[fdic["SPECIES_CD_2"]] !="F":
					if row[fdic["SITE_INDEX"]]>=15:
						row[fdic["AU"]]=90
					if 10<=row[fdic["SITE_INDEX"]]<15:
						row[fdic["AU"]]=91
					if row[fdic["SITE_INDEX"]]<10:
						row[fdic["AU"]]=92
		elif row[fdic["TSA_NUMBER_DESCRIPTION"]] == "100 Mile House TSA": #this doesn't work (found tons of null AUs APril 27)
			if row[fdic["SPECIES_CD_1"]] in Aspen + Birch:
				if row[fdic["SITE_INDEX"]]<10:
					row[fdic["AU"]]=11
				elif 15>row[fdic["SITE_INDEX"]]>=10:
					row[fdic["AU"]]=12
				elif 20>row[fdic["SITE_INDEX"]]>=15:
					row[fdic["AU"]]=13
				elif row[fdic["SITE_INDEX"]]>=20:
					row[fdic["AU"]]=14
			elif row[fdic["SPECIES_CD_1"]] in DougFir:
				if row[fdic["SITE_INDEX"]]<10:
					row[fdic["AU"]]=21
				elif 15>row[fdic["SITE_INDEX"]]>=10:
					row[fdic["AU"]]=22
				elif 20>row[fdic["SITE_INDEX"]]>=15:
					row[fdic["AU"]]=23
				elif row[fdic["SITE_INDEX"]]>=20:
					row[fdic["AU"]]=24
			elif row[fdic["SPECIES_CD_1"]] in Bal + Cedar + Hem:
				if row[fdic["SITE_INDEX"]]<10:
					row[fdic["AU"]]=31
				elif 15>row[fdic["SITE_INDEX"]]>=10:
					row[fdic["AU"]]=32
				elif 20>row[fdic["SITE_INDEX"]]>=15:
					row[fdic["AU"]]=33
				elif row[fdic["SITE_INDEX"]]>=20:
					row[fdic["AU"]]=34
			elif row[fdic["SPECIES_CD_1"]] in Pine:
				if row[fdic["SITE_INDEX"]]<10:
					row[fdic["AU"]]=41
				elif 15>row[fdic["SITE_INDEX"]]>=10:
					row[fdic["AU"]]=42
				elif 20>row[fdic["SITE_INDEX"]]>=15:
					row[fdic["AU"]]=43
				elif row[fdic["SITE_INDEX"]]>=20:
					row[fdic["AU"]]=44
			elif row[fdic["SPECIES_CD_1"]] in Spruce:
				if row[fdic["SITE_INDEX"]]<10:
					row[fdic["AU"]]=51
				elif 15>row[fdic["SITE_INDEX"]]>=10:
					row[fdic["AU"]]=52
				elif 20>row[fdic["SITE_INDEX"]]>=15:
					row[fdic["AU"]]=53
				elif row[fdic["SITE_INDEX"]]>=20:
					row[fdic["AU"]]=54
		elif row[fdic["TSA_NUMBER_DESCRIPTION"]] == "Kamloops TSA":
			if row[fdic["SPECIES_CD_1"]] in DougFir:
				if row[fdic["BEC_ZONE_CODE"]] in "PP"+"BG":
					row[fdic["AU"]]=1
				elif row[fdic["BEC_ZONE_CODE"]]== "IDF":
					if row[fdic["BEC_SUBZONE"]] in "dc"+"dh"+"dm"+"dv"+"dvw"+"dw"+"mc"+"mh"+"mm"+"mmp"+"mw"+"un"+"vk"+"wc"+"wcp"+"wcw"+"wk"+"xc"+"xcw"+"xh"+"xk"+"xm"+"xv"+"xvp"+"xvw"+"xw":
						row[fdic["AU"]]=1
					elif row[fdic["BEC_SUBZONE"]] == "dk":
						if row[fdic["BEC_VARIANT"]] in "1"+"3"+"4":
							row[fdic["AU"]]=1
						elif row[fdic["BEC_VARIANT"]]=="2":
							if row[fdic["SPECIES_CD_2"]] not in ["H"+"HM"+"HW" + "CW"+"YC"+ "B"+"BA"+"BG"+"BL" + "PL" + "PLI"]:
								row[fdic["AU"]]=2
				elif row[fdic["BEC_ZONE_CODE"]] in "ESSF"+"ICH"+"IMA"+"MS"+"SBPS"+"SBS":
					if row[fdic["SITE_INDEX"]]>15:
						row[fdic["AU"]]=3
					elif row[fdic["SITE_INDEX"]]<=15:
						row[fdic["AU"]]=5
				elif row[fdic["BEC_ZONE_CODE"]] =="MS":
					if row[fdic["SPECIES_CD_2"]] not in ["H"+"HM"+"HW"+ "CW"+"YC"+ "B"+"BA"+"BG"+"BL" + "PL" + "PLI"]:
						row[fdic["AU"]]=2
			elif row[fdic["SPECIES_CD_1"]] in Cedar:
				if row[fdic["SITE_INDEX"]]>17:
					row[fdic["AU"]]=7
				elif row[fdic["SITE_INDEX"]]<=17:
					row[fdic["AU"]]=8
			elif row[fdic["SPECIES_CD_1"]] in Hem:
				if row[fdic["SITE_INDEX"]]>16:
					row[fdic["AU"]]=9
				elif row[fdic["SITE_INDEX"]]<=16:
					row[fdic["AU"]]=10
			elif row[fdic["SPECIES_CD_1"]] in Bal:
				if row[fdic["SITE_INDEX"]]>13:
					row[fdic["AU"]]= 210 # was 11
				elif row[fdic["SITE_INDEX"]]<=13:
					row[fdic["AU"]]=212 # was 13
			elif row[fdic["SPECIES_CD_1"]] in Spruce:
				if row[fdic["SITE_INDEX"]]>14:
					row[fdic["AU"]]=15
				elif row[fdic["SITE_INDEX"]]<=14:
					row[fdic["AU"]]=216 # was 17
			elif row[fdic["SPECIES_CD_1"]] in Pine:
				if row[fdic["SITE_INDEX"]]>14:
					row[fdic["AU"]]=19
				elif row[fdic["SITE_INDEX"]]<=14:
					row[fdic["AU"]]=217 # was 21
			elif row[fdic["SPECIES_CD_1"]] in Aspen:
				row[fdic["AU"]] = 700
			elif row[fdic["SPECIES_CD_1"]] in Larch:
				row[fdic["AU"]]=701
			elif row[fdic["SPECIES_CD_1"]] in Birch:
				row[fdic["AU"]]=702

		cursor.updateRow(row)
print ('It took ', round((time.time()-Start)/60,1), " minutes to run this script.")