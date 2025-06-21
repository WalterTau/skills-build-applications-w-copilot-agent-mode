# Test data for octofit_db
# This file contains sample data for users, teams, activities, leaderboard, and workouts collections.

TEST_DATA = {
    "users": [
        {"email": "alice@octofit.com", "name": "Alice", "team": "Tigers"},
        {"email": "bob@octofit.com", "name": "Bob", "team": "Tigers"},
        {"email": "carol@octofit.com", "name": "Carol", "team": "Lions"},
        {"email": "dave@octofit.com", "name": "Dave", "team": "Lions"}
    ],
    "teams": [
        {"name": "Tigers", "members": ["alice@octofit.com", "bob@octofit.com"]},
        {"name": "Lions", "members": ["carol@octofit.com", "dave@octofit.com"]}
    ],
    "activity": [
        {"activity_id": 1, "user": "alice@octofit.com", "type": "run", "distance": 5, "date": "2025-06-20"},
        {"activity_id": 2, "user": "bob@octofit.com", "type": "walk", "distance": 3, "date": "2025-06-20"},
        {"activity_id": 3, "user": "carol@octofit.com", "type": "cycle", "distance": 10, "date": "2025-06-20"},
        {"activity_id": 4, "user": "dave@octofit.com", "type": "run", "distance": 7, "date": "2025-06-20"}
    ],
    "leaderboard": [
        {"leaderboard_id": 1, "team": "Tigers", "points": 8},
        {"leaderboard_id": 2, "team": "Lions", "points": 17}
    ],
    "workouts": [
        {"workout_id": 1, "name": "Morning Run", "duration": 30, "type": "run"},
        {"workout_id": 2, "name": "Evening Walk", "duration": 45, "type": "walk"},
        {"workout_id": 3, "name": "Cycle Sprint", "duration": 60, "type": "cycle"}
    ]
}
