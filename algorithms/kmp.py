def computeLPSArray(pat): 
    val = 0 
    lps = [0]*len(pat)
    # lps[0]
    i = 1
    while i < len(pat): 
        if pat[i]== pat[val]: 
            val += 1
            # uncomment for non - overlap
            # if 2*val > i+1:
	        # 	val = lps[val - 1]
            lps[i] = val
            i += 1
        else: 
            if val != 0: 
                val = lps[val-1]  
            else: 
                lps[i] = 0
                i += 1
    return lps