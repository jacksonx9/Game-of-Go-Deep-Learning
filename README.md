# Go Deep Learning

> Use Deep Learning to train AI to Play the Game of Go



To generate game data for 20 9 × 9 Go games and store features in features.npy, and labels in labels.npy, run:

```bash
python generate_mcts_games.py -n 20 --board-out features.npy --move-out labels.npy
```




The general approach is inspired by the book "Deep Learning And The Game of Go".
