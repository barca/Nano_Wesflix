from entertainment_center import Movies
from detail_page import write_detailed_pages
from calendar_page import write_calendar
from WesFlix import write_and_open_homepage
#Above imports necessary functions to generate the all files for the website


#generates the calendar page, and links to the detailed pages, and main page
write_calendar(Movies)
#generates all the detailed pages for the movies
write_detailed_pages(Movies)
#generates the homepage
write_and_open_homepage(Movies)
