
json.(@guess, :id)

json.guess_info do
  json.guess @guess.guess
  json.won @winner
  json.number_of_guesses @guesses
  json.points @guess.points
  json.created_at @guess.created_at
end

json.guesser do
  json.(@guess.post.user, :user_name, :first_name, :last_name, :email)
end

json.post do
  json.(@guess.post, :image_url)
end
