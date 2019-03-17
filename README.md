# OPgg-aggregator

This tool calculates the average of all the viewable Ranked Flex 5v5 OP scores in the OP.GG match history.

Directions for use:

`python opggscorecalculator.py [options] -u [summoner-name-1] -u [summoner-name-2] -u [summoner-name-3]` ...

If no users are specified, then by default, the aggregator will calculate the OPgg scores of the following summoners:
* MAN OF INTELLECT
* Commandments
* MunichMonster
* Lazersquirrel
* Shmaul Cat


## [options]

`--verbose`

prints more information when gathering OPgg information.


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
