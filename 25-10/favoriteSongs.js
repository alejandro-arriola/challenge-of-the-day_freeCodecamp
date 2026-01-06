function favoriteSongs(playlist) {
  playlist.sort((a, b) => b.plays - a.plays)
  return [ playlist[0].title, playlist[1].title ];
}

console.log(favoriteSongs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))