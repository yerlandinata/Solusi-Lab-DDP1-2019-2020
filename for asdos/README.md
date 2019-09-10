# How to unzip all submission
- Download all submission from scele (zipped)
- Install git bash or use linux
- Execute this in bash:
```
find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;
```
