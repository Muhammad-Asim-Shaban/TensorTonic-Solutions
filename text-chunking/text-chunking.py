def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    n=len(tokens)
    final_result=[]
    check=False
    final_value=0
    while final_value<n:
        check=False
        newlist=[]
        for i in range(final_value,final_value+chunk_size):
            if i >=n:
                check=True
                break 
            else:
                newlist.append(tokens[i])
         
        
        final_result.append(newlist)

        if final_value + chunk_size >= n:
            break
        final_value = final_value + chunk_size - overlap

    return final_result
        