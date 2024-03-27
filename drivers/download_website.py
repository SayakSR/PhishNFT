import os
def save_webpage(url_id,url):
    os.system(f"wget -p -k {url} >/dev/null 2>&1")
    try:
        url=url[7:]
        os.system(f"cp -r {url} saved_webpages/{url_id}")
        os.system (f"rm -r {url}")
        filename=f"{url_id}"
        return filename
    except Exception as e:
        print(e)


#save_webpage(187291,'https://google.com')