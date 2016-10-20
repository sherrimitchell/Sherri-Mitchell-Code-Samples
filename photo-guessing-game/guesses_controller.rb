class GuessesController < ApplicationController
  before_action :authenticate_with_token!

  def new
    @guess = Guess.new( user_id: current_user.id,
                            post_id: params[:post_id],
                            guess: params[:guess])
    if self.post_exists && self.not_solved && self.not_same_user_as_post && self.unique_guess
      if @guess.save
        @winner = @guess.check_solution
        @guesses = Post.find_by(id: params[:post_id]).guesses.where(user_id: current_user.id).count
        render 'new.json.jbuilder', status: :created
      else
        render json: { errors: @guess.errors.full_messages },
          status: :unprocessable_entity
      end
    end
  end

  protected
    def not_solved
      post = @guess.post
      if post.solution.nil?
        result = true
      else
        result = false
        render json: { message: "You cannot make a guess! You're too slow" },
          status: :unprocessable_entity
      end
      result
    end

    def not_same_user_as_post
      post_user = @guess.post.user
      if current_user != post_user
        result = true
      else
        result = false
        render json: { message: "You cannot make a guess on your own post. You are a cheater!" },
          status: :unprocessable_entity
      end
      result
    end

    def post_exists
      if Post.find_by(id: params[:post_id])
        result = true
      else
        result = false
        render json: { message: "That post doesn't exist!"},
          status: :unprocessable_entity
      end
      result
    end

    def unique_guess
      if current_user.guesses.find_by(guess: params[:guess])
        result = false
        render json: { message: "You already guessed that!" },
          status: :unprocessable_entity
      else
        result = true
      end
      result
    end

end



