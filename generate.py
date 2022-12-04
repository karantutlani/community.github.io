from yattag import Doc
from template import start, header, banner, main, footer, scripts

doc, tag, text = Doc().tagtext()

with tag('h1'):
    text('Hello world!')

print(doc.getvalue())

with open('index2.html', 'w') as f:
    f.write(start)
    f.write(doc.getvalue())

print("Done")