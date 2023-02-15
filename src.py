import pandas as pd



#calculates Levenshtein distance between two strings a,b using dynamic programming algorithm
def getDistance(a,b):
    n=len(a)
    m=len(b)
    dp=[[1000]*(m+1) for _ in range(n + 1)]
    for i in range(0,m+1):
        dp[0][i]=i

    for i in range(1,n+1):
        dp[i][0]=i
        for j in range(1,m+1):
            if(a[i-1]==b[j-1]):
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
    return dp[n][m]

if __name__ == "__main__":
    # df = pd.read_csv('sample.csv')
    df = pd.read_csv('assignment_data.csv')
    from geopy.distance import geodesic

    #result data frame with classification as 1/0
    res=pd.DataFrame(columns=['name','latitude','longitude','is_similar'])

    for i in range(0,len(df)):
        baseLocation=(df.loc[i][1],df.loc[i][2])
        has_neighbour=0
        for j in range(0,len(df)):
            neighbour=(df.loc[j][1],df.loc[j][2])
            dis=geodesic(baseLocation, neighbour).km*1000
            if(dis<=200):
                if(getDistance(df.loc[i][0],df.loc[j][0])<5):
                    has_neighbour=1
                    break
        res.loc[i]=[df.loc[i][0],df.loc[i][1],df.loc[i][2],has_neighbour]

    res.to_csv('classified.csv',index=False)
        

