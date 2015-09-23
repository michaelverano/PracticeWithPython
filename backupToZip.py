#! python3
# backupToZip.py 	- copies an entire folder and its contents into 
# 					  a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
	# Backup the entire contents of "folder" into a ZIP file.

	folder = os.path.abspath(folder)	# Make sure folder is absolute.

	# Figure out the filename this code should use based on 
	# what files already exist.

	number = 1

	while True:
		
		zipFilename = os.path.basename(folder) + '_backup_' + str(number) + '.zip'
		print('test')
		
		if not os.path.exists(zipFilename):
			break 	# breaks out of the loop, but doesn't exit program.

		number = number + 1
		print('test 2')

	# TODO: Create the ZIP file.
	print('Creating %s....' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')


	# TODO: Walk the entire folder tree and compress the files in each folder.
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in %s...' % (foldername))
		# Add the current folder to the Zip file.
		backupZip.write(foldername)
		
		# Add all the files in the folder to the ZIP file.
		for filename in filenames:
			newBase = os.path.basename(folder) + '_backup_'
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue	# don't back up the backup ZIP files
			backupZip.write(os.path.join(foldername, filename))

		backupZip.close()
		print('Done')
		break
	exit()

if __name__ == '__main__':
	backupToZip('/home/verano/Documents/PythonProjects')