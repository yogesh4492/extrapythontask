import typer 
import json
import csv
import glob
from rich.progress import Progress
from concurrent.futures import ThreadPoolExecutor,as_completed
import os

app=typer.Typer()

class Main:
    def __init__(self,input,fields,output):
        self.input=input
        self.output=output
        self.fields=fields.split(",")

    def run(self):
        with open(self.input,'w') as c:
            csw=csv.DictWriter(c,fieldnames=self.fields)
            csw.writeheader()

