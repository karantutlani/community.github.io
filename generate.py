from yattag import Doc
from template import start, header, banner, main, footer, scripts

doc, tag, text = Doc().tagtext()

with tag('h1'):
    text('Hello world!')

print(doc.getvalue())

with open('index.html', 'w') as f:
    f.write(start)
    f.write(header)
    f.write(banner)
    f.write(main)
    #add the generated content
    f.write(doc.getvalue())
    f.write(footer)
    f.write(scripts)

print("Done")