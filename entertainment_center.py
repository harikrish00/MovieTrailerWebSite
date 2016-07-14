from media import Movie
import fresh_tomatoes

ff7 = Movie("Fast and Furious 7"," It is the seventh installment in the Fast and the Furious franchise.","https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg","https://www.youtube.com/watch?v=TEiPbJNS8Mc")

toy_story = Movie("Toy Story","A Story about a boy and his toys come alive","http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450","https://www.youtube.com/watch?v=KYz2wyBy3kc")

baahubali = Movie("Baahubali","is a 2015 Indian epic historical fiction film directed by S. S. Rajamouli.","https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg","https://www.youtube.com/watch?v=sOEg_YZQsTI")

ratatouille = Movie("Ratatouille","Movie above rat learning to cook","https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = Movie("Midnight In Paris","While on a trip to Paris with his fiance's family, a nostalgic screenwriter finds himself mysteriously ","https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = Movie("Hunger Games","The Fire Will Burn Forever. The Hunger Games:","https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg","https://www.youtube.com/watch?v=4S9a5V9ODuY")


movies_list = [baahubali, ff7, ratatouille, hunger_games, midnight_in_paris, toy_story]
fresh_tomatoes.open_movies_page(movies_list)
