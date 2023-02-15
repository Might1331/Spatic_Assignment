if __name__ == "__main__":
    import pandas as pd
    from geopy.distance import geodesic

    #calculates Levenshtein distance between two strings a,b using dynamic programming algorithm
    def getDistance(a,b):
        n=len(a)
        m=len(b)
        dp=[[1000]*(m+1) for _ in range(n + 1)]
        for i in range( 0 , m+1 ):
            dp[0][i]=i

        for i in range(1,n+1):
            dp[i][0]=i
            for j in range(1,m+1):
                if(a[i-1]==b[j-1]):
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        return dp[n][m]

    df0 = pd.read_csv('assignment_data.csv')
    
    # sorted dataframe to decrease search space
    df=pd.DataFrame(columns=['name','latitude','longitude','idx'])
    for i in range(0,len(df0)):
        df.loc[i]=[df0.loc[i][0],df0.loc[i][1],df0.loc[i][2],i]
    df.sort_values(by='latitude',inplace=True)
    print("Sorted")
    
    # result dataframe with classification as 1/0
    finalAnswer=pd.DataFrame(columns=['name','latitude','longitude','is_similar'])
    for i in range(0,len(df)):
        baseLocation=(df.loc[i][1],df.loc[i][2])
        has_neighbour=0
        for j in range(i+1,len(df)):
            neighbour=(df.loc[j][1],df.loc[j][2])
            dis=geodesic(baseLocation, neighbour).km
            if(dis>0.2):
                break
            if(getDistance(df.loc[i][0],df.loc[j][0])<5):
                has_neighbour=1
                break
        finalAnswer.loc[df.iloc[i][3]]=[df.loc[i][0],df.loc[i][1],df.loc[i][2],has_neighbour]

    finalAnswer.to_csv('classified.csv',index=False)
    print(finalAnswer)


