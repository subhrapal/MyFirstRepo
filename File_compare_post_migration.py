##############################################################################################################################
## This python script can be used to compare files post migration															 #
## File's existence in target, it's size,It's Modification time are compared. File permission is not compared. 				 #
## We need to mount the source and target share on to a workstation, from where this script can be run. 					 #
## Python 2.7.x persion should be installed for this script to work. 														 #
## The script need to be run like [ python File_compare_post_migration.py ] 												 #
##					Then it will ask for source and target PATH , and we need to provide that like "c:\SRC" and "D:\TGT"	 #
## This script will create a file called Output.txt, the content of this file is a "|" seperated values						 #
## For any questions pls contact "subhra.pal@dell.com"																		 #
##############################################################################################################################
import os
import sys

SRC=raw_input("Enter the full path for Source Folder:")
TGT=raw_input("Enter the full path for Target Folder:")

def comp_func(src,tgt):
 with open("Output.txt","a") as f:
  f.write("Source PATH|Source File Size|Target PATH|Target Filesize|File Size Matches|File Modification time Matches" )
  f.write("\n")
  for dirpath, dirs, files in os.walk(src):
	for fname in files:
	  try:
		fpath_src=str(os.path.join(dirpath,fname))
		src_fsize=os.path.getsize(fpath_src)
		src_f_mtime=os.path.getmtime(fpath_src)
		fpath_tgt=fpath_src.replace(src,tgt,1)
		if os.path.isfile(fpath_tgt):
 			tgt_fname=fpath_tgt
			tgt_fsize=os.path.getsize(fpath_tgt)
			tgt_f_mtime=os.path.getmtime(fpath_tgt)
			if src_fsize == tgt_fsize:
			     match='FILE Size MATCHED'
			else:
			     match='FILE Size NOT MATCHED'
			if src_f_mtime == tgt_f_mtime:
				fmtime_match='Modification Time matched'
			elif src_f_mtime > tgt_f_mtime :
				fmtime_match='Source File mtime latest'
			else:
				fmtime_match='Target File mtime latest'
		else:
			tgt_fname='File not found'
			tgt_fsize='NOT Applicable'
			match='NOT Applicable'
			fmtime_match='NOT Applicable'
		f.write(fpath_src + "|" + str(src_fsize) + "|" + tgt_fname + "|" + str(tgt_fsize) + "|" + match + "|" + fmtime_match)
		f.write("\n")
	  except:
		f.write(fpath_src + "|||||"+"This file could not be processed by the script for some Error. \n")

comp_func(SRC,TGT)