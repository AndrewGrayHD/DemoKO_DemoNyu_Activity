
#init translation code dictionary
culture_code={'english': 'en-US',
                  'chinese':'zh-CH'}

#transform function
def get_culture_code(key):
	
	try:
		code=culture_code[key]
	except:
		code=key

	return code

def unpivot_data(data:dict,column_index):
	
	dict_index=1
	final_data={}

	for values in data.values():
		for key in list(values.keys()):
			final_data.update({dict_index:{}})
			if  key not in column_index:
				for index in column_index:
					final_data[dict_index][index]=values[index]
				
				final_data[dict_index]['culture']=get_culture_code(key)
				final_data[dict_index]['values']=values[key]
				dict_index+=1

	return 	final_data


	
#set data
data={1:{'code':'hi','text':'Hi','chinese':'你好'},
      2:{'code':'good_bye','text':'Good Bye','chinese':'再见', 'english':'Bye Bye'}}


#print original table and transform table
print('******** START ORIGINAL DATA **********')

for values in data.values():
	columns=[]
	for key in list(values.keys()):
		if "{:<20}|".format(get_culture_code(key)) not in columns:
			columns.append("{:<20}| ".format(get_culture_code(key)))
			
print(f"{'-' * 89}")	
print(''.join(columns))
print(f"{'-' * 89}")

for values in data.values():
	orig_values = ["{:<20}|".format(values[key]) for key in list(values.keys()) ]
	print(''.join(orig_values))
	print(f"{'-' * 89}")	

print('******** END ORIGINAL DATA **********')
print("\n")

data=unpivot_data(data,column_index=['code','text']).copy()

print('******** START TRANSFORM DATA **********')

for values in data.values():
	columns=[]
	for key in list(values.keys()):
		if "{:<20}|".format(get_culture_code(key)) not in columns:
			columns.append("{:<20}| ".format(get_culture_code(key)))
			
print(f"{'-' * 89}")	
print(''.join(columns))
print(f"{'-' * 89}")

for values in data.values():
	orig_values = ["{:<20}|".format(values[key]) for key in list(values.keys()) ]
	print(''.join(orig_values))
	print(f"{'-' * 89}")	

print('******** END TRANSFORM DATA **********')
print("\n")
