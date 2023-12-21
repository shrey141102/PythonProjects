# Mad Libs Story Generator

This Python script generates amusing and random stories using the Mad Libs format. Mad Libs are a fun way to create stories by filling in the blanks with random words. In this script, we have a predefined dictionary of words, categorized by types such as adjectives, city names, nouns, action verbs, and sports nouns.

## How it Works

1. The `word_dict` dictionary contains lists of words for different word types.
2. The `story` template defines a narrative with placeholders for different word types.
3. The `get_word` function selects a random word of a given type from the dictionary and removes it to avoid repetition.
4. The `create_story` function generates a random story by filling in the placeholders with words from the dictionary.


## Example Output

```
Story 1:
One day my tasty friend and I decided to go to the puck game in Charlotte. We really wanted to see the people play the ball. So, we jump our hotdog down to the scoreboard and bought some mit. We got into the game and it was a lot of fun. We ate some hamster music and drank some music hotdog. We had a great time! We plan to go again next year!

Story 2:
One day my abrasive friend and I decided to go to the uniform game in Indianapolis. We really wanted to see the dog play the puck. So, we bounce our salad down to the player and bought some hotdog. We got into the game and it was a lot of fun. We ate some grubby map and drank some salad ball. We had a great time! We plan to go again next year!
```
