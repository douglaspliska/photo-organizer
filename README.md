To begin the process, run "create.py" which creates the "Source" and "Destination" folders. Then put your photos (including folders 
if there are any) into the "Source" folder. When all of the photos are in the "Source" folder, run the main program 
called "filter.py". After "filter.py" is completes, there will be folders created in the "Destination" folder. These
folders will be in year format and each year's folder will include sub-folders for each month (January, February, etc). 
There will also be two other folders, "Miscellaneous" and "Unsupported". "Miscellaneous" will 
include any non-photo files, if any. "Unsupported" will contain any photos in which metadata could not be read to verify when the 
photo was taken. After running "filter.py", the user can run "remove.py" to remove the "Source" folder as well as any sub-folders
left inside it. This is a handy tool for anyone looking to organize an bunch of photos they've been accumulating for years as well
as provide a way to filter miscellaneous files from their photo folders.