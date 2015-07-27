class movie:
	def __init__(self, title, date, poster, desc, trailer, 
		big_pic, director, runtime, main_cast_member, secondary_cast_member):
		'''
		The movie class encapsulates all the metadata 
		associated with a particular film.  
		All variables are treated as strings by the codebase.
		EXAMPLE:
		
		the_philadelphia_story = movie(
    		"The Philadelphia Story",
    		"July 18",
    		"http://bit.ly/1S3MYPB",
    		"This 1940 Kathrine Hepburn, romantic comedy focuses on a young \
    		soccalite and her relationship between her ex-husband, 
    		fiance and a reporter. Unclear about her feelings for all \
    		three men, Tracy must decide whom she truly loves.",
			"https://www.youtube.com/embed/oCfuPPR7wnQ",
    		"",
    		"George Cukor",
    		"112",
    		"Kathrine Hepburn",
    		"Cary Grant")


		'''
		self.title = title
		self.date = date
		self.poster = poster
		self.desc = desc
		self.trailer = trailer
		self.big_pic = big_pic
		self.director = director
		self.runtime = runtime
		self.main_cast_member = main_cast_member
		self.secondary_cast_member = secondary_cast_member

