# nomad-verse-
- it's a login in rails with the country, the phone number, and the name
- the person has bookmarks , social bokmarks, to bookmark yourself as a lot of bookmarks,
- - like many countries,
  - vehicle
- as if your bookmarks has all the countries,  many places,  all the things you can bokmark
- as if your bookmarks are so varied
-
-
- database
- user  : phone number, phone country, name,
- social bookmarking : person, place, dish, country
- plane tickets : city, country, user id 
- number of stuff bookmarked, nuber of people bookmarked
- no value in trips, people met,
- social meda posts,
- networkingsystem and tech application
- valid emails, spam alerts
- events, reviews of homes
-     * nomad verse  adventures, in varied countries
  * 
- Meetup
ruby
t.references :user
t.string :location_city
t.string :location_country
t.datetime :met_on
t.text :notes
📸 PhotoMoment
ruby
t.references :user
t.string :title
t.string :location_city
t.string :location_country
t.string :image_url
t.datetime :taken_at
t.text :caption
🍽️ SharedMeal
ruby
t.references :user
t.string :dish_name
t.string :restaurant_name
t.string :location_city
t.string :location_country
t.integer :people_count
t.datetime :date
t.text :conversation_notes
🎨 LocalArtEncounter
ruby
t.references :user
t.string :art_type
t.string :artist_name
t.string :location_city
t.string :location_country
t.datetime :date
t.text :reaction

- in the welcome page you have got a plane ticket
- and the signup has phone number and ountry of phone number
- user can randomly receipt mail in inbox, or sms in phone inbox, or vocal message in phone

- 
