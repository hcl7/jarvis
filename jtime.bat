if %time:~0,-9% GTR 12 (set /a timehour=%time:~0,-9%-12) else set timehour=%time:~0,-9%
if %time:~3,1%==0 (set timeminute=%time:~4,1%) else set timeminute=%time:~3,2%
echo It is currently %timeminute% minutes past %timehour%, sir.
nircmd speak text "It is currently %timeminute% minutes past %timehour%, sir."