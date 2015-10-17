#!	readCensusExcel.py
#	readCensusExcel.py - Tabulates population and number of 
#	census tracts for each county.

import openpyxl
import pprint
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # diables logging if uncommented.

print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# TODO: Fill in countyData with each County's population and tracts.
print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
	# Each row in the spreadsheet has data for one census tract.
	state 	= sheet['B' + str(row)].value
	county 	= sheet['C' + str(row)].value
	pop 	= sheet['D' + str(row)].value

	# Make sure the key for this state exists.
	# Note:setdefault creates a new dictionary key and value pair if nothing exists.
	countyData.setdefault(state, {}) 
	# Make sure the key for this county in this state exists.
	countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

	# Each row represents one census tract, so increment by one.
	countyData[state][county]['tracts'] += 1
	logging.debug('Adding count to tracts...')
	# Increase the county pop by the pop in this census tract.
	countyData[state][county]['pop'] += int(pop)
	logging.debug('Adding population to ' + str(countyData[state][county]) + ' population total.')

# TODO: Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')