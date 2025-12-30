import json
import csv
import pandas as pd
import glob
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor,as_completed
from rich.progress import Progress
import os
import typer
pd.options.display.max_rows=9999
app=typer.Typer()
def read_json(file):
    with open(file,'r') as r:
        return json.load(r)

    
@app.command()
def main(input_folder,input_csv,output_folder):
    files=glob.glob(f"{input_folder}/**/*.json",recursive=True)
    print(len(files))
    row={}
    csw=pd.read_csv(input_csv)
    











if __name__=="__main__":
    app()
