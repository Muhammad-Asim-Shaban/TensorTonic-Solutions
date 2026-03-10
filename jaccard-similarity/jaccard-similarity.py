def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_aa=set()
    set_bb=set()
    for value in set_a:
        set_aa.add(value)
    
    for value in set_b:
        set_bb.add(value)
    if len(set_aa)==0 and len(set_bb)==0:
        return 0.0
    set_total=set()
    for value in set_aa:
        set_total.add(value)
    for value in set_bb:
        set_total.add(value)
    intersection = set_aa & set_bb

    one=len(intersection)
    two=len(set_total)
    return (one/two)