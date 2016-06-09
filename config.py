#new paste defaults
defaults = {
	'ttl': 1,
	'lexer': 'auto',
	'burn': -1,
	'paste': '',
}

#paste options
paste_limits = {
	'ttl_max': 731, #maximum allowed paste ttl in hours, extra decimals 
	'ttl_min': 0, #minimum allowed paste ttl in hours
	'burn_max': 1000, #maximum allowed reads before burning paste [default: 1000]
	'burn_min': 1, #minimum allowed reads before burning paste [default: 1]
}

token_len =  6 #delete token length in bytes/characters

#flask configuration
secret_key = 'some_secret'
max_content_length = 2 * 1024 * 1024 #max form upload size in bits
domain = 'http://localhost:5000'

#postgresql configuration
dsn = "host=localhost port=5432 dbname='pastebin' user='pastebin' password='1234'"

#paste url
url_len = 1 #minimum paste url length in characters
url_alph = tuple("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghkmnpqrstuvwxyz") #alphabet used to generate paste url
base = len(url_alph)

#return messages
empty_paste = "pls, actually paste something k?\n"
invalid_ttl = "ttl must be between " + str(paste_limits['ttl_min']) + " and " + str(paste_limits['ttl_max']) +" hours.\n"
invalid_burn = "burn count must be between " + str(paste_limits['burn_min']) + " and " + str(paste_limits['burn_max']) + ".\n" 
msg_err_404 = "404 - Not Found.\n"
msg_err_401 = "401 - Unauthorized - check your delete token.\n"
msg_paste_deleted = "paste deleted successfully.\n"


#form options
ttl_options = [
	('5 minutes', 0.0833),
	('15 minutes', 0.25),
	('30 minutes', 0.5),
	('1 hour', 1),
	('3 hours', 3),
	('6 hours', 6),
	('12 hours', 12),
	('1 day', 24),
	('3 days', 72),
	('1 week', 168),
	('2 weeks', 336),
	('1 month', 730),
]

lexers_common = [
	('Bash', 'bash'),
	('C', 'c'),
	('C++', 'cpp'),
	('C#', 'csharp'),
	('Python', 'python'),
	('Ruby', 'ruby'),
	('Go', 'go'),
	('Perl', 'perl'),
	('PHP', 'php'),
	('CSS', 'css'),
	('HTML', 'html'),
	('JavaScript', 'javascript'),
	('JSON', 'json'),
	('XML', 'xml'),
	('SQL', 'sql'),
]

