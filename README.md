# SpotifyJanusGraph

## Objectives
The goal of this project is to prototype JanusGraph ingest functionality using a CQL backend and Elasticsearch index. The dataset used will be extracted from the Spotify API, normalized, and bulk ingested to CQL using Java (or Python) scripts.

## Tools
- Python
- Cassandra v3.10.11
- Elasticsearch
- JanusGraph v0.5.3
- Docker

## Key Components
- Docker Image with Cassandra, Elasticsearch, and JanusGraph configuration
- Spotipy Utils python program
- Cytoscape for UI

### Architecture Version I - Ephemeral Graphs
The initial architecture for this project will be a single monolithic docker image with Cassandra, Elastic, JanusGraph, and Spotipy utils deployed. This image will generate new Cassandra/Elastic databases every time it is run, and create a new graph with the user's playlist/song data at runtime.

![image](https://user-images.githubusercontent.com/17954995/121594742-79180380-ca0b-11eb-892f-ac7707d0ac0b.png)

### Architecture Version II - Graph with Persistent Backends
Eventually, to build larger graphs and save build time, we may choose to create persistent Cassandra/Elastic clusters (host service tbd). In this case, only JanusGraph and Spotipy will be dockerized, and connect to already existing backend and index stores

![image](https://user-images.githubusercontent.com/17954995/121595598-6d790c80-ca0c-11eb-80d3-e7f005fd7ce6.png)


