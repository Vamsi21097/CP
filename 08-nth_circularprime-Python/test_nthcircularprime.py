import os,sys
sys.path.append(os.getcwd())
from nthcircularprime import nthcircularprime
import pytest


@pytest.mark.parametrize('x, result',[
	(1, 2), (2, 3), (3, 5), (4, 7), 
	(5, 13), (6, 17), (7, 31), (8, 37), 
	(9, 71), (10, 73), (11, 79), (12, 97), 
	(13, 113), (14, 131), (15, 197), (16, 199), 
	(17, 311), (18, 337), (19, 373), (20, 719), 
	(21, 733), (22, 919), (23, 971), (24, 991), 
	(25, 1193), (26, 1931), (27, 3119), (28, 3779), 
	(29, 7793), (30, 7937), (31, 9311), (32, 9377), 
	(33, 11939), (34, 19391), (35, 19937), (36, 37199), 
	(37, 39119), (38, 71993), (39, 91193), (40, 93719), 
	(41, 93911), (42, 99371), (43, 193939), (44, 199933), 
	(45, 319993), (46, 331999), (47, 391939)
])

def test_nthcircularprime(x, result):
	assert nthcircularprime(x) == result
