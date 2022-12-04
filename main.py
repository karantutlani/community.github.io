import pandas as pd
from yattag import Doc
from template import start, header, banner, filter, main, footer, scripts
from sheet_detail import sheet_detail
import numpy as np

doc, tag, text = Doc().tagtext()

def generate_html():
    for sheet_name, sheet_id in sheet_detail.items():
        try:
            spreadsheet_id = "13AU6tbAudnYdcr1Avl0DTbXAaOEW1pSpP1nK8x7Ov2M"
            url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&gid={sheet_id}"
            df = pd.read_csv(url)
            # Drop columns and rows with NaN values
            df.dropna(axis= 1,how='all', inplace=True)# remove columns with all NaN values
            df.dropna(axis= 0,how='all', inplace=True)# remove rows with all NaN values
            df.drop([0], axis=0, inplace=True) # Drop row title index:0 
            df.replace(np.nan, "-", inplace=True)
            with open(f"templates/{sheet_name}.html", "w",encoding="utf-8") as f:
                f.write(start)
                f.write(header)
                f.write(banner(sheet_name.title()))
                f.write(filter)
                f.write(pd.DataFrame.to_html(df, header=True, table_id= "myTable"))
                # put table here from df
                #f.write(main)
                # add the generated content
                #f.write(doc.getvalue())
                #f.write(footer)
                f.write(scripts)
        except:
            print("Error with {}".format(sheet_name))
            pass

# Run the function to generate HTML
generate_html()