import os
from shutil import copyfile

song_file_location = 'F:\\musics\\'
group_location = song_file_location + '\\group'
if not os.path.exists(group_location):	
	os.mkdir(group_location)

print('Numer of files : [' + str(len(os.listdir(song_file_location))) + ']')

for folder_name, subfolders, file_names in os.walk(song_file_location):
	for file_name in file_names:
		print('- File name is : [' + file_name + ']')
		if  file_name.startswith('['):
			singer_name = file_name[1 : file_name.find(']')]
		elif '-' in file_name:
			singer_name = file_name.split('-')[0].strip()
		if singer_name is not None:
			print('- Find singer: [' + singer_name + ']')
			singer_location = group_location + '\\' + singer_name
			if not os.path.exists(singer_location):	
				os.mkdir(singer_location)
				print('- New singer : [' + singer_name + ']')
			copyfile(song_file_location + file_name, singer_location + '\\' + file_name)
			print('- Moved : [' + file_name + '].')

			

