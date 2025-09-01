# Riddle Me This

A simple Python riddle game that loads riddles from a JSON file and prompts the user to answer them. The game tracks your score and allows you to exit by typing `exit`.

## How to Run

1. Make sure you have Python 3 installed.
2. Place your riddles in a file called `riddles.json` in the same directory. Example format:
    ```json
    [
        {"riddle": "What has keys but can't open locks?", "answer": "piano"},
        {"riddle": "What has a heart but no other organs?", "answer": "artichoke"}
    ]
    ```
3. Run the game:
    ```bash
    python3 riddle-me-this.py
    ```

## Running Unit Tests

Unit tests for the `Riddle` class are provided in `test_riddle.py`. To run the tests:
```bash
python3 -