# Goals
1) Create a simple app
2) Decompose and plan our app
3) code in Scratch
4) Code in python
5) cement our knowledge of common coding concepts

# App Brief
Problem
- Eating is great, but choosing meals every week is a pain
- Remembering all the ingredients for the weekly shop is also a pain - too easy to forget things and making a list is tedious

Solution
- A simple app to pick meals for us, and give us a list of all the ingredients we need for our shopping list.
- Munch!

***

1. Decompose the ideal solution
2. Code a Proof of Concept (PoC) using Scratch
3. Code a Minimum Viable Product (MVP) using Python

***

Decompose
- Choose Dishes
    - Days - USER INPUT
    - Food We Like - LIST for now, but will be updatable by user later

- List Ingredients
    - Map Ingredients for every dish - SUBLISTS
    - List ingredients if dish chosen - Conditionals


output list of chosen dishes and list of ingredients for chosen dish in a "grocery list" format

https://www.udemy.com/course/coding-for-beginners-you-can-learn-to-code/learn/lecture/11565312#content

'Food we like'
'My Menu' 
Ask user how many days to plan for
Call function to choose dishes (pass answer)
Show this week's menu

Choose Dishes Function (for given no. of days)
Choose a random dish from our food we like list
    - Until We have a dish for given no. of days
        -If dish not already chosen
         - Add dish to this week's menu list
    
Show this week's menu
Ask user if they want the shopping list
 - If answer is yes
    call function to generate shopping list
    show shopping list
    send to file for printing
ELSE 
    Say Goodbye


Build Shopping List Function
If dish A is chosen for my menu
 Add dish A's ingredients list to this week's shopping list
If dish B....etc


Number of servings calculator

Build Add Receipt function
take name
take ingredients
maybe provide link for directions too, idk

---

Possible flow, assuming TUI

Main Menu Options
1) Plan Your Week
    - Provide number 1-7, blank defaults to 5
        - Return matching number of unique recipe names from the pool. Figure out how to format it nicely later
        - Provide option to swap out any of the recipes
            - either random or specifying one from the pool later, start random.
        - Confirm choices 
            - iterate through selected recipes, normalize ingredient amounts to purchasable whole quantities for Grocery List output
                - (1/2 cup diced onion = 1 onion, etc)
        - Output ingredients in ready to go Grocery List
            - in parenthesis show the total amount needed for all included recipes
                - [ ] 2 Onions (1 1/2 cups of onion)
        - Save to dated text file? Or offer to?
2) View list of all named recipes
3) Add new recipes
    - need to create a method to view/edit/add recipes but to start, and while in TUI, the only method should be to add new appropriately formatted receipe files. 

With the above thoughts we need to decide how we're going to store the recipes. JSON? Or do we use a db? Maybe start with JSON? What kind of technical debt does that create... If I set things up modularly enough it shouldn't effect much. The first thing that the program is going to do from a flow perspective is going to be to load the recipes from whatever format.Whether that's json or sql lite. I'm personally fuzzy on how the abstraction layer(am I using that right) works here to make it interchangeable and that will require some research so I understand. 

From my current understanding, assuming I plan ahead in the json formatting, converting to a db later for a larger scaled set should be relatively fluid. I will simply have to try it and find out. 

I also should include a timer to show how long it takes to complete the process post selecting number days to showing the randomly chosen recipes. Put in however many recipes to get things functional, then fill in some nonsense recipes to get like 1k+ or something to get ensure it's just as efficient/fast to pull in data. Same for manually choosing recipes, the data access should be quick and not require loop that reads through the recipes one at a time. 

Maybe look into using textual for handling the interface to make it more navigable, but I want the core of this project to focus on getting a usable product FIRST, that's a later deal to build out as more of a finishing touch. 

