class UserService:
    def __init__(self, repository):
        self.repository = repository

    def get_user(self, user_id):
        return self.repository.find_by_id(user_id)
