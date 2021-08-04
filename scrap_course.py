from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

# go to next page link
# https://www.coursera.org/search?query=artificial%20intelligence&page=2&index=prod_all_products_term_optimization
def coursera():
	url = 'https://www.coursera.org/courses?query=artificial%20intelligence'
	res = requests.get(url,headers=headers)
	soup = BeautifulSoup(res.text,'html.parser')
	course_list = soup.find('div',class_='ais-InfiniteHits').find('ul',class_='ais-InfiniteHits-list').find_all('li',class_='ais-InfiniteHits-item')
	for course in course_list:
		image = course.find('a',class_='image-wrapper').img['src']
		title = course.find('a',class_='color-primary-text card-title headline-1-text').get_text()
		partner = course.find('span',class_='partner-name').get_text()
		product_type = course.find('div',class_='product-type-row').div.get_text()
		product_info = course.find('div',class_='rc-ProductInfo')
		rating = product_info.find('span',class_='ratings-text').get_text()
		review = product_info.find('span',class_='ratings-count').span.get_text()
		enrollment = product_info.find('span',class_='enrollment-number').get_text()
		level = product_info.find('span',class_='difficulty').get_text()
		print("-----",image,title,partner,rating,review,enrollment,level)



def udacity():
	url = 'https://www.udacity.com/school-of-ai'
	res = requests.get(url,headers=headers)
	soup = BeautifulSoup(res.text,'html.parser')
	course_list = soup.find('ul',attrs={'data-testid':'upcoming-programs-list'})
	for course in course_list.find('li'):
		course_detail_link = 'https://www.udacity.com/'+course.find('a')['href']
		c_date = course.find('time').get_text()
		title = course.find('h3').get_text()
		desc = course.find('p',class_='upcoming-programs-list_conceptsCovered__3LZ01').get_text()
		print("---",course_detail_link,c_date,title,desc)





if __name__ == '__main__':
	# coursera()
	# udacity()