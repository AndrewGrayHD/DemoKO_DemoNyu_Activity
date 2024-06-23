
#set initial translation culture dictionary
culture_code={	
		'english': 'en-US',
            	'chinese':'zh-CH'
			 }

#transform function
def get_culture_code(key):
	
	try:
		code=culture_code[key]
	except:
		code=key

	return code

def unpivot_data(data:dict,column_index,column_name):
	
	dict_index=1
	final_data={}

	#1
	for values in data.values():
		2#
		for key in list(values.keys()):
			final_data.update({dict_index:{}})
			if  key not in column_index:
				#3
				for index in column_index:
					final_data[dict_index][index]=values[index]
				#4		
				final_data[dict_index][column_name]=key
				final_data[dict_index]['values']=values[key]
				dict_index+=1
	#5
	return 	final_data


	
#set data
data={1:{'code':'hi','text':'Hi','chinese':'你好'},
      2:{'code':'good_bye','text':'Good Bye','chinese':'再见', 'english':'Bye Bye'}}


#print original table and transform table
print('******** START ORIGINAL DATA **********')

#columns
columns=[]
for values in data.values():
	for key in list(values.keys()):
		if key not in columns:
			columns.append(key)
			
print(f"{'-' * 120}")	
print(''.join(["|{:<20}".format(get_culture_code(key)) for key in columns]))
print(f"{'-' * 120}")

#values
for values in data.values():
	orig_values=[]
	for col in columns:
		try:
			orig_values.append("|{:<20}".format(values[col]))
		except:
			orig_values.append("|{:<20}".format(''))

	print(''.join(orig_values))
	print(f"{'-' * 120}")	

print('******** END ORIGINAL DATA **********')
print("\n")



print('******** START TRANSFORM DATA **********')

#Call Transfrom from columns to rows function
data=unpivot_data(data,column_index=['code','text'],column_name='culture').copy()


#columns
columns=[]
for values in data.values():
	for key in list(values.keys()):
		if key not in columns:
			columns.append(key)
			
print(f"{'-' * 89}")	
print(''.join(["|{:<20}".format(get_culture_code(key)) for key in columns]))
print(f"{'-' * 89}")

#values
for values in data.values():
	orig_values = ["|{:<20}".format(get_culture_code(values[key])) for key in list(values.keys()) ]
	print(''.join(orig_values))
	print(f"{'-' * 89}")	

print('******** END TRANSFORM DATA **********')
print("\n")
