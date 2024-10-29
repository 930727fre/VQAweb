# VQAweb
The multimodal answering system based on RAG.

## The imagined file structure tree
```CSS
/project-root
│
├── api/
│   └── Dockerfile
│   └── main.py
│   └── ...
│   └── requirements.txt    # can use "pip freeze > requirements.txt" to generate
├── frontend/
│   └── Dockerfile
│   └── src/
│   └── ...
│   └── package.json
│   └── package-lock.json   # will auto generate after "npm install"
├── backend/       
│   └── ...                 # Dockerfile(s) in ? folder
│   └── ...                 # main.py in ?? folder
│   └── ... 
│   └── ...                 # requirements.txt(s) in ??? folder
└── docker-compose.yml
```
