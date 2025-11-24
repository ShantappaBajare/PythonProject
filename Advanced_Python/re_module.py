"""
What is a Regular Expression?

A Regular Expression (Regex) is a pattern used to:
Search,Match,Validate,Extract and Replace text in strings.
Python provides regex via the built-in module: re module



"""

"""
Quantifiers:can be used to specify the number of occurrences to match
a: exactly 1 match
a+: atleast 1 match
a*:any number of match including 0 also
a?:atmost 1 a either a or zero number also
"""

# import re
# matcher=re.finditer("a?","abaabaab")
# for match in matcher:
#     print(match.start(),"   ",match.group())

"""re.match(): to check the given pattern at the begining of the target string, 
               if then returns match object else returns none """
# import re
# s=input("Enter a pattern: ")
# m=re.match(s,"abcdefgh")
# if m!=None:
#     print("match is available at the beginning of string")
#     print("start index:{} and end index:{}".format(m.start(),m.end()))
# else:
#     print("no match")


"""re.fullmatch(): pattern should match the complete target string """

# import re
# s=input("Enter a pattern: ")
# m=re.fullmatch(s,"abcdefgh")
# if m!=None:
#     print("fullstring is available")
# else:
#     print("no match")

"""re.search(): Searches a string and returns the first match """

# import re
# s=input("Enter a pattern: ")
# m=re.search(s,"abaabaaab")
# if m!=None:
#     print("match is available")
#     print("first ocurance with start index:{} and end index:{}".format(m.start(),m.end()))
# else:
#     print("no match")

"""re.findall(): Searches a string and returns all the matched object in a list """
# import re
# l=re.findall('[0-9]','a7b9k6z')
# print(l)

# import re
# l=re.findall('\W','a7b#@&*9k6z')
# print(l)

"""re.finditer(): it returns iterator of matched objects and it gives start and end and group data """
# import re
# matcher=re.finditer("a?","abaabaab")
# for match in matcher:
#     print(match.start(),"   ",match.group())

"""re.sub(): Subtitute/replace the matched string with relpace string string """

# import re
# s=re.sub('\d','#','a7b9kt')
# print(s)

"""re.subn(): subtitutes the string and gives the result string and number of substitutes in tuples """
"""re.split(): split the target string based on pattern """
"""re.compile():  """

""" file operations """
# import re
#
# f1 = open("input.txt", "r")
# f2 = open("output.txt", "w")
#
# for line in f1:
#     nums = re.findall(r'[6-9]\d{9}', line)
#     for num in nums:
#         f2.write(num + "\n")
#
# print("Extracted all mobile numbers into output.txt")
#
# f1.close()
# f2.close()


"""web scraping using regular expressions:"""

#Extract all links from a webpage
# import re
# import urllib.request
#
# url = "https://www.youtube.com/"
# response = urllib.request.urlopen(url)
# html = response.read().decode()
#
# # Regex to extract all links
# links = re.findall(r'href="(.*?)"', html)
#
# for link in links:
#     print(link)


#Extract Emails from a Webpage
# import re
# import urllib.request
#
# url="https://mail.google.com"
# response=urllib.request.urlopen(url)
# html=response.read().decode()
#
# emails=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.\w+',html)
# for email in emails:
#     print(email)

"""Extract Headings (Example: <h1>, <h2>)"""

import re
import urllib.request

url = "https://www.google.com/"
html = urllib.request.urlopen(url).read().decode()

title = re.findall(r'<title>(.*?)</title>', html)


for h in title:
    print(h)
