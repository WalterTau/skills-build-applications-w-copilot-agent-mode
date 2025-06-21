from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@octofit.com', name='Test', team='Tigers')
        self.assertEqual(user.email, 'test@octofit.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Tigers', members=['test@octofit.com'])
        self.assertEqual(team.name, 'Tigers')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(activity_id=1, user='test@octofit.com', type='run', distance=5, date='2025-06-21')
        self.assertEqual(activity.type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(leaderboard_id=1, team='Tigers', points=10)
        self.assertEqual(leaderboard.team, 'Tigers')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(workout_id=1, name='Morning Run', duration=30, type='run')
        self.assertEqual(workout.name, 'Morning Run')
