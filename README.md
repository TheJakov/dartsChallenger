# dartsChallenger

Console application made in Python for darts game lovers.🎯

Primary purpose behind making this app was learning more about Python.
 
### Running

```python3 dartsChallenger.py``` (Linux) 
or ```python3 .\dartsChallenger.py``` (Windows)

### Additional libraries

```pip install colorama```

### Preview

#### Adding players and number of rounds
<img alt="Preview1" src="https://github.com/TheJakov/dartsChallenger/blob/master/preview/app1.gif" width="882" height="502">

#### Example of playing challenges
<img alt="Preview2" src="https://github.com/TheJakov/dartsChallenger/blob/master/preview/app2.gif" width="882" height="502">


### Adding your own challenges is fun !

##### [Special type] (number of darts allowed) Description of challenge , +points (if succedded), -points (if failed)

**_Examples:_**


_"**[EPIC]** (3 darts) Score more than 60 points.", 15, 0_

_"**[EPIC]** (3 darts) Score less than 7 points - each dart MUST hit the target.", 15, 0_

_"(3 darts) Score any number of points between 20 and 30, including those numbers" + " - each dart MUST hit the target.", 10, 2_

_"(1 dart) You must hit even number.", 10, 5_

_"(1 dart) You must hit odd number.", 10, 5_

_"(2 darts) Sum of two darts must be an even number - each dart MUST hit the target.", 8, 3_

_"(2 darts) Sum of two darts must be an odd number - each dart MUST hit the target.", 8, 3_

_"(5 darts) You must hit BULLSEYE !", 30, 4_

_"**[LEGENDARY]** (1 dart) You must hit BULLSEYE ! (30 points, but then doubles total points)", 30, 0_

_"**[LEGENDARY]** (2 darts) You must hit number 7 two times. (15 points, but then doubles total points)", 15, 0_

_"(2 darts) You must hit one even and one odd number.", 15, 3_

_"**[UNLUCKY]** (2 darts) You must hit two numbers in range 11-16. (BULLSEYE is not included)", 0, 25_

_"(3 darts) You must hit two number neighbours. (e.g. 5 and 6, 18 and 17)", 12, 4_



**_Special type explanations:_**

_**EPIC** - no score decreasing upon not completing the challenge_

_**LEGENDARY** - gives points and after that doubles total points (HARD)_

_**UNLUCKY** - 0 points for completing, but removing 25 for not completing_

