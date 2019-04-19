# Installation
###latest version 1.2.5
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

# myblog address
https://home.51cto.com/space?uid=12109115
#QQ
752477168



