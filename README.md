# Workplace Safari
## Scenario
### We are required to build a dataset for a report of TV shows that students have watched.
- The visual report layout exists already, this shows the following details per show:
    - TV Show Name
    - Watched By (Student Name)
    - Cover/Poster Image
    - Total Show Duration
    - Then a breakdown of TV Show Seasons, Episode Names, Images, First Airdate and Duration
    - Total duration of all reported TV Shows

        <img src="tvmaze/.md_img/tv-show-report-layout.png" height="400">

- A public API data source called **TV Maze** has been identified that can provide the details that the report requires.
- A function has already been written and hosted in the cloud to process show submissions that are posted into a storage queue. It will retrieve the data from the TV Maze public API when it processes queued items containing the name of the student that submitted it and the ID of the show from the TV Maze dataset.

## Project Work Phases - Computational Thinking
1. Ab.........
2. De...........
3. Pat.... Rec........
4. Al........

## Part 1
Write an API Request ***Procedure*** to submit a request including two (string) parameters (**name** and **show_id**) to the Workplace Safari TV Maze Show Submit service. `Estimated 8 lines of code`.

## Part 2
Adjust the API Request **Procedure** into a **Function**, add an additional parameter (defining the element/format of the response) to return. `Estimated additional 6 lines of code (14 lines in total)`.

Add a condition (IF statement) for data validation, to the code section that makes the call to the API Request function.

## Part 3
Replace the static show_id variable with another API Request call that can process a tv show search of the TV Maze API, with a text search term. Then automatically submit the top search result using the existing function call. We're passing the variable `show_id` from the output of this additional function call. `Estimated additional 8 lines of code (22 lines in total)`

# Appendix
## Computational Thinking
The process of thinking about a problem using computational means in order to create a solution which a computer can implement.

### Abstraction
The process of removing irrelevant or unnecessary information from the problem in order to better understand the basic parts of it.

### Decomposition
The process of breaking a problem down into smaller parts to make it easier to solve.

### Pattern Recognition
Pattern recognition uses the identification of similarities within a particular dataset or sequence to simplify understanding and resolution of a problem or goal. It can also increase effectiveness in the problem-solving process by creating solutions that can be repeated to resolve similar problems or goals.

### Algorithms
The process of working out the individual steps needed to solve a problem in order to produce an algorithmic solution.
