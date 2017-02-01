## this script
#adds AU field and updATes the AU field based on AU definitions from the TSAs accordingly
#October 2016
#Jillian Spies (Jillian.Spies@forestry.ubc.ca)


import arcpy
import time
Start = time.time()
print 'Start script'

arcpy.env.workspace = r"G:\ArcMap\Resultant_V1_Final_Thisisit.gdb"
fc = "res_finalforeal_v4"

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
Spruce=["S","SS","SW","SX", "SE", "SXW", "SB"]
Birch=["EP",'E']
HemBal=Bal+Hem
HemBalSpruce = Bal+Hem+Spruce
Larch = ["LW","L"]

print 'Reading from arcCrap...'
#the update cursor
with arcpy.da.UpdateCursor(fc, fl) as cursor:
	for row in cursor:
		row[fdic["AU"]]=None

		if row[fdic["TSA_NUMBER_DESCRIPTION"]] == "Lillooet TSA":
			if row[fdic["Slope"]]<=40:
				if row[fdic["SPECIES_CD_1"]] in DougFir:
					if row[fdic["BEC_ZONE_CODE"]] == "IDF":
						if row[fdic["BEC_SUBZONE"]] == "dk":
							print row[fdic["BEC_VARIANT"]]
							if row[fdic["BEC_VARIANT"]] == "2":
								row[fdic["AU"]]=1
							elif row[fdic["BEC_VARIANT"]] in ["1","3","4"]:
								print "BecVar134"
								if row[fdic["SITE_INDEX"]] >=17:
									if 141>row[fdic["Current_Year"]]>=28:
										row[fdic["AU"]]=2
									elif row[fdic["Current_Year"]]>=141:
										row[fdic["AU"]]=4
								elif row[fdic["SITE_INDEX"]] <17:
									if 141>row[fdic["Current_Year"]]>=28:
										row[fdic["AU"]]=3
									elif row[fdic["Current_Year"]]>=141:
										row[fdic["AU"]]=5
						elif row[fdic["BEC_SUBZONE"]] == "xh":
							#if row[fdic["BEC_VARIANT"]] not in [None,""]:
							#if row[fdic["SITE_INDEX"]] not in [None,""]:
							#if row[fdic["Current_Year"]] not in [None,""]:
							row[fdic["AU"]]=1
						elif row[fdic["BEC_SUBZONE"]] in ["xw", "xm", "xk", "xc", "xv", "dh", "dw", "dm", "dc", "dv"]:
							#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
							if row[fdic["SITE_INDEX"]] >=17:
								if 141>row[fdic["Current_Year"]]>=28:
									row[fdic["AU"]] = 2
								elif row[fdic["Current_Year"]]>=141:
									row[fdic["AU"]]=4
							elif row[fdic["SITE_INDEX"]] <17:
								if 141>row[fdic["Current_Year"]]>=28:
									row[fdic["AU"]] = 2
								elif row[fdic["Current_Year"]]>=141:
										row[fdic["AU"]]=5
					elif row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
						#if row[fdic["BEC_SUBZONE"]] not in [None, ""]:
						#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
						#if row[fdic["SITE_INDEX"]] not in [None,""]:
						#if row[fdic["Current_Year"]] not in [None,""]:
						row[fdic["AU"]]=1
					elif row[fdic["BEC_ZONE_CODE"]] in ["AT", "BWBS", "CWH", "ESSF", "ICH", "MH", "SBPS", "SBS", "SWB"]:
						#if row[fdic["BEC_SUBZONE"]] not in [None, ""]:
						#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
						if row[fdic["SITE_INDEX"]] >=17:
							if 141>row[fdic["Current_Year"]]>=28:
								row[fdic["AU"]]=2
							elif row[fdic["Current_Year"]]>=141:
								row[fdic["AU"]]=4
						elif row[fdic["SITE_INDEX"]] <17:
							if 141>row[fdic["Current_Year"]]>=28:
								row[fdic["AU"]]=3
							elif row[fdic["Current_Year"]]>=141:
										row[fdic["AU"]]=5
				elif row[fdic["SPECIES_CD_1"]] in Spruce+Bal+Hem+Cedar:
					#if row[fdic["BEC_ZONE_CODE"]] not in [None,""]:
					#if row[fdic["BEC_SUBZONE"]] not in [None, ""]:
					#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
					if row[fdic["SITE_INDEX"]] >=15:
						if 141>row[fdic["Current_Year"]]>=28:
							row[fdic["AU"]]=6
						elif row[fdic["Current_Year"]]>=141:
							row[fdic["AU"]]=8
					elif row[fdic["SITE_INDEX"]] <15:
						if 141>row[fdic["Current_Year"]]>=28:
							row[fdic["AU"]]=7
						elif row[fdic["Current_Year"]]>=141:
							row[fdic["AU"]]=9

				elif row[fdic["SPECIES_CD_1"]] in ["PL","PLI","PLC"]:
					#if row[fdic["BEC_ZONE_CODE"]] not in [None,""]:
					#if row[fdic["BEC_SUBZONE"]] not in [None, ""]:
					#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
					if row[fdic["SITE_INDEX"]] >=16:
						if 141>row[fdic["Current_Year"]]>=28:
							row[fdic["AU"]]=10
						elif row[fdic["Current_Year"]]>=141:
							row[fdic["AU"]]=16
					if row[fdic["SITE_INDEX"]] <16:
						if 141>row[fdic["Current_Year"]]>=28:
							row[fdic["AU"]]=15
						elif row[fdic["Current_Year"]]>=141:
							row[fdic["AU"]]=17

			if row[fdic["Slope"]]>40:
					if row[fdic["SPECIES_CD_1"]] in DougFir:
						if row[fdic["BEC_ZONE_CODE"]] == "IDF":
							if row[fdic["BEC_SUBZONE"]] == "dk":
								if row[fdic["BEC_VARIANT"]] == "2":
									row[fdic["AU"]]=119
								elif row[fdic["BEC_VARIANT"]] in ["1","3","4"]:
									if row[fdic["SITE_INDEX"]] >=17:
										if 141>row[fdic["Current_Year"]]>=28:
											row[fdic["AU"]]=120
										elif row[fdic["Current_Year"]]>=141:
											row[fdic["AU"]]=122
									elif row[fdic["SITE_INDEX"]] <17:
										if 141>row[fdic["Current_Year"]]>=28:
											row[fdic["AU"]]=121
										elif row[fdic["Current_Year"]]>=141:
											row[fdic["AU"]]=123
							elif row[fdic["BEC_SUBZONE"]] == "xh":
								#if row[fdic["BEC_VARIANT"]] not in [None,""]:
								#if row[fdic["SITE_INDEX"]] not in [None,""]:
								#if row[fdic["Current_Year"]] not in [None,""]:
								row[fdic["AU"]]=119
							elif row[fdic["BEC_SUBZONE"]] in ["xw", "xm", "xk", "xc", "xv", "dh", "dw", "dm", "dc", "dv"]:
								#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
								if row[fdic["SITE_INDEX"]] >=17:
									if 141>row[fdic["Current_Year"]]>=28:
										row[fdic["AU"]] = 120
									elif row[fdic["Current_Year"]]>=141:
										row[fdic["AU"]]=122
								elif row[fdic["SITE_INDEX"]] <17:
									if 141>row[fdic["Current_Year"]]>=28:
										row[fdic["AU"]] =121
									elif row[fdic["Current_Year"]]>=141:
											row[fdic["AU"]]=123
						elif row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
							#if row[fdic["BEC_SUBZONE"]] not in [None, ""]:
							#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
							#if row[fdic["SITE_INDEX"]] not in [None,""]:
							#if row[fdic["Current_Year"]] not in [None,""]:
							row[fdic["AU"]]=119
						elif row[fdic["BEC_ZONE_CODE"]] in ["AT", "BWBS", "CWH", "ESSF", "ICH", "MH", "SBPS", "SBS", "SWB"]:
							#if row[fdic["BEC_SUBZONE"]] not in [None, ""]:
							#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
							if row[fdic["SITE_INDEX"]] >=17:
								if 141>row[fdic["Current_Year"]]>=28:
									row[fdic["AU"]]=120
								elif row[fdic["Current_Year"]]>=141:
									row[fdic["AU"]]=122
							elif row[fdic["SITE_INDEX"]] <17:
								if 141>row[fdic["Current_Year"]]>=28:
									row[fdic["AU"]]=121
								elif row[fdic["Current_Year"]]>=141:
									row[fdic["AU"]]=123
					elif row[fdic["SPECIES_CD_1"]] in Spruce+Bal+Hem+Cedar:
						#if row[fdic["BEC_ZONE_CODE"]] not in [None,""]:
						#if row[fdic["BEC_SUBZONE"]] not in [None, ""]:
						#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
						if row[fdic["SITE_INDEX"]] >=15:
							if 141>row[fdic["Current_Year"]]>=28:
								row[fdic["AU"]]=124
							elif row[fdic["Current_Year"]]>=141:
								row[fdic["AU"]]=126
						elif row[fdic["SITE_INDEX"]] <15:
							if 141>row[fdic["Current_Year"]]>=28:
								row[fdic["AU"]]=125
							elif row[fdic["Current_Year"]]>=141:
								row[fdic["AU"]]=127

					elif row[fdic["SPECIES_CD_1"]] in ["PL","PLI","PLC"]:
						#if row[fdic["BEC_ZONE_CODE"]] not in [None,""]:
						#if row[fdic["BEC_SUBZONE"]] not in [None, ""]:
						#if row[fdic["BEC_VARIANT"]] not in [None, ""]:
						if row[fdic["SITE_INDEX"]] >=16:
							if 141>row[fdic["Current_Year"]]>=28:
								row[fdic["AU"]]=1128
							elif row[fdic["Current_Year"]]>=141:
								row[fdic["AU"]]=130
						if row[fdic["SITE_INDEX"]] <16:
							if 141>row[fdic["Current_Year"]]>=28:
								row[fdic["AU"]]=129
							elif row[fdic["Current_Year"]]>=141:
								row[fdic["AU"]]=131

		elif row[fdic["TSA_NUMBER_DESCRIPTION"]] == "Quesnel TSA":
			if row[fdic["SPECIES_CD_1"]] in Spruce+Bal:
				#if row[fdic["SPECIES_PCT_1"]]==:
				#if row[fdic["SPECIES_CD_2"]] in :
				#if row[fdic["SPECIES_PCT_2"]]==:
				if row[fdic["FID_uwr"]]==(-1):
					if 5<row[fdic["SITE_INDEX"]]<=12:
						row[fdic["AU"]]=143
						print "AU143"
					elif 12<row[fdic["SITE_INDEX"]]<=21:
						row[fdic["AU"]]=144
						print "AU144"
					elif 21<row[fdic["SITE_INDEX"]]:
						row[fdic["AU"]]=145
						print"AU145"
			elif row[fdic["SPECIES_CD_1"]] in DougFir:
				#if row[fdic["SPECIES_PCT_1"]]==:
				#if row[fdic["SPECIES_CD_2"]] in :
				#if row[fdic["SPECIES_PCT_2"]]==:
				if row[fdic["FID_uwr"]]==(-1):
					print "species_dougfir"
					if 5<row[fdic["SITE_INDEX"]]<=13:
						row[fdic["AU"]]=140
					elif 13<row[fdic["SITE_INDEX"]]<=21:
						row[fdic["AU"]]=141
					elif 21<row[fdic["SITE_INDEX"]]:
						row[fdic["AU"]]=142
			elif row[fdic["SPECIES_CD_1"]] in ["PL","PLI","PLC"]:
				#if row[fdic["SPECIES_PCT_1"]]==:
				#if row[fdic["SPECIES_CD_2"]] in :
				#if row[fdic["SPECIES_PCT_2"]]==:
				if row[fdic["FID_uwr"]]==(-1):
					if 5<row[fdic["SITE_INDEX"]]<=14:
						row[fdic["AU"]]=146
						print "AU146"
					elif 14<row[fdic["SITE_INDEX"]]<=23:
						row[fdic["AU"]]=147
						print "AU147"
					elif 23<row[fdic["SITE_INDEX"]]:
						row[fdic["AU"]]=148
						print "AU148"
			elif row[fdic["SPECIES_CD_1"]] in ["PA", "PW", "PY"]:
				if row[fdic["SPECIES_PCT_1"]]>70:
					#if row[fdic["SPECIES_CD_2"]] in :
					#if row[fdic["SPECIES_PCT_2"]]==:
					if row[fdic["FID_uwr"]]==(-1):
						#if 5<row[fdic["SITE_INDEX"]]<=14:
						row[fdic["AU"]]=149
						print "AU149"
			elif row[fdic["SPECIES_CD_1"]] in Aspen+Alder+Birch:
				#if row[fdic["SPECIES_PCT_1"]]>70:
				#if row[fdic["SPECIES_CD_2"]] in :
				#if row[fdic["SPECIES_PCT_2"]]==:
				if row[fdic["FID_uwr"]]==(-1):
					if row[fdic["SITE_INDEX"]]<=21:
						row[fdic["AU"]]=150
						print "AU150decid"
					elif 21<row[fdic["SITE_INDEX"]]:
						row[fdic["AU"]]=151
						print "AU151decid"
			if row[fdic["FID_uwr"]]!=(-1):
				if row[fdic["SPECIES_CD_1"]] in DougFir:
					if row[fdic["SPECIES_PCT_1"]]>=40:
						#if row[fdic["SPECIES_CD_2"]] in :
						#if row[fdic["SPECIES_PCT_2"]]==:
						#if row[fdic["SITE_INDEX"]]<=21:
						row[fdic["AU"]]=152
						print "AU152spec1"
						#if row[fdic["SPECIES_CD_1"]] in [DougFir]:
						#if row[fdic["SPECIES_PCT_1"]]>=40:
				if row[fdic["SPECIES_CD_2"]] in DougFir:
					if row[fdic["SPECIES_PCT_2"]]>=40:
						#if row[fdic["SITE_INDEX"]]<=21:
						row[fdic["AU"]]=152
						print "AU152spec2"
					elif row[fdic["SPECIES_PCT_2"]]<40:
						#if row[fdic["SITE_INDEX"]]<=21:
						row[fdic["AU"]]=153
						print "AU152<40"

		elif row[fdic["TSA_NUMBER_DESCRIPTION"]] == "Williams Lake TSA":
			if row[fdic["SPECIES_CD_1"]] in DougFir and row[fdic["SPECIES_PCT_1"]]>=40 and row[fdic["SITE_INDEX"]]>=7:
				if row[fdic["UWR_NUMBER"]] not in ['',None]:
					row[fdic["AU"]]=101
				if row[fdic["BEC_ZONE_CODE"]] in ['IDF', 'SBPS']:
					row[fdic["AU"]]=102
				elif row[fdic["BEC_ZONE_CODE"]] in ['SBS', 'ICH']:
					row[fdic["AU"]]=104
			elif row[fdic["SPECIES_CD_1"]] in DougFir and row[fdic["BEC_ZONE_CODE"]] in ['IDF','SBPS'] and row[fdic["UWR_NUMBER"]] in ['',None]:
				if row[fdic["SITE_INDEX"]]>12:
					row[fdic["AU"]]=109
				elif 7<=row[fdic["SITE_INDEX"]]<=12:
					row[fdic["AU"]]=108
			if row[fdic["SPECIES_CD_1"]] in Cedar or Hem:
				if row[fdic["SITE_INDEX"]]>17:
					row[fdic["AU"]]=112
				elif 7<=row[fdic["SITE_INDEX"]] <=12:
					row[fdic["AU"]]=110
				elif 17<=row[fdic["SITE_INDEX"]] <=12.1:
					row[fdic["AU"]]=111
			if row[fdic["SPECIES_CD_1"]] in Spruce or Bal:
				if row[fdic["SITE_INDEX"]]>17:
					row[fdic["AU"]]=115
				elif 7<=row[fdic["SITE_INDEX"]] <=12:
					row[fdic["AU"]]=114
				elif 12<row[fdic["SITE_INDEX"]] <=17:
					row[fdic["AU"]]=114
			if row[fdic["SPECIES_CD_1"]] in Pine:
				if row[fdic["SITE_INDEX"]]>17:
					row[fdic["AU"]]=118
				elif 7<=row[fdic["SITE_INDEX"]] <=12:
					row[fdic["AU"]]=116
				elif 12<row[fdic["SITE_INDEX"]] <=17:
					row[fdic["AU"]]=117
			if row[fdic["SPECIES_CD_1"]] in DougFir:
				if row[fdic["SITE_INDEX"]] >=7:
					if row[fdic["UWR_NUMBER"]] not in ['',None]:
						row[fdic["AU"]]=105	

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

		elif row[fdic["TSA_NUMBER_DESCRIPTION"]] == "100 Mile House TSA": #this works
			if row[fdic["SPECIES_CD_1"]] in [Aspen, Birch]:
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

			elif row[fdic["SPECIES_CD_1"]] in [Bal, Cedar, Hem]:
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
			if row[fdic["Current_Year"]]<141:
				if row[fdic["SPECIES_CD_1"]] in DougFir:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
						#if row[fdic["BEC_SUBZONE"]]=="xh":
						#if row[fdic["BEC_VARIANT"]]==:
						#if row[fdic["SITE_INDEX"]]==:
						row[fdic["AU"]]=1
					elif row[fdic["BEC_ZONE_CODE"]]== "IDF":
						if row[fdic["BEC_SUBZONE"]] in ["dc","dh","dm","dv","dvw","dw","mc","mh","mm","mmp","mw","un","vk","wc","wcp","wcw","wk","xc","xcw","xh","xk","xm","xv","xvp","xvw","xw"]:
							#if row[fdic["BEC_VARIANT"]]!="2":
							#if row[fdic["SITE_INDEX"]]==:
							row[fdic["AU"]]=1
						elif row[fdic["BEC_SUBZONE"]] == "dk":
							if row[fdic["BEC_VARIANT"]] in ["1","3","4"]:
								#if row[fdic["SITE_INDEX"]]==:
								row[fdic["AU"]]=1
					elif row[fdic["SPECIES_CD_2"]] not in [Hem, Cedar, Bal, "PL", "PLI"]:
						if row[fdic["BEC_ZONE_CODE"]] =="IDF":
							if row[fdic["BEC_SUBZONE"]]=="dk":
								if row[fdic["BEC_VARIANT"]]=="2":
									#if row[fdic["SITE_INDEX"]]==:
									row[fdic["AU"]]=2
						elif row[fdic["BEC_ZONE_CODE"]] =="MS":
							#if row[fdic["BEC_SUBZONE"]]=="xh":
							#if row[fdic["BEC_VARIANT"]]==:
							#if row[fdic["SITE_INDEX"]]==:
							row[fdic["AU"]]=2
					elif row[fdic["BEC_ZONE_CODE"]] in ["ESSF","ICH","IMA","MS","SBPS","SBS"]:
						#if row[fdic["BEC_SUBZONE"]]=="xh":
						#if row[fdic["BEC_VARIANT"]]==:
						if row[fdic["SITE_INDEX"]]>15:
							row[fdic["AU"]]=3
						elif row[fdic["SITE_INDEX"]]<=15:
							row[fdic["AU"]]=5
				elif row[fdic["SPECIES_CD_1"]] in Cedar:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>17:
						row[fdic["AU"]]=7
					elif row[fdic["SITE_INDEX"]]<=17:
						row[fdic["AU"]]=8
				elif row[fdic["SPECIES_CD_1"]] in Hem:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>16:
						row[fdic["AU"]]=9
					elif row[fdic["SITE_INDEX"]]<=16:
						row[fdic["AU"]]=10
				elif row[fdic["SPECIES_CD_1"]] in Bal:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>13:
						row[fdic["AU"]]=11
					elif row[fdic["SITE_INDEX"]]<=13:
						row[fdic["AU"]]=13
				elif row[fdic["SPECIES_CD_1"]] in Spruce:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>14:
						row[fdic["AU"]]=15
					elif row[fdic["SITE_INDEX"]]<=14:
						row[fdic["AU"]]=17
				elif row[fdic["SPECIES_CD_1"]] in Pine:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>14:
						row[fdic["AU"]]=19
					elif row[fdic["SITE_INDEX"]]<=14:
						row[fdic["AU"]]=21

			elif row[fdic["Current_Year"]]>=141:
				if row[fdic["SPECIES_CD_1"]] in DougFir:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
						#if row[fdic["BEC_SUBZONE"]]=="xh":
						#if row[fdic["BEC_VARIANT"]]==:
						#if row[fdic["SITE_INDEX"]]==:
						row[fdic["AU"]]=1
					elif row[fdic["BEC_ZONE_CODE"]]== "IDF":
						if row[fdic["BEC_SUBZONE"]] in ["dc","dh","dm","dv","dvw","dw","mc","mh","mm","mmp","mw","un","vk","wc","wcp","wcw","wk","xc","xcw","xh","xk","xm","xv","xvp","xvw","xw"]:
							#if row[fdic["BEC_VARIANT"]]!="2":
							#if row[fdic["SITE_INDEX"]]==:
							row[fdic["AU"]]=1
						elif row[fdic["BEC_SUBZONE"]] == "dk":
							if row[fdic["BEC_VARIANT"]] in ["1","3","4"]:
								#if row[fdic["SITE_INDEX"]]==:
								row[fdic["AU"]]=1
					elif row[fdic["SPECIES_CD_2"]] not in [Hem, Cedar, Bal, "PL", "PLI"]:
						if row[fdic["BEC_ZONE_CODE"]] =="IDF":
							if row[fdic["BEC_SUBZONE"]]=="dk":
								if row[fdic["BEC_VARIANT"]]=="2":
									#if row[fdic["SITE_INDEX"]]==:
									row[fdic["AU"]]=2
						elif row[fdic["BEC_ZONE_CODE"]] =="MS":
							#if row[fdic["BEC_SUBZONE"]]=="xh":
							#if row[fdic["BEC_VARIANT"]]==:
							#if row[fdic["SITE_INDEX"]]==:
							row[fdic["AU"]]=2
					elif row[fdic["BEC_ZONE_CODE"]] in ["ESSF","ICH","IMA","MS","SBPS","SBS"]:
						#if row[fdic["BEC_SUBZONE"]]=="xh":
						#if row[fdic["BEC_VARIANT"]]==:
						if row[fdic["SITE_INDEX"]]>15:
							row[fdic["AU"]]=4
						elif row[fdic["SITE_INDEX"]]<=15:
							row[fdic["AU"]]=6
				elif row[fdic["SPECIES_CD_1"]] in Bal:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>13:
						row[fdic["AU"]]=12
					elif row[fdic["SITE_INDEX"]]<=13:
						row[fdic["AU"]]=14
				elif row[fdic["SPECIES_CD_1"]] in Spruce:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>14:
						row[fdic["AU"]]=16
					elif row[fdic["SITE_INDEX"]]<=14:
						row[fdic["AU"]]=18
				elif row[fdic["SPECIES_CD_1"]] in Pine:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>14:
						row[fdic["AU"]]=20
					elif row[fdic["SITE_INDEX"]]<=14:
						row[fdic["AU"]]=22
				elif row[fdic["SPECIES_CD_1"]] in Cedar:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>17:
						row[fdic["AU"]]=32
					elif row[fdic["SITE_INDEX"]]<=17:
						row[fdic["AU"]]=33
				elif row[fdic["SPECIES_CD_1"]] in Hem:
					#if row[fdic["SPECIES_CD_2"]] not in ["SX","HW", "CW", "BL", "PL"]:
					#if row[fdic["BEC_ZONE_CODE"]] in ["PP","BG"]:
					#if row[fdic["BEC_SUBZONE"]]=="xh":
					#if row[fdic["BEC_VARIANT"]]==:
					if row[fdic["SITE_INDEX"]]>16:
						row[fdic["AU"]]=34
					elif row[fdic["SITE_INDEX"]]<=16:
						row[fdic["AU"]]=35



		cursor.updateRow(row)
print ('It took ', round((time.time()-Start)/60,1), " minutes to run this script.")