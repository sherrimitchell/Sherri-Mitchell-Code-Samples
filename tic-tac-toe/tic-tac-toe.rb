## Tic Tac Toe
## The game lets 2 players play tic tac toe from the console
## You win by getting 3 of the same letters in a row horizontally, vertically, or diagonally
## A draw happens if the board gets filled without either player getting 3 of the same letters in a row
## A player chooses which letter they will play with, and they only enter that letter during their turn
## Each player gets one turn to enter a letter into a space.
## A space only holds one letter, and after a letter is entered it can't be deleted from that space
## The next player's turn starts after the previous player has entered their letter into a space.
## The game ends when one player wins or there is a draw

# require 'pry'

# Remove/comment require.pry/ binding.pry before sending file to Github

# binding.pry

# board = ["b1", "b2", "b3","b4", "b5", "b6", "b7", "b8", "b9"]

  def display_board(board)
    puts " #{board[0]} | #{board[1]} | #{board[2]} "
    puts "---+----+----"
    puts " #{board[3]} | #{board[4]} | #{board[5]} "
    puts "---+----+----"
    puts " #{board[6]} | #{board[7]} | #{board[8]} "
  end
  


  # display_board board
  # Test for print_board function: display_board board

# A player may select one Player option: x = Player 1, o = Player 2, or Play against the computer.

def player_move(board)
  display_board(board)
  puts "Where would you like to move? Please enter the number of the square:"
  square = gets.chomp
  available = board.select { |x| x.is_a? Fixnum }
  until square =~ /^#{available}$/
    puts "Sorry. Not a valid square. Please enter a numbered square."
    square = gets.chomp
  end
  square.to_i - 1
end

# A player needs to have 3 spaces filled in a row
# Check to see if 3 spaces on the board have the same letter

WINS = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]

def win_game?(board)
  WINS.any? do |a, b, c|
    board[a] == board[b] &&  board[b] == board[c]
  end
end
  
def draw_game?(board)
  board.all? { |x| x.is_a? String }
end

def game_over?(board)
  win_game?(board) || draw_game?(board)
end

def get_entry
  puts "Please enter an X or O."
  entry = gets.chomp
  until entry =~ /^[xo]$/i
    puts "Sorry. Invalid entry. You must enter an X or an O. "
  entry = gets.chomp
end
entry.upcase
end

# binding pry

def tic_tac_toe
  board = (1 .. 9).to_a
  current_player = get_entry
  until game_over?(board)
    puts "Next player. Make a move. '#{current_player}'!"
    move = player_move(board)
    board[move] = current_player
    current_player = current_player == 'X' ? 'O' : 'X'
  end
  puts "Game Over!"
end

tic_tac_toe
