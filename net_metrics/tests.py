import net_metrics

#same as sample network described in Wikipedia paper
sample_net = {'A': 'B', 'B':'C', 'C':'A', 'D':'C', 'E':'C',
              'G':'E', 'F':'E'}

#sample net with list values (one node pointing to several nodes)
sample_net_multiple_nodes = {'A':['B'], 'B':['C'], 'C':['A'], 'E':['C'], 'D':['E', 'C']}

def test_traversal_visits():
    """
    tests result of traversal visits computation
    """
    traversal_visits = net_metrics.compute_traversal_visits(sample_net)
    assert traversal_visits['A'] == 7 
    assert traversal_visits['E'] == 2 
    assert traversal_visits['G'] == 0

    
def test_traversal_funnels():
    """
    tests result of traversal funnels computation
    """
    pass
