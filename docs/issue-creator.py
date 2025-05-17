import sys
import re
import subprocess
import json

'''
Created with the express purpose of creating issues from the microsoft docs
Takes in markdown in the form of a [url](here)\tDescription
Taken from the tables show in the overviews in the ms docs for kusto, e.g.

https://learn.microsoft.com/en-us/kusto/query/scalar-functions

pasting the table into github first will give markdown links, then
putting into a text document here will create commands for creating issues
'''

def create_issue(name:str, desc:str, milestone:int):
    result = subprocess.run(
        ['gh', 'api',
         '--method', 'POST',
         '-H', "Accept: application/vnd.github+json",
         '-H', "X-GitHub-Api-Version: 2022-11-28",
         '/repos/Hashfastr/hash-query-language/issues',
         '-f', f'title={name}',
         '-f', f'body={desc}',
         '-F', f'milestone={milestone}'],
        capture_output=True,
        text=True
    )

    try:
        return json.loads(result.stdout)['id']
    except:
        raise Exception(json.dumps(json.loads(result.stdout), indent=2))

def add_subissue(parent:int, child:int):
    result = subprocess.run(
        ['gh', 'api',
         '--method', 'POST',
         '-H', "Accept: application/vnd.github+json",
         '-H', "X-GitHub-Api-Version: 2022-11-28",
         f'/repos/Hashfastr/hash-query-language/issues/{parent}/sub_issues',
         '-F', f'sub_issue_id={child}'
         ],
        capture_output=True,
        text=True
    )
    
    try:
        return json.loads(result.stdout)['id']
    except:
        raise Exception(json.dumps(json.loads(result.stdout), indent=2))

parent_id = int(sys.argv[2])
issue_suffix = sys.argv[3]
milestone_id = int(sys.argv[4])

with open(sys.argv[1]) as f:
    for i in f.readlines():
        link = i.split('\t')[0]
        desc = i.split('\t')[1]
        
        match = re.match(f'\[([^\]]+)\]\(([^\)]+)\)', link)
        name = match.group(1)
        url = match.group(2)
        
        issue_id = create_issue(
            f'{name} {issue_suffix}',
            f'{url}\n\n{desc}',
            milestone_id
        )
        
        subissue_id = add_subissue(parent_id, issue_id)