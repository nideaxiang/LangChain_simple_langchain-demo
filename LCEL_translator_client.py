# client.py
from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/chain")

result = remote_chain.invoke({"language": "Italian","text": "hi"})

print(result)
