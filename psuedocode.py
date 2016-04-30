def findDistrict(tracts):
    #Check to see if we are done
    # each loop is O(N*lg(N)) and we must run this n times so overall runtime is O(N^2*lg(N)) where n is the number of tracts in the state 
    if district population >= targetPop
        return tracts
    # choose next district based on selection method
    toAdd = tract id of the highest valaue
    # once selection is made addtract will handle all of the set updates
    addTract(toAdd)

    if  ( district cannot grow any more but is still below target pop):
        return tracts
    # recursice call to add next tract
    return findDistrict(tracts)

def addTract (tract):
        # this method runs in n*lg(n) time since all of their subroutines can be bounded by n*lg(n)
        #add tract to the district
        dist.append(tract)
        #remove dist from adjset or set inDistrict flag
        adjSetl[tract] =-1
        # update pop
        pop=pop+ tract pop
        #update params
        params=updateParams(tract,params)
        #update adj set for new adjacent
        adjSetl=updateAdjSet(adjSetl,tract,params)
    return

def updateAdjSet(localAdjSet,index,params):
    # adjacent tracts for census tracts key in NEIGHBOR_TRACTID col
    # the worst case runtime is O(N*lg(N)) time
    toAdd = get all neighboring tracts
     # loop through those tracts and see if they are in the district if not upadate their values
    for i in range(0,toAdd.shape[0]):#
            if (tract is already in a district):
                # do nothing this value is alredy been added to the district
            else:
                #calculate the valaue
                localAdjSet[key]=calcValue(key,params)
    return localAdjSet

def calcValue(toAdd,params):
    # calculates the value of the tract this is a constant time operation using the value function described in the text
    #O(lg(N)) time since all values are just accesing know indices of a matrix or map
    val= value function (toAdd,params)
    return val

def updateParams(toAdd,params):
    # update the params in consant time with welfords method
    #O(lg(N)) time since querries are in effect binary serches in pandas
    return params
