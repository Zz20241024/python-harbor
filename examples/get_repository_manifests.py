#!/usr/bin/env python

import sys
sys.path.append("../")

from harborclient import harborclient

host = "127.0.0.1"
user = "admin"
password = "Harbor12345"

client = harborclient.HarborClient(host, user, password)

# Get repository manifests
repo_name = "library/cirros"
tag = "latest"
client.get_repository_manifests(repo_name, tag)
