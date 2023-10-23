-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name 
FROM tv_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genre.id
INNER JOIN tv_show_genres ON tv_shows_genre.show_id = tv_shows.id
WHERE tv_show.title = "Dexter"
ORDER BY tv_genres.name ASC;
