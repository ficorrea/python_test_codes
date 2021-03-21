#!/usr/bin/python3

import cgi
import cgitb
import rele


cgitb.enable()
form = cgi.FieldStorage()


# Verificar dados dos botões
if form.getvalue('onrele1'):
    rele.ligar1()
        	
elif form.getvalue('offrele1'):
    rele.desligar1()
    
if form.getvalue('onrele2'):
    rele.ligar2()
    
elif form.getvalue('offrele2'):
    rele.desligar2()   

if form.getvalue('onrele3'):
    rele.ligar3()
    
elif form.getvalue('offrele3'):
    rele.desligar3()   

if form.getvalue('onrele4'):
    rele.ligar4()
    
elif form.getvalue('offrele4'):
    rele.desligar4()
    


print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<title>Acionamento Reles via Web</title>")
print("<center><h1>Controle de reles</h1></center><br><br>")
print("<style> h1{color:blue; size:px;}</style>")
print("</head>")
print("<body>")
print("<center>")
print('<div id="rele1">')
print('<legend>Rele 1 </legend>')
print('<form action="/cgi-bin/hello.py" method="get"><input type="radio" name="onrele1" value="on"/>Liga&nbsp<input type="radio" name="offrele1" value="on"/>Desliga&nbsp&nbsp<input type="submit" value="Selecionar"/></form>')
print("</div>")
print("<br>")
print("</center>")
print("<center>")
print('<div id="rele2">')
print('<legend>Rele 2 </legend>')
print('<form action="/cgi-bin/hello.py" method="get"><input type="radio" name="onrele2" value="on"/>Liga&nbsp<input type="radio" name="offrele2" value="on"/>Desliga&nbsp&nbsp<input type="submit" value="Selecionar"/></form>')
print("</div>")
print("</center>")
print("<br>")
print("<center>")
print('<div id="rele3">')
print("<legend>Rele 3 </legend>")
print('<form action="/cgi-bin/hello.py" method="get"><input type="radio" name="onrele3" value="on"/>Liga&nbsp<input type="radio" name="offrele3" value="off"/>Desliga&nbsp&nbsp<input type="submit" value="Selecionar"/></form>')
print("</div>")
print("</center>")
print("<br>")
print("<center>")
print('<div id="rele4">')
print("<legend>Rele 4 </legend>")
print('<form action="/cgi-bin/hello.py" method="get"><input type="radio" name="onrele4" value="on"/>Liga&nbsp<input type="radio" name="offrele4" value="off"/>Desliga&nbsp&nbsp<input type="submit" value="Selecionar"/></form>')
print("</div>")
print("</center>")
print("</body>")
print("</html>")
