import sys


fields = [
	'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 
	'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 
	'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 
	'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 
	'num_access_files', 'num_outbound_cmds', 'is_hot_login', 
	'is_guest_login', 'count', 'srv_count', 'serror_rate', 
	'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate:', 
	'same_srv_rate:', 'diff_srv_rate:', 'srv_diff_host_rate:', 
	'dst_host_count:', 'dst_host_srv_count:', 'dst_host_same_srv_rate:', 
	'dst_host_diff_srv_rate:', 'dst_host_same_src_port_rate:', 
	'dst_host_srv_diff_host_rate:', 'dst_host_serror_rate:', 
	'dst_host_srv_serror_rate:', 'dst_host_rerror_rate:', 
	'dst_host_srv_rerror_rate:', 'class'
]

numeric = [
	True, False, False, False, True, True, False, True, True, True, 
	True, False, True, False, False, True, True, True, True, True, 
	False, False, True, True, True, True, True, True, True, True, 
	True, True, True, True, True, True, True, True, True, True, 
	True, False
]

#~ numeric = [
	#~ False for i in xrange(42)
#~ ]


def get_possible_values(input_lines):
	# computing possible values
	values = [ set() for i in xrange(len(fields)) ]
	for l in input_lines:
		l.replace('.\n', '')
		attributes = l.replace('.\n', '').split(',')
		for i,att in enumerate(attributes):
			if not numeric[i]:
				values[i].add(att)
	return values

def to_string_attribute_values(values_set):
	return '{'+', '.join(list(values[i]))+'}'
	

if __name__ == '__main__':
	input_name = sys.argv[1]
	output_name = sys.argv[2]
	f = open(input_name, 'r')
	input_lines = f.readlines()
	
	values = get_possible_values(input_lines)
	#~ for i in xrange(42):
		#~ print('field: {} values: {}'.format(fields[i],len(values[i])))
	
	header = ''
	header += '@relation kddcup\n'
	for i in xrange(len(fields)):
		if numeric[i]:
			header += '@attribute {} numeric\n'.format(fields[i])
		else:
			header += '@attribute {} {}\n'.format(fields[i], to_string_attribute_values(values[i]))
	header += '@data\n'
	
	# writing file
	output_file = open(output_name, 'w')
	output_file.write(header+'\n')
	
	# adding content
	for i in input_lines:
		output_file.write(i.replace('.\n', '')+'\n')
		
	output_file.close()
	

