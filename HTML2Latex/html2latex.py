#Maayez Imam 10/5/17
#HTML to Latex program

htmlString = str(input('Please enter a HTML string: '))
# user inputs an HTML string

newString = htmlString.replace('%', '\\%').replace('&ldquo;', '``').replace('&rdquo;', '\"').replace('&apos;', '\'').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('{', '\\{').replace('}', '\\}')
# replaces all the HTML text with Latex text

print(newString)
# prints the new string with the Latex text