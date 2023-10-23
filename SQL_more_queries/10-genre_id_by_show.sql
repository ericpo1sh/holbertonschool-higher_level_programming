-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.genre_id = tv_shows_genres.show_id
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;
