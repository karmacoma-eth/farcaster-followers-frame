# farcaster-followers-frame

Describe your project here.


## GRPC API

```sh
# separately check out hub-monorepo
git clone https://github.com/farcasterxyz/hub-monorepo path/to/hub-monorepo

# copy the updated protobufs in our repo
cp -R path/to/hub-monorepo/protobufs farcaster-followers-frame/protobufs

# generate the client code
python -m grpc_tools.protoc -I./protobufs/schemas/ \
  --python_out=./src/fff/grpc --grpc_python_out=./src/fff/grpc protobufs/schemas/rpc.proto
```
