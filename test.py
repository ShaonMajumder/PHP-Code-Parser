import re

"""
text="<h3 class="heading">General Purpose</h3>"
pattern="(<.*?>)(.*)(<.*?>)"
pattern="(h3)(.*)(h3)"

g=re.search(pattern,text)
g = g.group(2)
print(g)


text="echo(hello);/*one*/echo(hello2);/*two*/echo(hello3);"
pattern="(/\*)(.*)(\*/)"
g=re.search(pattern,text)
g = g.group(2)
print(g)

text="echo(hello);/*one*/echo(hello2);/*two*/echo(hello3);"
if '/*' in text and '*/' in text:
	text="echo(hello);/*one*/echo(hello2);/*twoecho(hello3);"
	i = -1
	break_ = True
	while(break_ and i < len(text)-1):
		
		i = i + 1
		print(i)
		if text[i] == '/' and text[i+1] == '/':
			sin_c = text[ text.index('//') : ]
			text = text.replace(sin_c,'')

		elif text[i] == '/' and text[i+1] == '*':
			
			try:
				mlend = text.index('*/')
				fi_com = text[ i : text.index('*/')+2]
				text = text.replace(fi_com,'')
				i = -1
			except ValueError:
				#continue to next line
				ignore = True
				fi_com = text[ i : ]
				text = text.replace(fi_com,'')
				break_ = False
		#if(break_): break
			
print(text)
"""
line = "echo(hello);/*one*/echo(hello2);/*twoecho(hello3);"
clean_code = ''
loop = True
while(loop):
	if '//' in line and '/*' in line:
		sli = line.index('//')
		mli = line.index('/*')
		if sli < mli:
			line = line.replace( get_single_line_comment(line) ,'')
		else:
			#multi before
			if '/*' in line and '*/' in line:
				com = line[line.index('/*'):line.index('*/')+2]
				line = line.replace(com,'')
				#again run loop on same line
			elif '/*' in line:
				#before /*
				line = line[:line.index('/*')]
				#continue to next line
				#loop = False
	elif '//' in line:
		line = line.replace( get_single_line_comment(line) ,'')
	elif '/*' in line:
		if '/*' in line and '*/' in line:
			com = line[line.index('/*'):line.index('*/')+2]
			line = line.replace(com,'')
			#again run loop on same line
		elif '/*' in line:
			line = line[:line.index('/*')]
			#continue to next line
	else:
		clean_code = line
		loop = False


print(clean_code)