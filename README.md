# Lab3_FileTransfer
1. Built Image
```bash
docker build -t lab3-watcher . 
```  
2. Với ${PWD} là đường dẫn tuyệt đối đến file Lab3_FileTransfer
```bash
docker run -d --name legacy_worker `
-v "${PWD}\Lab3_FileTransfer\input:/app/input" `
-v "${PWD}\Lab3_FileTransfer\processed:/app/processed" `
-v "${PWD}\Lab3_FileTransfer\error:/app/error" `
lab3-watcher
```
3. Kiểm tra log xem nó có hoạt động hay không
```bash
docker logs -f legacy_worker 
```
