import mechanize
import csv
filename = './Credentials.csv'
loanDir = 'C:/Users/Brandon/Documents/loandir/'


url = 'https://www.nslds.ed.gov/npas/index.htm'
accessPage = 'https://www.nslds.ed.gov/nslds/nslds_SA/secure/SaFinLogin.do#login'
downloadPage = '/nslds/nslds_SA/secure/SaFinShowMyDataConfirm.do'
downloadLink = 'https://www.nslds.ed.gov/nslds/nslds_SA/secure/MyData/MyStudentData.do?language=en'



csv_file = open(loanDir + 'Credentials.csv')
csv_reader = csv.reader(csv_file)
for row in csv_reader:
	USERNAME = row[0]
	PASSWORD = row[1]
	
	br = mechanize.Browser()
	br.open(url)


	for link in br.links():
		target_url = accessPage
		if link.url == target_url:
			print "Success!"
			br.follow_link(link)
			print br.geturl()


	br.select_form(name="signIn")

			
	br["signIn:inputUserId"] = USERNAME
	br["signIn:inputPassword"] = PASSWORD

	result = br.submit()

	#logincheck = result.read()

	#print logincheck

	for link in br.links():
		target_url2 = downloadPage

		if link.url == target_url2:
			print "Download Confirm Page"
			br.follow_link(link)
			print br.geturl()


	#for link in br.links():
	 #   target_url3 = '/nslds/nslds_SA/secure/MyData/MyStudentData.do?language=en'

	  #  if link.url == target_url3:
	   #     print "Downloading..."
		#    br.retrieve(link, 'loans.txt')
	print "Downloading..."
	br.retrieve(downloadLink, loanDir + USERNAME + '.txt')
	print "Done!"

		
	
	
csv_file.close()



