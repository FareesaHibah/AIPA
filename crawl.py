# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# def url_list(url):
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text,"html.parser")

#         links = []
#         for tag in soup.find_all('a',href = True):
#             url1 = urljoin(url,tag['href'])
#             links.append(url1)
#         return links
    
# def xyz(links,filename):
#     with open(filename,'w') as file:
#         for link in links:
#             file.write(link + '\n')
#             print(f"Links saved : {filename}") 

# if __name__ == "__main__":
#     url = "https://www.cricbuzz.com/"
#     links = url_list(url)
#     if links:
#         xyz(links,"Fareesa.txt")
#         print(f"Links : {links}")
#         for link in links:
#             print(link)



import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def xyz(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")
    print(f"HTML CONTENT:{soup.prettify()}")
          
    images = []
    for image in soup.find_all("img",src = True):
        img1 = urljoin(url,image["src"])
        images.append(img1)

    print(f'Images are : {images}')
    for image in images:
        print(image)
    return images

def abc(images,directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for x,image1 in enumerate(images):
        img1 = requests.get(image1).content
        name = f"image{x+1}.jpeg"
        path = os.path.join(directory,name)

        with open(path,'wb') as file1:
            file1.write(img1)
        print(f"Images : {path}")
        
if __name__ == "__main__":
    url = "https://www.amazon.in/"
    images = xyz(url)
    if images:
        abc(images,"Website images")
