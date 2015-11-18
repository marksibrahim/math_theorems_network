from collections import defaultdict

def compute_traversal_visits(net):
    """
    returns a dictionary: nodes --> number of visits
    input net is a dictionary of nodes and  single outward link
    """
    #initializes dictionary with 0 as default value 
    traversal_visits = defaultdict(int)

    for node in net:
        link = net.get(node, False)
        traversed = []
        while link not in traversed and link:
            traversal_visits[link] += 1
            traversed.append(link)
            link = net.get(link, False)
    return traversal_visits

        
        

