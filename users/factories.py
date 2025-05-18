from users.models import StudentProfile, ProfessorProfile, AdminProfile

class ProfileFactory:
    @staticmethod
    def create_profile(user, role):
        if role == "student":
            return StudentProfile.objects.create(user=user, major="Undecided")
        elif role == "professor":
            return ProfessorProfile.objects.create(user=user, department="Unknown")
        elif role == "admin":
            return AdminProfile.objects.create(user=user, permissions="full")
        else:
            raise ValueError("Invalid role")