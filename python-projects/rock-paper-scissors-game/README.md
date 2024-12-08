# Rock, Paper, and Scissors Game

## Requirements

**End Goal:**

- Determine the winner between the user and the program.
- Display the outcome: "Won," "Lost," or "Draw."
- Provide an option to restart the game through user input.

**Inputs:**

- User selects one of the following options: **Rock**, **Paper**, or **Scissors**.
- The program randomly selects one of these options as well.

**Business Logic:**

- **Rock** beats **Scissors**.
- **Paper** beats **Rock**.
- **Scissors** beats **Paper**.

- If both selections are the same, the result is a **Draw**.

## Pseudo-code

1. **Print Welcome Message**

    - Display a welcome message to the user.
2. **Explain Game Rules**

    - Inform the user about how the game works, including the possible choices.
3. **Initialize Game Variables**

    - Create variables to track total wins, losses, and draws.
4. **Game Loop**

    - **Start Game Round:**

        1. Prompt the user to input their choice:

            - Accept `rock` (`r`, `1`), `paper` (`p`, `2`), or `scissors` (`s`, `3`).
        2. Validate the user's input. If invalid, ask again.

        3. Let the computer randomly choose one of the three options and store it.

    - **Compare Choices:**

        1. **If User Wins:**
            - `rock` beats `scissors`.
            - `paper` beats `rock`.
            - `scissors` beats `paper`.
        2. **If Draw:**
            - User choice == Computer choice.
        3. **Otherwise:**
            - Computer wins.
    - **Display Round Result:**

        1. Show the user's and computer's choices.
        2. Announce whether the user won, lost, or drew this round.
    - **Update and Display Total Results:**

        - Increment and display the cumulative scores (wins, losses, draws).
5. **Ask to Restart or Exit:**

    - Ask the user if they want to play another round.
    - **If Yes:** Restart the game loop.
    - **If No:** End the game with a goodbye message and display the final results.
