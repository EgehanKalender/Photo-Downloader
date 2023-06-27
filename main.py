import requests # to get image from the web
import shutil # to save it locally
import json


jsondata = open('links.json', encoding="utf8")
jsonconvert = json.load(jsondata) 

for i in jsonconvert: 
    image_url = i['imageLink']
    filename = i['fileName'] #isteğe bağlı bir isimlendirme olabilir.


    r = requests.get(image_url, stream = True)


    if r.status_code == 200:
        
        r.raw.decode_content = True
        
        
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Fotoğraf başarılı bir şekilde indirildi.',filename)
    else:
        print('Fotoğraf indirilemedi')