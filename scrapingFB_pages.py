from selenium import webdriver as wd
import time
from xvfbwrapper import Xvfb


url_gecko = "/home/salegosse/Esiea/5A/OSINT/geckodriver"
#url_page =  "https://www.facebook.com/pg/chantal.brunel"#/about/?ref=page_internal"
#url_posts = "https://www.facebook.com/pg/chantal.brunel/posts/?ref=page_internal"



# facebook page about (uncomment this line or empty variable)
#url_about = ""
#url_about = "https://www.facebook.com/pg/chantal.brunel/about/?ref=page_internal"
def getInfos(mainpage,about,posts,url_g=url_gecko):
	#display = Xvfb()
	#display.start()
	driver = wd.Firefox(executable_path=url_g)

	driver.get(mainpage)

	# get profil image
	url_img = driver.find_element_by_css_selector('img._6tb5')
	url_img = url_img.get_attribute('src')

	# get username
	full_name = driver.find_element_by_xpath('//h1[@id="seo_h1_tag"]')
	full_name = full_name.text

	# get followers
	followers = driver.find_element_by_class_name('_52id')
	followers = followers.text

	file = open(full_name.translate({ord(' '): None})+".txt", "w")

	# To write in file 
	file.write("####### Main Page ########" + "\n")
	file.write("username : " + full_name +"\n")
	file.write("followers : " + followers + "\n")
	file.write("url_image : " + url_img + "\n")
	file.write("Related : " + "\n")

	# Related pages
	related_pages = driver.find_elements_by_class_name("_4-lu")
	related_len = len(related_pages)
	for i in range(related_len):
		if ( related_pages[i].text != "" ):
			file.write(related_pages[i].text +"\n")
	file.write("\n" + "\n")	
	###### About Pages
	file.write("########### About ######### " + "\n")
	driver.get(about)
	infos = driver.find_elements_by_class_name("_4bl9")
		
	abouts = driver.find_elements_by_class_name("_3-8w")
	#file.write("Informations : " + mail + "\n")
	for i in range(len(infos)):
		if ( infos[i].text != "" ):
 			file.write(infos[i].text + "\n")

	#for i in range(len(abouts)):	
	#	if( abouts[i].text != "" ):
	#		file.write(abouts[i].text + "\n")


	file.write("\n" + "\n"  )	

	file.write("Publications : " )
	# Wait for 2 seconds
	driver.get(posts)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(3)
	#click = driver.execute_script("javascript:function('e')")
	#click = driver.find_elements_by_class_name("see_more_link_inner")

	#get publications 
	publications = driver.find_elements_by_class_name("_3576")
	jaimes = driver.find_elements_by_class_name("_81hb") 
	times = driver.find_elements_by_class_name("timestampContent")
	for i in range(len(publications)):
		#more = driver.find_elements_by_class_name("_3-8w")
		if (publications[i].text != ""):
			#infos = infos.text
			file.write("\n" + "date : " + times[i].text + "\n" + "j'aime : " + jaimes[i].text + "\n")
			file.write("contenue : " + publications[i].text.translate({ord('\n'): None}) + "\n")
	file.close()
	driver.close()
	#display.stop()
					


with open("linksFB_pages.txt") as f:
	i = 1
	for line in f:
		if (i == 1):
			link1 = line
			i += 1
		elif (i == 2):
			link2 = line
			i += 1
		elif (i == 3):
			link3 = line
			i = 1 
			getInfos(link1,link2,link3)

		



