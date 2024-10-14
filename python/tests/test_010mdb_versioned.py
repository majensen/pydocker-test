import sys
import pytest
import pytest_docker
from neo4j import GraphDatabase
from pdb import set_trace

def test_mdb(mdb_versioned):
    (b, h) = mdb_versioned
    drv = GraphDatabase.driver(b, auth=("",""))
    drv.verify_connectivity()
    recs, summ, keys = drv.execute_query("match (a) return count(a) as ct",{});
    assert recs[0]['ct'] == 134
    drv.close()
    
        
