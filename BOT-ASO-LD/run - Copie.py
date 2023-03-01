

link_url = 'https://app.apptweak.com/applications/android/com.camerasideas.instashot/metadata?scope=country&country=mx&language=sp&device=android'
print(link_url)

dotindex = link_url.find("metadata")
link_url1 = link_url[:dotindex]+"keywords"+link_url[dotindex+8:]
print(link_url1)
