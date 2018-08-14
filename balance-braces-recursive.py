import re

regexCheck = re.compile(r"\{\}|\[\]|\(\)")
braces = "{)[](}]}]}))}(())("

def usingRegex(row):
	if len(row) == 0:
		return True

	if not re.search(regexCheck, row):
		return False

	return usingRegex(re.sub(regexCheck, "", row))

print(usingRegex(braces))
