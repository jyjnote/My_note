def solution(players, callings):
    answer = {}
    idx={}
    for i in range(len(players)):
        answer[players[i]]=i
        idx[i]=players[i]
        
    for i in callings:
        j=answer[i]
        answer[i]=j-1
        imsi=idx[j-1]
        
        answer[imsi]=j
        idx[j-1]=i
        idx[j]=imsi
        
    
    return list(idx.values())