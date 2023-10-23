-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres, COUNT(tv_show_genres.show_id) as number
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
