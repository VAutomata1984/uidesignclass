from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

""" 
UI HW 6 - Search Application Functionality - Example II 
Author: Matthew Vollo
Started: 06/26/2026
Finished: 06/28/2026

Note: To better practice the concepts utilized in this homework and in lieu of a two-minute YouTube video, 
I decided to do another example, this time based on places in NYC to do remote work. 
"""

cafes = { 
    "1": {
        "id": 1,
        "title": "Georgie's Cafe & Bar",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNBL0LLwCUGE5wgf0ePYKWdrvcRfdnjlbaKa32vFyeJ8rxHXjzW-_OCTI&s=10",
        "summary": "A brutalist asian-style cafe on the top floor of VITAL climbing gym.",
        "location":"Lower East Side, Manhattan",
        "rating":"4.5/5",
        "review": "An excellent place for remote work. The cafe is filled with remote workers, students, and people who just want a nice coffee and pastry after a fun bouldering session. Opens early and closes late. If you are seated at the big table, there is an outlet strip attatched to the back of the table, yet not all chargers can stay in without falling.",
        "similar":["2","3"]
    },
    "2":{
        "id": 2,
        "title": "Remi43 Flower's Coffee",
        "image": "https://passblue.com/wp-content/uploads/2021/10/Remi43-from-the-mezzanine-scaled.jpg",
        "summary": "Part-flower shop and part coffee shop, this small yet sprawling cafe offers a lush retreat near the heart of Midtown.",
        "location":"Midtown, Manhattan",
        "rating":"4/5",
        "review": "Excellent beverages and a wonderful ambiance. Yet, at times it can be hard to find a seat. Can get crowded during a lunch rush.",
        "similar":["1","3"]
    },
    "3":{
        "id": 3,
        "title": "Kona Coffee Roasters | Midtown",
        "image": "https://s3-media0.fl.yelpcdn.com/bphoto/bJazlW3e-BwXogLmqzk1rQ/348s.jpg",
        "summary": "Right off from Grand Central, treat yourself to a supurb Hawaiian Coffee!",
        "location":"Midtown, Manhattan",
        "rating":"4/5",
        "review": "The coffee itself is amoung the best in the city, and there is plenty of space to work. Arond lunch time the store can get a little crowded, which means long lines and trouble finding seating.",
        "similar":["2","1"]
    },
    "4":{
        "id": 4,
        "title": "Cafe W & Bakery / Dessert",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAqD0VNwXDbGaorxyXVlUGTWBQfP7v2dhTi6bjo7tWripWkK6TeBIWspo&s=10",
        "summary": "A trendy, relaxed cafe that sells delicous coffee and asian pastries.",
        "location":"Flushing, Queens",
        "rating":"4.5/5",
        "review": "The Misugaru latte is a standout drink. Plenty of space and tables to work and excellent sweet treats. Open late, which is a huge plus. However, unless you have a car, it is hard to get here. Addtionally, they have barely any parking spots. A great evening work, study or hang-out spot.",
        "similar":["1"]
    },
    "5":{
        "id": 5,
        "title": "Cafe Auburndale",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/APNQkAGnCfqGRxIsYw1W4sUhew4xlWSShh9w1RGvFl9Gz56utNsXjm6_qdAa1FHDCaN8mnix6xp3RbRU93H8GEhYpK1ldp4ZPK4UV51GP7e6_LcSXUDR9WbgSsTCUsq-Bvf_NTKzTS5i=s1360-w1360-h1020",
        "summary": "A modern, trendy cafe with outdoor seating and excellent drinks.",
        "location":"Flushing, Queens",
        "rating":"4/5",
        "review": "The drinks and beverages are excellent, and usually you can find a spot to work in. A bit harder to get to in terms of transportation, and may be crowded. Open late which is a plus.",
        "similar":["4"]
    },
    "6":{
        "id": 6,
        "title": "Fasan",
        "image": "https://pub-ba1a74be17d7442a9f2541946eb9510e.r2.dev/shops/5f3cebed-f009-418c-82ff-1208a24d49d3/0.jpg",
        "summary": "A small quaint Chinese coffee shop tucked away on Allen st.",
        "location":"Chinatown, Manhattan",
        "rating":"3.5/5",
        "review": "Drinks here are a 5/5, but it is a very small cafe, more suited for a grab and go situation. If you could grab a drink here and then go to a library, that would be ideal. Offers outside seating. Less of a work-from-home place more than a place to just relax.",
        "similar":["1","4"]
    },
    "7":{
        "id": 7,
        "title": "The Library Cafe by Amy's Bread @ Stavros NYPL",
        "image": "https://offloadmedia.feverup.com/secretnyc.co/wp-content/uploads/2025/04/17120622/NYPL-rooftop-terrace-1024x683.jpg",
         "summary": "Note, this place has closed. It was a small spot located on the top floor of the Stavros Niarchos Foundation Library where you could buy a coffee or some bread and enjoy it on the Terrace.",
        "location":"Midtown, Manhattan",
        "rating":"4/5",
        "review": "The outdoor seating, when available, was supurb for eithe enjoyment or study. A nice retreat from studies located inside a library. You can still come and work on the terrace, yet now there will be no cafe to greet you. Seating is first-come, first-served. You can still sit on the terrace for free",
        "similar":["1"]
    },
    "8":{
        "id": 8,
        "title": "Blue Java Cafe (Butler) | Columbia University",
        "image": "https://dining.columbia.edu/sites/dining.columbia.edu/files/styles/cu_crop/public/content/Retail%20Location%20Photos/Butlerhero.jpg.webp?itok=G-sin-tT",
        "summary": "One of the most in-demand study spots on Columbia's campus. A great place to study or cram with friends.",
        "location":"Morningside Heights, Manhattan",
        "rating":"3/5",
        "review": "The beverages are standard, yet the pastries are quite good. It is easy to find seating sometimes, and on other times it is almost impossible. You can only enter if you either are a CU student, an Alumni, or a guest. If you are able to get in, an amazing late-night study location, though the cafe will be closed by then.",
        "similar":["7"]
    },
    "9":{
        "id": 9,
        "title": "Joe's Coffee | Columbia University - SIPA",
        "image": "https://www.sipa.columbia.edu/sites/default/files/2025-03/JoesCoffee.jpg",
        "summary": "An underrated coffee shop near the back of Columbia's campus. Ample seating, and even after it has closed, if you are a student you can come here to work.",
        "location":"Morningside Heights, Manhattan",
        "rating":"3.5/5",
        "review": "A bit out of the way, and only accessable to CU students, it serves as an underrated study spot. You are usually able to get seating, but sometimes it is almost impossible.",
        "similar":["7","8", "10"]
    },
    "10":{
        "id": 10,
        "title": "Joe's Coffee | Columbia University - Journalism School",
        "image": "https://bwog.com/wp-content/uploads/2018/10/IMG_7559.jpg",
        "summary": "Sleek, studious and intimate coffee shop located next to Columbia Journalism School. ",
        "location":"Morningside Heights, Manhattan",
        "rating":"3.5/5",
        "review": "More accessable than the other Joe's Coffee on campus (especially for guests), what it lacks up in seating it makes up in atmosphere and quality.",
        "similar":["7","8","9"]
    }
}

# ROUTES
@app.route('/', methods=['GET', 'POST'])
def cafe_world():
   return render_template('homepage.html',cafes=cafes)   

@app.route('/search', methods=['GET', 'POST'])
def search():
   search_text = request.form.get("search_text", '').strip()
   if not search_text:
      return render_template('homepage.html', cafes=cafes)
   
   results = [cafe for cafe in cafes.values() if search_text in cafe['title']]

   return render_template('search_results.html', cafes=cafes, results=results, search_text=search_text)
   
   
@app.route("/view/<id>", methods=['GET'])
def view(id):
   cafe = cafes.get(id)
   return render_template('view.html', cafes=cafes, id=id)

if __name__ == '__main__':
   app.run(debug = True)