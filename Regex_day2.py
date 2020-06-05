
#Commands to be exeucted on Regex101.com
#String to be tested:
#


import re
# =============================================================================
# 111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 
# yahod
# yahd 
# yahoood
# PASS
# 01/12/1987
# kames_.-h3wsha4hit@gmail.com
# john@doe.com
#  
# k@k.com
# band
# \d
# kamesh shah
# bad "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
# 111.222.333.123 HOME - [ 01/02/1998 :01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
# 111.222.333.123 AWAY - [ 01/02/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 200 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
# 111.222.333.123 AWAY - [ 01/02/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 200 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
# user@host> file show /var/log/processes Feb 22 08:58:24 router1 snmpd[359]:
# %DAEMON-3-SNMPD_TRAP_WARM_START: trap_generate_warm: SNMP trap: warm start
# Feb 22 20:35:07 router1 john@doe.com snmpd[359]:
# %DAEMON-6-SNMPD_THROTTLE_QUEUE_DRAINED: trap_throttle_timer_handler: cleared all throttled traps
# Feb 23 07:34:56 router1 john@doe.com snmpd[359]:
# %DAEMON-3-SNMPD_TRAP_WARM_START: trap_generate_warm: SNMP trap: warm start
# Feb 23 07:38:19 router1 snmpd[359]:
# %DAEMON-2-SNMPD_TRAP_COLD_START: trap_generate_cold: SNMP trap: cold start
#  =============================================================================
#  192.168.198.92 - - [22/Dec/2002:23:08:37 -0400] "GET 
#     / HTTP/1.1" 200 6394 www.yahoo.com 
#     "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1...)" "-"
#  192.168.198.92 - - [22/Dec/2002:23:08:38 -0400] "GET 
#     /images/logo.gif HTTP/1.1" 200 807 www.yahoo.com 
#     "http://www.some.com/" "Mozilla/4.0 (compatible; MSIE 6...)" "-"
#  192.168.72.177 - - [22/Dec/2002:23:32:14 -0400] "GET 
#     /news/sports.html HTTP/1.1" 200 3500 www.yahoo.com 
#     "http://www.some.com/" "Mozilla/4.0 (compatible; MSIE ...)" "-"
#  192.168.72.177 - - [22/Dec/2002:23:32:14 -0400] "GET 
#     /favicon.ico HTTP/1.1" 404 1997 www.yahoo.com 
#     "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3)..." "-"
#  192.168.72.177 - - [22/Dec/2002:23:32:15 -0400] "GET 
#     /style.css HTTP/1.1" 200 4138 www.yahoo.com 
#     "http://www.yahoo.com/index.html" "Mozilla/5.0 (Windows..." "-"
#  192.168.72.177 - - [22/Dec/2002:23:32:16 -0400] "GET 
#     /js/ads.js HTTP/1.1" 200 10229 www.yahoo.com 
#     "http://www.search.com/index.html" "Mozilla/5.0 (Windows..." "-"
#  192.168.72.177 - - [22/Dec/2002:23:32:19 -0400] "GET 
#     /search.php HTTP/1.1" 400 1997 www.yahoo.com 
#     "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ...)" "-"
#  =============================================================================
# 
# =============================================================================

 

##### Whole numbers
\d\d\d - \D act as negation
\w\w\w - \W act as negation
[a-z],[0-9] - Match in range
[^x-z^X-Z] Negated character Class 
\\d - Escaping the character.
b[ad] - matches either a or d not both
b[df]d- Must match one
(abc) - matches a complete set
(ba[l-z]) - nested expressions.
(ba[l-z]|d) Matching an alternate:
    ba[l-z]
    bad
    yaho
    yahodd
yaho?d - Adding question mark make the character before it optional in occurence
yaho*d - Asterisk matches when the character preceding * matches 0 or more times.It should be same character
kamesh\s - Identifying white space. (/S whitespace negation)
+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
* -- 0 or more occurrences of the pattern to its left
? -- match 0 or 1 occurrences of the pattern to its left  

Quantifiers:
P\w+ - P followed by letters
P\w{3} - P followed by 3 letters
P\w{2,4} - Two to four times
P\w{3,}	Three or more times
pa
paaaaaa
paaa
pa

Email: ([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})
date(dd/mm/yyyy):([1-9]|0[1-9]|[12][0-9]|3[01])\D([1-9]|0[1-9]|1[012])\D(19[0-9][0-9]|20[0-9][0-9])
Camelcase: ([A-Z][a-z0-9]+)
ipv4: (\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]){3}
domains: ([a-z][a-z0-9-]+(\.|-*\.))+[a-z]{2,6}
http:(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?
email:[\w.-]+@[\w.-]+






