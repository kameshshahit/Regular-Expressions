import re
#Matching,Extracting,Spliting,Replacing
# =============================================================================
# pattern = re.compile("(ban)")
# for i, line in enumerate(open('SampleText.txt')):
#     for match in re.finditer(pattern, line):
#         print ('Found on line %s: %s' % (i+1, match.groups()))
# =============================================================================
# '
#+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
#* -- 0 or more occurrences of the pattern to its left
#? -- match 0 or 1 occurrences of the pattern to its left       
        ☻
#Leftmost & Largest
#First the search finds the leftmost match for the pattern, and second it tries to use up as much of the string 
#as possible -- i.e. + and * go as far as possible (the + and * are said to be "greedy").
textfile = open('SampleText.txt', 'r')
filetext = textfile.read()
textfile.close()

htmlfile = open('Alice in Wonderland.txt', 'r',encoding="utf8")
Alicetext = htmlfile.read()
htmlfile.close()

# =============================================================================
#Sample 1: Search Method
# =============================================================================
#The 'r' in front tells Python the expression is a raw string. In a raw string, escape sequences are not parsed. 
#For example, '\n' is a single newline character. But, r'\n' would be two characters
match=re.search(r'111.',filetext)
if match:
    print('found',match.group())
else:
    print('No found!!')

#The basic rules of regular expression search for a pattern within a string are:

#The search proceeds through the string from start to end, stopping at the first match found
#All of the pattern must be matched, but not all of the string
#If match = re.search(pat, str) is successful, match is not None and 
#in particular match.group() is the matching text
  
# =============================================================================
#Sample 1: MAtch Method
# =============================================================================
match_var=re.match(r'esh',filetext)
if match_var:
    print('found',match_var.group())
else:
    print('No found!!')


#Note:if you need to match at the beginning of the string, or to match the entire string use match. It is faster. Otherwise use search.
# =============================================================================
#Sample 2: Group Extraction
# =============================================================================
match=re.search(r'([\w.-]+)@([\w.-]+)',filetext)
if match:
    print('found',match.group())
    print('found',match.group(1))
    print('found',match.group(2))
else:
    print('No found!!')
# =============================================================================
#Sample 3: FindAll Method
# =============================================================================
match=re.findall(r'[\w.-]+@[\w.-]+',filetext)
print(match)
for email in match:
    print(email)



   
# =============================================================================
#Sample 4: FindAll Method with Groups
# =============================================================================
match=re.findall(r'([\w.-]+)@([\w.-]+)',filetext)
print(match)
for email in match:
    print(email[0])
    print(email[1])
 
#match = re.search(r'word:\w\w\w', str)
## If-statement after search() tests if it succeeded
#if match:
#  print ('found', match.group()) ## 'found word:cat'
#else:
#  print ('did not find')
    
    
    
# =============================================================================
#Sample 5: Flags ignorecase
# =============================================================================
  match_result=re.match(r'kamesh',filetext)
  print(match_result)
  if match_result:
      print ('found')
  else:
      print ('No found')       



# =============================================================================
#Sample 6: Flags multiline
# =============================================================================
match=re.search(r'abc\nxyz',filetext,re.MULTILINE)
print(match)
if match:
     print ('found')
else:
     print ('No found')
    


# =============================================================================
#Sample 7: Split Function
# =============================================================================
match=re.findall(r'[\w.-]+@[\w.-]+',filetext)
print(match)
for email in match:
    userid,domain = re.split("@",email)
    print(userid)
    print(domain)




# =============================================================================
#Sample 8: Sub Function
# =============================================================================

#re.sub(pat, replacement, str) 

print(re.sub(r'[\w.-]+@[\w.-]+',r'pru.com',filetext))

# =============================================================================
#Sample 8: Sub Function with group
# =============================================================================

#re.sub(pat, replacement, str) 

print(re.sub(r'([\w.-]+)@([\w.-]+)',r'\1@pru.com',filetext))



