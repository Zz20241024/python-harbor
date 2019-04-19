# Installation
pip install pyharbor

# Usage
from pyharborclient.harborclient import HarborClient


host = "xx"  
user = "xx"  
password = "xx"  
### login
client = HarborClient(host, user, password,protocol="https")  
### receive tags
client.get_repository_tags("ww/ww")  
### receive projects
client.get_projects()  

# examples for more
find examples in examples directions



