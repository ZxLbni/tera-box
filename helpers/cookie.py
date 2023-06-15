import re
def parseCookieFile(cookiefile):
    cookies = {}
    with open(cookiefile, 'r') as fp:
        for line in fp:
            if not re.match(r'^\#', line):
                lineFields = line.strip().split('\t')
                if len(lineFields) >= 7:  # Check if line has enough fields
                    cookies[lineFields[5]] = lineFields[6]
    return cookies