from pathlib import Path
pathname=r"/storage/emulated/0/WOW"
pathnam=Path(pathname)
import os,time
begin_time=time.time()
if pathnam.exists():
	filename="gamefile.dat"
	path=pathname+filename
	p=Path(path)
	if p.exists():
		new_file=open(filename, 'w')
		new_file.write('')
		new_file.close()
		print(f"Successfully reseted '{filename}'")
		players = open("players.dat", 'w')
		players.write ('')
		players.close ()
	else:
		new_file=open(filename, 'w')
		new_file.close()
		print(f"Successfully created '{filename}'")
		players = open("players.dat", 'w')
		players.write ('')
		players.close ()
else:
	os.chdir(r"/storage/emulated/0")
	os.mkdir(r'/WOW')
	new_file=open('gamefile.dat','w')
	print("Successfully initialized 'gamefile.dat'")
	new_file.close()
	players = open("players.dat", 'w')
	players.write ('')
	players.close ()
end_time=time.time()
time_taken=round(end_time-begin_time)
print("Process Completed\nTime taken>>>"+str(time_taken),"secs")
