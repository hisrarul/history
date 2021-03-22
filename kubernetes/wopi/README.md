## WOPI

#### Admin page
```
http://localhost:9980/loleaflet/dist/admin/admin.html
```

#### Convert document using WOPI
```
echo "This is test document" > test.txt
curl -F "data=@test.txt" http://localhost:9980/lool/convert-to/docx > out.docx
```
