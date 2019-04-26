import codecs
import re

def read_file(filename):
	with codecs.open(filename, "r", encoding="utf-8") as file_reader:
		lines = file_reader.readlines()
	return lines

def get_single_line_comment(line):
	if '//' in line:
		return line[line.index('//'):]
	else:
		return False

def get_single_line_comments(lines):
	comments_ = []
	for line in lines:
		comment = get_single_line_comment(line)
		if(comment): comments_.append(comment)
	return comments_

def get_multi_line_comments(lines):
	one_multi = ""
	all_multi = []
	read = False
	cursor = -1
	while(cursor<len(lines)-1):
		cursor = cursor + 1
		line = lines[cursor]
		if '*/' in line:
			read = False
			for i in range(len(line)) :
				if line[i] == '*' and line[i+1] == '/':
					one_multi = one_multi + line[:i+2]
					newline = line[i+2:]
			
			lines[cursor] = newline
			cursor = cursor - 1
			all_multi.append(one_multi)
			one_multi = ''
		elif(read):
			one_multi = one_multi + line
		elif '/*' in line:
			read = True
			for i in range(len(line)) :
				if line[i] == '/' and line[i+1] == '*':
					one_multi = one_multi + line[i:]

	return all_multi

def remove_all_single_comments(lines):
	clean_code = ''
	single_line_comments = get_single_line_comments(lines)
	for line in lines:
		
		#single_line_comments deduct  from line 
		
		for slc in single_line_comments:
			if slc in line:
				line = line.replace(slc,'')
				break
		clean_code = clean_code + line
	return clean_code

def single_line(line,multi_read):
	clean_line = ''
	loop = True
	if '*/' in line:
		#after */
		line = line[line.index('*/')+2:]
		multi_read = False
	while(loop and not multi_read):
		if '//' in line and '/*' in line:
			sli = line.index('//')
			mli = line.index('/*')
			if sli < mli:
				if '\r\n' in line:
					bl = '\r\n'
				elif '\n' in line:
					bl = '\n'
				line = line.replace( get_single_line_comment(line) ,'')  + bl
			else:
				#multi before
				if '/*' in line and '*/' in line:
					com = line[line.index('/*'):line.index('*/')+2]
					line = line.replace(com,'')
					#again run loop on same line
				elif '/*' in line:
					#before /*
					line = line[:line.index('/*')]
					#continue to next line # correct
					multi_read = True
					loop = False
		elif '//' in line:
			if '\r\n' in line:
				bl = '\r\n'
			elif '\n' in line:
				bl = '\n'
			line = line.replace( get_single_line_comment(line) ,'')  + bl
		elif '/*' in line:
			if '/*' in line and '*/' in line:
				com = line[line.index('/*'):line.index('*/')+2]
				line = line.replace(com,'')
				#again run loop on same line
			elif '/*' in line:
				#before /*
				line = line[:line.index('/*')]
				#continue to next line # correct
				multi_read = True
				loop = False
		else:
			clean_line = line
			loop = False
	
	return clean_line,multi_read

def remove_all_comments(lines):
	# escape character not handled
	multi_read = False
	clean_code = []
	for line in lines:
		clean_line,multi_read= single_line(line,multi_read)
		clean_code.append(clean_line)
	return clean_code

def get_className(line):
	pattern='(class )(.*)({)'
	g=re.search(pattern,line)
	g = g.group(2)
	return g.strip()

def findnth(haystack, needle, n):
	 return [m.start() for m in re.finditer(needle,haystack)][n]

def get_block_end_position(block_start_position,block_start_char,block_end_char):
	#score_based algo
	sc = 0
	ec = 1
	c = 1
	while(sc != ec):
		last_p = findnth(string,'}',c)
		s_str = string[string.index('{'):last_p+1]
		sc = s_str.count('{')
		ec = s_str.count('}')
		c = c + 1
	
	return last_p

def return_class(string):
	#class detector
	if ' class ' in string:
		suff = '\nclass '
	elif '\nclass ' in string:
		suff = '\nclass '
	classname_ = string[ string.index(suff) + len(suff) : string.index('{') ]
	classname = classname_.strip()
	block_start_position = string.index(suff + classname_) + len(suff + classname_)
	block_stop_position = get_block_end_position(block_start_position,'{','}')
	class_txt = suff + classname_ + string[block_start_position:block_stop_position+1]
	return class_txt

lines = read_file('sample.php')
lines = remove_all_comments(lines)
string = ''.join(lines)
print(return_class(string))