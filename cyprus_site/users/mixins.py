class ProfileMixin:
    def get_object(self, queryset=None):
        return self.request.user
