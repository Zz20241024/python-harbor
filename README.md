# Installation
pip install pyharbor

# Usage
from pyharborclient.harborclient import HarborClient


host = "xx"  
user = "xx"  
password = "xx"  
client = HarborClient(host, user, password,protocol="https")  
client.get_repository_tags("ww/ww")  
client.get_projects()  


# examples for more



