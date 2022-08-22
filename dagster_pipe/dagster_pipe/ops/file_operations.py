from dagster import op, Out


import os
import glob
import logging



@op(out={"value1": Out(is_required=True), "value2": Out(is_required=True)})
def get_csv_path(context):
	path = r'/home/kshitij/Downloads/dataset/'
	all_files = glob.glob(path + "/*.csv")
	context.log.info(all_files[0])
	context.log.info(all_files[1])
	return all_files[0], all_files[1]

	

@op(out={"table1": Out(is_required=True), "table2": Out(is_required=True)})
def get_tablename(context):
	path = r'/home/kshitij/Downloads/dataset/'
	all_files = glob.glob(path + "/*.csv")
	tablename1 = (os.path.basename(all_files[0]))
	tablename2 = (os.path.basename(all_files[1]))
	context.log.info(tablename1[:-4])
	context.log.info(tablename2[:-4])
	return tablename1[:-4], tablename2[:-4]
