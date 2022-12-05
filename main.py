import pandas as pd
from yattag import Doc
from template import start, header, banner, filter, main, footer, scripts
from sheet_detail import sheet_detail
import numpy as np

doc, tag, text = Doc().tagtext()

def generate_index():
    spreadsheet_id = "13AU6tbAudnYdcr1Avl0DTbXAaOEW1pSpP1nK8x7Ov2M"
    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&gid=0"
    df = pd.read_csv(url, index_col=False)
    # Drop columns and rows with NaN values
    df.dropna(axis= 1,how='all', inplace=True)# remove columns with all NaN values
    df.dropna(axis= 0,how='all', inplace=True)# remove rows with all NaN values
    df.replace(np.nan, "-", inplace=True)
    # Reset column names
    df2 = df.set_axis(['A', 'B'], axis=1, inplace=False)
    # Transform to one column
    #df2 = df2['A'].append(df2['B']).reset_index(drop=True)
    df2 = pd.concat([df2['A'], df2['B']]).reset_index(drop=True)
    #Save HTML
    with open(f"index.html", "w",encoding="utf-8") as f:
        f.write(start)
        f.write(header)
        f.write(banner("WELCOME TO THE COMMUNITY SERVICES DATABASE !".title()))
        #f.write(filter)
        f.write(pd.DataFrame.to_html(df2.to_frame(), header=False, index = False, table_id= "myTable"))
        # put table here from df
        #f.write(main)
        # add the generated content
        #f.write(doc.getvalue())
        #f.write(footer)
        f.write(scripts)

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
            #Save HTML
            with open(f"{sheet_name}.html", "w",encoding="utf-8") as f:
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
generate_index()
generate_html()