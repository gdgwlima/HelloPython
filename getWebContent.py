import urllib.request as url
import xml.etree.ElementTree as et

webdata = url.urlopen("http://www.w3schools.com/xml/cd_catalog.xml")
str_data = webdata.read()
print(str_data)


# URLLIB

webData = url.urlopen("https://twitter.com/NathalyAlarconT")
print (webData.read()) #IMPRIME TODO EL HTML DE LA PAGINA

web_content = url.urlretrieve("https://twitter.com/NathalyAlarconT", "tw.html")  #Para descargas
