# This is the database file
# https://docs.google.com/spreadsheets/d/13AU6tbAudnYdcr1Avl0DTbXAaOEW1pSpP1nK8x7Ov2M/edit?usp=sharing
import pandas as pd
from yattag import Doc
from template import start, header, banner, main, footer, scripts

sheet_names = [
    "WELCOME!",
    "Sheet37",
    "Abuse",
    "Addictions",
    "AIDS Hepatitis C",
    "Bereavement",
    "Anger Management",
    "Black Lives",
    "Brain InjuryTumour",
    "Clothing Donations",
    "Community Programs",
    "Disability",
    "Education",
    "Emergency Services",
    "Employment Services",
    "Family Services",
    "Food Banks",
    "Financial",
    "Francophones",
    "Government",
    "Healthcare",
    "Homelessness",
    "Housing",
    "Indigenous People",
    "LGBTQ2S+",
    "Legal Assistance",
    "Mental Health",
    "Newcomers",
    "Pregnancy",
    "Older Adults",
    "Transportation",
    "Youth",
]

doc, tag, text = Doc().tagtext()

with tag("h1"):
    text("Hello world!")

print(doc.getvalue())


for sheet in sheet_names:
    try:
        sheet_id = "13AU6tbAudnYdcr1Avl0DTbXAaOEW1pSpP1nK8x7Ov2M"
        sheet_name = sheet
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        data = pd.read_csv(url)
        data.dropna(axis=1)
    except:
        print("Error with {}".format(sheet))
        pass

    # print(data.head())
    try:
        with open(f"{sheet_name}.html", "w") as f:
            f.write(start)
            f.write(header)
            f.write(banner)
            f.write(pd.DataFrame.to_html(data))
            # put table here from df
            f.write(main)
            # add the generated content
            f.write(doc.getvalue())
            f.write(footer)
            f.write(scripts)

            # print(pd.DataFrame.to_html(data))
    except:
        pass


print("Done")
