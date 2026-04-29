# TSIS 4


```text
snake/
├── config_loader.py
├── config.py
├── db.py
├── game.py
├── main.py
├── screens.py
├── settings.json
```

## TASK 1. Leaderboard (PostgreSQL + psycopg2)

Main logic - `dp.py`

## TASK 2. Poison Food

Food generetic function - `game.py`

## TASK 3. Power-ups

Power app logics - `game.py`

## TASK 4. Obstacles

Obstacles are created while `len(obstacles) < level * 3`

## TASK 5. Settings (JSON file)

Setted in `settings.json`

## TASK 6. Game Screens

- Main Menu — buttons: Play, Leaderboard, Settings, Quit.
- Game Over screen — shows final score, level reached, personal best; buttons: Retry, Main Menu.
- Leaderboard screen — table with rank, username, score, level, date; button: Back.
- Settings screen — toggle grid, toggle sound, pick snake color; button: Save & Back.



