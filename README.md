# Asteroids Game

Welcome to my Python implementation of the classic Asteroids game!

## Description

This project is a recreation of the iconic Asteroids arcade game using Python and Pygame. Players control a spaceship, navigating through an asteroid field while shooting to destroy the space rocks and avoiding collisions.

## Features

- Player-controlled spaceship with realistic momentum-based movement
- Dynamically generated asteroid field
- Shooting mechanics with projectile management
- Collision detection between the ship, asteroids, and bullets
- Simple yet effective graphics using Pygame
- Score tracking system

## Installation

1. Ensure you have Python installed on your system.
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/deedee-ke/build_asteroids_game.git
   ```
4. Navigate to the project directory:
   ```bash
   cd build_asteroids_game
   ```

## How to Play

Run the game:
```bash
python main.py
```

### Controls:

- Use the WASD keys to control the ship:
  - **W**: Thrust forward
  - **A**: Rotate left
  - **S**: Reverse thrust
  - **D**: Rotate right
- Press the spacebar to shoot
- Avoid colliding with asteroids
- Destroy asteroids to increase your score
- Clear all asteroids to advance to the next level

## Game Mechanics

- The ship's movement simulates space physics with momentum and inertia.
- Asteroids split into smaller pieces when shot.
- The game becomes progressively more challenging with each level.

## Future Improvements

- Implement multiple lives for the player.
- Add power-ups (shields, rapid-fire, etc.).
- Create a high-score leaderboard.
- Enhance graphics with particle effects for explosions.
- Add sound effects and background music.

## Contributing

Feel free to fork this project and submit pull requests with improvements! If you have ideas for new features or find any bugs, please open an issue.

## Acknowledgements

This project was created as part of the Boot.dev course.
