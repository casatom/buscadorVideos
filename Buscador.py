from pyquery import PyQuery as pq
 
jquery = pq(url="http://www.cambio-euro.es/")
print jquery("div[id='valor']").text()