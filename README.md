# Python Implementation of Recommendation ITU-R P.2109

This code repository contains a python software implementation of Recommendation [ITU-R P.2109-2](https://www.itu.int/rec/R-REC-P.2109/en) with a prediction procedure for  estimating building entry loss at frequencies between about 80 MHz and 100 GHz.

This version of the code is functionally identical to the reference Excel version approved by ITU-R Working Parties 3K and 3M and published by Study Group 3 on [ITU-R SG 3 Software, Data, and Validation Web Page](https://www.itu.int/en/ITU-R/study-groups/rsg3/Pages/iono-tropo-spheric.aspx). 

The package can be downloaded and installed using:
~~~
python -m pip install "git+https://github.com/eeveetza/Py2109/#egg=Py2109"   
~~~

and imported as follows
~~~
from Py2109 import P2109
~~~

The following table describes the structure of the folder.

| File/Folder               | Description                                                         |
|----------------------------|---------------------------------------------------------------------|
|`/src/Py2109/P2109.py`        | python implementation of Recommendation ITU-R P.2109      |
|`/tests/validateP2109.py`          | python script used to validate the implementation of Recommendation ITU-R P.2109 against reference implementation   |



## Function call

~~~
Lbe = bel_p2109(f, p, cl, th);
~~~

| Variable          | Type   | Units | Limits       | Description  |
|-------------------|--------|-------|--------------|--------------|
| `f`               | scalar double | GHz   | 0.08 ≤ `f` ≤ 100 | Frequency   |
| `p`          | scalar double | %    |  0 < `p` < 100 | Probability for which the loss is not exceeded |
| `cl`           | scalar int    |     | 1  or 2             |  Building class:  </li><li>1: traditional</li><li>2: thermally efficient</li></ul> |
| `th`          | scalar double | deg   | 0 ≤ `th` ≤ 90  | Elevation angle at the building facade (degrees above the horizontal)|


 ## Outputs ##

| Variable   | Type   | Units | Description |
|------------|--------|-------|-------------|
| `Lbe`    | double | dB    | Building entry loss |

## References

* [Recommendation ITU-R P.2109](https://www.itu.int/rec/R-REC-P.2109/en)

* [ITU-R SG 3 Software, Data, and Validation Web Page](https://www.itu.int/en/ITU-R/study-groups/rsg3/Pages/iono-tropo-spheric.aspx)