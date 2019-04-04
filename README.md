# <p align="center">Maze Adventures: Maze Game using Depth-First Search and Breadth-First Search </p>

## Autors

| Name  | Registration  |
|---|---|
| Daniel Maike Mendes Gonçalves  | 16/0117003  |
| Lucas Pereira de Andrade Macêdo  | 15/0137397  |

## Installation

> * ``` git clone https://github.com/projeto-de-algoritmos/Graphs-List1-DanielGoncalves-LucasMacedo.git ``` <br> <br>
> * ``` pip3 install -r requirements.txt --user ```

## Execution

> * ``` python3 graph-list1.py ```

## About Maze

<p align="justify"> A maze is a path or collection of paths, typically from an entrance to a goal. 
The word is used to refer both to branching tour puzzles through which the solver must find a route, 
and to simpler non-branching patterns that lead unambiguously through a convoluted layout to a goal. </p>

### Generating Mazes

<p align="justify"> Maze generation is the act of designing the layout of passages and walls within a maze. 
There are many different approaches to generating mazes, with various maze generation algorithms for building them, 
either by hand or automatically by computer.
There are two main mechanisms used to generate mazes. 
In "carving passages", one marks out the network of available routes. In building a maze by "adding walls", 
one lays out a set of obstructions within an open area. Most mazes drawn on paper are done by drawing the walls, 
with the spaces in between the markings composing the passages. </p>

### Solving Mazes

<p align="justify"> Maze solving is the act of finding a route through the maze from the start to finish. 
Some maze solving methods are designed to be used inside the maze by a traveler with no prior knowledge of the maze, 
whereas others are designed to be used by a person or computer program that can see the whole maze at once.
The mathematician Leonhard Euler was one of the first to analyze plane mazes mathematically, 
and in doing so made the first significant contributions to the branch of mathematics known as topology.
Mazes containing no loops are known as "standard", or "perfect" mazes, and are equivalent to a tree in graph theory. 
Thus many maze solving algorithms are closely related to graph theory. Intuitively, 
if one pulled and stretched out the paths in the maze in the proper way, the result could be made to resemble a tree. </p>

## Maze Adventures

### Maze generation algorithm

#### Recursive backtracker using Depth-First Search

> 1. Make the initial cell the current cell and mark it as visited
> 2. While there are unvisited cells
>>      1. If the current cell has any neighbours which have not been visited
>>>             1. Choose randomly one of the unvisited neighbours
>>>             2. Push the current cell to the stack
>>>             3. Remove the wall between the current cell and the chosen cell
>>>             4. Make the chosen cell the current cell and mark it as visited
>>      2. Else if stack is not empty
>>>             1. Pop a cell from the stack
>>>             2. Make it the current cell

<br> ![generate-maze](gifs/generate_maze.gif) <br>

### Maze solving algorithm

#### Breadth-First Search

> 1. Define an initial node, marking as exploited
> 2. Add it to the queue
> 3. While the queue is not empty and you have not found the end of the maze
>> 	1. Remove the first node from the queue, **U**
>> 	2. For each neighbor **V** of **U**
>>>             1. If you have not explored
>>>>             	1. Mark U as the parent of V
>>>>               	2. Mark V as scanned
>>>>               	3. Put V at the end of the queue.
>>>>               	4. If V is the end of the maze
>>>>>                 	1. The end was found
> 4. Define the current node as the end of the maze
> 5. While the father of the node's parent is not empty
>>      1. Assign the current node as your parent, to walk the way back
       
<br> ![solving-maze](gifs/solving_maze.gif) <br>

## References

> * https://gifs.com/ <br>
> * https://en.wikipedia.org/wiki/Maze <br>
> * https://en.wikipedia.org/wiki/Maze_generation_algorithm <br>
> * https://en.wikipedia.org/wiki/Maze_solving_algorithm
