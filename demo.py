# Remove Punctuations From a String
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."
pfree=''
for x in my_str:
      if x not in punctuations:
            pfree=pfree+x
print(pfree)            
