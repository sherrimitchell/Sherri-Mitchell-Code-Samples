class Guess < ActiveRecord::Base
	validates :post_id, presence: true
	validates :guess, presence: true

	belongs_to :user
	belongs_to :post

	
	def check_solution
		if self.post.answer == self.guess
			self.points = 30
			self.post.update(solution: self.id)
			true
		else
			false
		end
	end
end
