# OPgg-aggregator

This tool calculates the average of all the viewable OP scores in the OP.GG match history.

Directions for use:

`python opggscorecalculator.py [options]`

If no users are specified in the options, then by default, the aggregator will calculate the op.gg scores of the following summoners:
* MAN OF INTELLECT
* Commandments
* MunichMonster
* Lazersquirrel
* Shmaul Cat


## [options]

`--verbose`

outputs more information when gathering op.gg data.

`--grouped`

Only selects games where all users that were included in the options are participating in the games.

`-u [summonername]`

Selects the summoner to average their op.gg score. Multiple summoners can be selected by doing `-u [summoner1] -u [summoner2] -u [summoner3]` ... 

Space characters in the summoner's name must be replaced with underscore characters. Names are not case-sensitive.


`-r [region]`

specifies the region. Valid regions are: 

* na 
* lan 
* las
* br 
* eune 
* euw
* kr 
* jp 
* oce 
* tr
* ru

`-l [limit-number]`

specifies a cap on the past number of games to calculate. For example, `-l 10` would limit the aggregate calculation to the last 10 games.

`-m [game-mode]`

specifies the game mode. Valid game modes are:

* solo
* flex
* norm
* ranked -- includes games from both flex and solo.
