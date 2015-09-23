#! 	python3
#	renameDates.py - renames filenames with American MM-DD-YY date formats
# 	to European DD-MM-YY.

import shutil, os, re

#	Create a regex that matches files with the American date format.
datePattern = re.compile(r"""(.*?)	# all text before the date.
			((0|1)?\d)-				# one or two digits for month
			((0|1|2|3)?\d)-			# one or two digits for the day
			((19|20)\d\d)			# four digits for th year.
			(.*?)$					# all text after the date.

	""", re.VERBOSE)

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)

	# TODO: Skip files without a date.
	if mo == None:
		continue

	# TODO: Get the different parts of the filename.
	beforePart 	= mo.group(1)
	monthPart 	= mo.group(2)
	dayPart		= mo.group(4)
	yearPart	= mo.group(6)
	afterPart	= mo.group(8)

	# Form the European-style filename.
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	# Get the full, absolute file paths.
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)

	# TODO: Rename the files.
	print('Rename "%s" to "%s"...' % (amerFilename, euroFilename))
	#shutil.move(amerFilename, euroFilename) # uncomment after testingself.