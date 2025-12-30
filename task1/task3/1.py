import json
import csv
import typer
from concurrent.futures import ThreadPoolExecutor,as_completed
from rich.progress import Progress
import os
import glob
from collections import defaultdict

app=typer.Typer()

def load_json(file):
    with open(file,'r') as jr:
        return json.load(jr)
    
def load_csv(file):
    with open(file,'r') as cr:
        return list(csv.DictReader(cr,skipinitialspace=True))
def dump_json(file,d):
    with open(file,'w') as d_csv:
        json.dump(d,d_csv,indent=4)

    

@app.command()
def main(input_dir,input_csv,out_csv):
    files=glob.glob(f"{input_dir}/**/.json",recursive=True)
    cs1=load_csv(input_csv)
    # for i in cs:
    #     print(cs)
    cs=defaultdict(dict)
    for i in cs1:
        cs[i['FilePath']][i['SegmentId']]=i['Updated_Start_Time']
        # print(cs)
    for filepath,segment in cs.items():
        read_json=load_json(filepath)
        # for i in read_json:
        #     print(i)
        for i in read_json['value']['segments']:
            # print(i['segmentId']) 
            if i['segmentId'] in segment:
                i['start']=segment[i['segmentId']]
                i['start']=float(i['start'])
        os.makedirs(out_csv,exist_ok=True)
        file=os.path.join(out_csv,os.path.basename(filepath))

        # dump_json()
        dump_json(file,read_json)

    

            
    # for i in files:
    #     data=load_json(i)




if __name__=="__main__":
    app()

