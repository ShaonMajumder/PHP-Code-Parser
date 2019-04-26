# PHP-Code-Parser
	## Work-Flow	
	PHP Class parser > Start reading from first
	Ignore Comments
		>> Get every lines as a list
		>> Detect // in a line, and remove all lines from //(*)\n
		>> Detect /* from whole file and remove all text from /*
														(*)
														*/
	Detect 'Class Name'
		>> Detect Class
		>> Detect ClassName
		>> if detected as 'class' keyword, then take text from 'class (*){' > trim the text for spaces. that is the class name

	Detect Inside text of Class and function
		>> Remove Comments
		>> Detect class ignorinng inside {} blocks
		>> First Detect and save Class, remove class from Source
		>> Then Detect and save Independent Function, remove function from Source
		>> Then Identify Doc String in second line with  /*/// ///*/ and take text inside it and register it as object descriptor.
		> Give a Track Flag to doc string so that it can choose which object to register
		> Detect Docstring
		> Register

	## Issues
		Docstring is not removing by remove_all_comments()